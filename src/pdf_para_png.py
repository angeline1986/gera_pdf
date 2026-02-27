import os
import sys
import fitz  # PyMuPDF

# Importar configurações
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

def pdf_to_pngs(pdf_path: str, out_dir: str, dpi: int = None):
    if dpi is None:
        dpi = config.DEFAULT_PDF_DPI
    
    os.makedirs(out_dir, exist_ok=True)

    doc = fitz.open(pdf_path)

    zoom = dpi / 72.0
    matrix = fitz.Matrix(zoom, zoom)

    for i in range(doc.page_count):
        page = doc.load_page(i)
        pix = page.get_pixmap(matrix=matrix, alpha=False)

        output_file = os.path.join(out_dir, f"{config.DEFAULT_IMAGE_PREFIX}{i+1:04d}.png")
        pix.save(output_file)

    doc.close()
    return doc.page_count


def pdf_to_pngs_interactive():
    """Executa conversão de PDF para imagens interativamente"""
    input_dir = config.PDF_OUTPUT_DIR
    output_dir = config.IMAGES_OUTPUT_DIR

    if not os.path.exists(input_dir):
        print("❌ Pasta 'output/pdfs' não encontrada.")
        return

    # Procurar PDFs na pasta
    pdf_files = [f for f in os.listdir(input_dir) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("❌ Nenhum PDF encontrado em 'output/pdfs'.")
        return

    print("\n📄 PDFs encontrados:")
    for i, pdf in enumerate(pdf_files, 1):
        print(f"{i}. {pdf}")
    
    try:
        choice = int(input("\nEscolha um PDF (número): "))
        if 1 <= choice <= len(pdf_files):
            selected_pdf = pdf_files[choice - 1]
            pdf_path = os.path.join(input_dir, selected_pdf)
            # Criar pasta com o nome do PDF (sem extensão)
            pdf_name = os.path.splitext(selected_pdf)[0]
            output_subdir = os.path.join(output_dir, pdf_name)
        else:
            print("❌ Opção inválida.")
            return
    except ValueError:
        print("❌ Entrada inválida.")
        return

    print(f"📄 Convertendo: {selected_pdf}")
    page_count = pdf_to_pngs(pdf_path, output_subdir, dpi=config.DEFAULT_PDF_DPI)
    print(f"✅ Conversão concluída! {page_count} PNGs gerados em 'output/conversoes/{pdf_name}'.")


if __name__ == "__main__":
    pdf_to_pngs_interactive()