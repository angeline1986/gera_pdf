import os
from collections import Counter
from PIL import Image

EXTS = (".png", ".jpg", ".jpeg", ".webp")


def analisar_pasta(root: str = "input") -> None:
    total = 0
    erros = 0

    tamanhos = Counter()
    modos = Counter()
    alpha_count = 0
    exif_rot_count = 0

    por_pasta = Counter()

    for path, _, files in os.walk(root):
        for f in files:
            if not f.lower().endswith(EXTS):
                continue

            total += 1
            fp = os.path.join(path, f)
            pasta_rel = os.path.relpath(path, root)
            por_pasta[pasta_rel] += 1

            try:
                with Image.open(fp) as img:
                    tamanhos[img.size] += 1
                    modos[img.mode] += 1

                    # alpha (transparência)
                    if img.mode in ("RGBA", "LA"):
                        alpha_count += 1
                    elif img.mode == "P":
                        # PNGs em paleta podem ter transparência via info
                        if "transparency" in img.info:
                            alpha_count += 1

                    # EXIF Orientation (fotos de celular)
                    exif = img.getexif()
                    if exif and exif.get(274, 1) in (3, 6, 8):
                        exif_rot_count += 1

            except Exception:
                erros += 1

    print("\n=== RELATÓRIO DE IMAGENS ===")
    print(f"📁 Raiz analisada: {root}")
    print(f"🖼️ Total de imagens: {total}")
    print(f"⚠️ Arquivos com erro ao abrir: {erros}")

    print("\n--- Imagens por pasta (top 20) ---")
    for pasta, qtd in por_pasta.most_common(20):
        print(f"{pasta} -> {qtd}")

    print("\n--- Tamanhos mais comuns (top 20) ---")
    for (w, h), qtd in tamanhos.most_common(20):
        print(f"({w}x{h}) -> {qtd}")

    print("\n--- Modos de cor ---")
    for modo, qtd in modos.most_common():
        print(f"{modo} -> {qtd}")

    print("\n--- Sinais importantes ---")
    print(f"🟦 Com transparência (alpha): {alpha_count}")
    print(f"🧭 Com EXIF rotation: {exif_rot_count}")

    # Heurística simples pra decisão
    print("\n=== SUGESTÃO AUTOMÁTICA ===")
    if total == 0:
        print("Nenhuma imagem encontrada.")
        return

    variacao_tamanho = len(tamanhos)
    print(f"📐 Quantidade de tamanhos diferentes: {variacao_tamanho}")

    if alpha_count == 0 and exif_rot_count == 0 and variacao_tamanho <= 3:
        print("✅ Cenário ideal para img2pdf puro (máxima fidelidade e pouca RAM).")
    else:
        print("⚠️ Recomendo abordagem híbrida (img2pdf + correções pontuais):")
        if exif_rot_count > 0:
            print("- corrigir EXIF rotation nas imagens afetadas")
        if alpha_count > 0:
            print("- remover alpha / aplicar fundo sólido nas imagens com transparência")
        if variacao_tamanho > 3:
            print("- considerar pagesize fixo (ex: A4) com 'fit' para consistência")


if __name__ == "__main__":
    # roda a partir da raiz do projeto (Gera_pdf/)
    analisar_pasta("input")