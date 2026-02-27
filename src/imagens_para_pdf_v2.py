import os
import sys
import time
from typing import List, Tuple

from PIL import Image

# Garantir import do config.py na raiz do projeto (Gera_pdf/config.py)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import config
from .utils import natural_key, format_duration, get_supported_files

# tqdm é opcional
try:
    from tqdm import tqdm
except Exception:
    tqdm = None


def _fix_exif_orientation(img: Image.Image) -> Image.Image:
    """Corrige rotação usando EXIF (quando existir)."""
    try:
        exif = img.getexif()
        orientation = exif.get(274)  # 274 = Orientation
        if orientation == 3:
            return img.rotate(180, expand=True)
        if orientation == 6:
            return img.rotate(270, expand=True)
        if orientation == 8:
            return img.rotate(90, expand=True)
    except Exception:
        pass
    return img


def _ensure_rgb(img: Image.Image) -> Image.Image:
    """Garante modo RGB para salvar em PDF."""
    if img.mode == "RGB":
        return img
    # Se tiver alpha, aplica fundo branco (PDF via PIL não lida bem com RGBA)
    if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
        bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
        img = img.convert("RGBA")
        img = Image.alpha_composite(bg, img).convert("RGB")
        return img
    return img.convert("RGB")


def images_to_pdf(input_folder: str, output_pdf: str) -> Tuple[int, int]:
    """
    Converte todas as imagens suportadas dentro de uma pasta em um único PDF.

    Retorna:
      (total_incluidas, total_ignoradas)
    """
    images_paths = get_supported_files(input_folder, config.SUPPORTED_IMAGE_EXTS)
    images_paths.sort(key=natural_key)

    if not images_paths:
        raise RuntimeError(f"Nenhuma imagem suportada encontrada em: {input_folder}")

    loaded: List[Image.Image] = []
    ignored = 0

    iterator = images_paths
    if tqdm is not None:
        iterator = tqdm(images_paths, desc=f"Lendo imagens: {os.path.basename(input_folder)}", unit="img")

    for path in iterator:
        try:
            with Image.open(path) as im:
                im = _fix_exif_orientation(im)
                im = _ensure_rgb(im)
                loaded.append(im.copy())
        except Exception:
            ignored += 1

    if not loaded:
        raise RuntimeError(f"Todas as imagens falharam ao abrir em: {input_folder}")

    os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

    # Salva PDF multipágina
    first, rest = loaded[0], loaded[1:]
    first.save(
        output_pdf,
        "PDF",
        resolution=getattr(config, "DEFAULT_PDF_RESOLUTION", 100.0),
        save_all=True,
        append_images=rest,
    )

    # liberar memória
    for im in loaded:
        try:
            im.close()
        except Exception:
            pass

    return len(images_paths) - ignored, ignored


def convert_all_input_folders(
    input_root: str = None,
    output_root: str = None,
    skip_existing: bool = True,
) -> None:
    """
    Varre todas as pastas dentro de input_root e gera 1 PDF por pasta.
    Nome do PDF = nome da pasta.
    """
    input_root = input_root or config.INPUT_DIR
    output_root = output_root or config.PDF_OUTPUT_DIR

    if not os.path.isdir(input_root):
        print(f"❌ Pasta input não existe: {input_root}")
        return

    folders = [
        d for d in os.listdir(input_root)
        if os.path.isdir(os.path.join(input_root, d)) and not d.startswith('.')
    ]
    folders.sort(key=natural_key)

    if not folders:
        print("❌ Nenhuma pasta encontrada em 'input'.")
        return

    os.makedirs(output_root, exist_ok=True)

    print(f"\n📁 Pastas encontradas em '{input_root}':")
    for f in folders:
        print(f"- {f}")

    start_all = time.perf_counter()
    ok = 0
    fail = 0

    for folder in folders:
        folder_path = os.path.join(input_root, folder)
        output_pdf = os.path.join(output_root, f"{folder}.pdf")

        if skip_existing and os.path.exists(output_pdf):
            print(f"\n⏭️  Pulando (já existe): {output_pdf}")
            continue

        print(f"\n➡️  Gerando: {output_pdf}")
        start = time.perf_counter()
        try:
            total, ignored = images_to_pdf(folder_path, output_pdf)
            elapsed = time.perf_counter() - start
            ok += 1
            print("✅ Concluído!")
            print(f"🖼️  Imagens incluídas: {total} | ignoradas: {ignored}")
            print(f"⏱️  Tempo: {elapsed:.2f}s ({format_duration(elapsed)})")
        except Exception as e:
            elapsed = time.perf_counter() - start
            fail += 1
            print(f"❌ Falhou: {e}")
            print(f"⏱️  Tempo até falhar: {elapsed:.2f}s ({format_duration(elapsed)})")

    elapsed_all = time.perf_counter() - start_all
    print("\n" + "=" * 60)
    print("🏁 Finalizado")
    print(f"✅ Pastas convertidas: {ok}")
    print(f"❌ Pastas com erro: {fail}")
    print(f"⏱️  Tempo total: {elapsed_all:.2f}s ({format_duration(elapsed_all)})")
    print(f"📂 PDFs em: {output_root}")
    if tqdm is None:
        print("ℹ️ (Dica) Instale 'tqdm' para ver barra de progresso: pip install tqdm")
    print("=" * 60 + "\n")


def main():
    """Entrada usada pelo main.py do projeto."""
    convert_all_input_folders()


if __name__ == "__main__":
    main()
