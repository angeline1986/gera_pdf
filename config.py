"""
Configurações do projeto Gera_pdf
"""

import os

# Diretórios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")
INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
TEMP_DIR = os.path.join(BASE_DIR, "temp")

# Subdirectórios de output
PDF_OUTPUT_DIR = os.path.join(OUTPUT_DIR, "pdfs")
IMAGES_OUTPUT_DIR = os.path.join(OUTPUT_DIR, "conversoes")

# Criar diretórios se não existirem
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(PDF_OUTPUT_DIR, exist_ok=True)
os.makedirs(IMAGES_OUTPUT_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

# Extensões suportadas
SUPPORTED_IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".webp")
SUPPORTED_PDF_EXTS = (".pdf",)

# Configurações de PDF
DEFAULT_PDF_RESOLUTION = 300.0
DEFAULT_PDF_DPI = 200

# Configurações de conversão
DEFAULT_IMAGE_MODE = "RGB"

# Nome padrão de saída
DEFAULT_PDF_NAME = "saida.pdf"
DEFAULT_IMAGE_PREFIX = "pagina_"
