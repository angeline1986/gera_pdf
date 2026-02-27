import os
import sys
import time
from PIL import Image

# Importar configurações e utilitários
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
from .utils import natural_key, format_duration, get_supported_files

# tqdm é opcional: se não tiver instalado, roda sem barra
try:
    from tqdm import tqdm
except Exception:
    tqdm = None


def images_to_pdf(input_dir: str, output_pdf: str):
    image_paths = get_supported_files(input_dir, config.SUPPORTED_IMAGE_EXTS)
    if not image_paths:
        raise FileNotFoundError(f"Nenhuma imagem encontrada em '{input_dir}'.")

    loaded_images = []
    ignored = 0

    iterator = image_paths
    if tqdm is not None:
        iterator = tqdm(image_paths, desc="Processando imagens", unit="img")

    for path in iterator:
        try:
            img = Image.open(path)

            # Corrigir rotação EXIF (principalmente JPG)
            try:
                exif = img.getexif()
                orientation = exif.get(274)
                if orientation == 3:
                    img = img.rotate(180, expand=True)
                elif orientation == 6:
                    img = img.rotate(270, expand=True)
                elif orientation == 8:
                    img = img.rotate(90, expand=True)
            except Exception:
                pass

            # Garantir RGB (evita inconsistências no PDF)
            if img.mode != "RGB":
                img = img.convert("RGB")

            loaded_images.append(img)

        except Exception:
            print(f"⚠️ Ignorada (erro ao abrir): {os.path.basename(path)}")
            ignored += 1

    if not loaded_images:
        raise RuntimeError("Nenhuma imagem válida foi carregada.")

    # Salvar PDF multipágina na ordem já garantida
    first_image = loaded_images[0]
    remaining_images = loaded_images[1:]

    first_image.save(
        output_pdf,
        save_all=True,
        append_images=remaining_images,
        resolution=config.DEFAULT_PDF_RESOLUTION
    )

    # Fechar imagens
    for img in loaded_images:
        try:
            img.close()
        except Exception:
            pass

    return len(loaded_images), ignored


def images_to_pdf_interactive():
    """Executa conversão de imagens para PDF interativamente"""
    start = time.perf_counter()

    input_dir = config.INPUT_DIR
    output_dir = config.PDF_OUTPUT_DIR

    if not os.path.isdir(input_dir) or not os.listdir(input_dir):
        print("❌ Nenhuma pasta encontrada em 'input'.")
        return

    # Listar pastas disponíveis
    folders = [f for f in os.listdir(input_dir) 
               if os.path.isdir(os.path.join(input_dir, f)) and not f.startswith('.')]
    
    if not folders:
        print("❌ Nenhuma pasta encontrada em 'input'.")
        return

    print("\n📁 Pastas encontradas:")
    for i, folder in enumerate(folders, 1):
        print(f"{i}. {folder}")
    
    try:
        choice = int(input("\nEscolha uma pasta (número): "))
        if 1 <= choice <= len(folders):
            selected_folder = folders[choice - 1]
            selected_path = os.path.join(input_dir, selected_folder)
            output_pdf = os.path.join(output_dir, f"{selected_folder}.pdf")
        else:
            print("❌ Opção inválida.")
            return
    except ValueError:
        print("❌ Entrada inválida.")
        return

    os.makedirs(output_dir, exist_ok=True)

    try:
        total, ignored = images_to_pdf(selected_path, output_pdf)

        elapsed = time.perf_counter() - start

        print("\n✅ PDF gerado com sucesso!")
        print(f"📄 Arquivo: {output_pdf}")
        print(f"🖼️ Total de imagens incluídas: {total}")
        if ignored > 0:
            print(f"⚠️ Imagens ignoradas: {ignored}")
        print(f"⏱️ Tempo total: {elapsed:.2f}s ({format_duration(elapsed)})")

        if tqdm is None:
            print("ℹ️ (Dica) Instale 'tqdm' para ver barra de progresso: pip install tqdm")

    except Exception as e:
        elapsed = time.perf_counter() - start
        print(f"\n❌ Erro: {e}")
        print(f"⏱️ Tempo até falhar: {elapsed:.2f}s ({format_duration(elapsed)})")


if __name__ == "__main__":
    images_to_pdf_interactive()