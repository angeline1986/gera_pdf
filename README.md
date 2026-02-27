# 📚 Gera PDF

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Repository size](https://img.shields.io/github/repo-size/angeline1986/gera_pdf)
![Top language](https://img.shields.io/github/languages/top/angeline1986/gera_pdf)

Ferramenta em Python para:

-   📸 Converter pastas de imagens em PDFs\
-   📄 Extrair imagens (PNG) de PDFs\
-   ⚡ Processamento automático por pasta

---

## 📌 Versão

v1.0.1

---
------------------------------------------------------------------------

## 📂 Estrutura do Projeto

    Gera_pdf/
    ├── src/
    │   ├── imagens_para_pdf.py
    │   ├── imagens_para_pdf_v2.py
    │   ├── pdf_para_png.py
    │   └── utils.py
    ├── input/              # Pastas com imagens
    ├── output/
    │   ├── pdfs/           # PDFs gerados
    │   └── conversoes/     # Imagens extraídas
    ├── temp/
    ├── config.py
    ├── main.py
    └── requirements.txt

------------------------------------------------------------------------

## 🚀 Instalação

### 1️⃣ Clone o repositório

    git clone https://github.com/angeline1986/gera_pdf.git
    cd gera_pdf

### 2️⃣ Crie e ative um ambiente virtual (recomendado)

    python -m venv .venv
    source .venv/bin/activate  # macOS/Linux

### 3️⃣ Instale as dependências

    pip install -r requirements.txt

------------------------------------------------------------------------

## 📸 Como usar

1.  Coloque suas pastas com imagens dentro de:

```{=html}
<!-- -->
```
    input/

Exemplo:

    input/
    ├── Capitulo 01/
    ├── Capitulo 02/

2.  Execute:

```{=html}
<!-- -->
```
    python main.py

------------------------------------------------------------------------

## 📌 Funcionalidades

### 📸 Opção 1 -- Imagens → PDF (v2 recomendado)

-   Cada pasta dentro de `input/` gera automaticamente **1 PDF**
-   O PDF terá o **mesmo nome da pasta**
-   Saída em:

```{=html}
<!-- -->
```
    output/pdfs/

### 📸 Opção 2 -- Imagens → PDF (v1)

Versão alternativa com abordagem diferente de geração.

### 📄 Opção 3 -- PDF → PNG

Extrai páginas de um PDF para:

    output/conversoes/

------------------------------------------------------------------------

## 📦 Observações

-   Pastas `input/`, `output/` e `temp/` não são versionadas no Git.
-   O projeto processa automaticamente todas as subpastas de `input/`.
-   Compatível com Python 3.10 -- 3.12.

------------------------------------------------------------------------

## 🛠 Dependências principais

-   Pillow
-   img2pdf
-   PyMuPDF
-   tqdm

------------------------------------------------------------------------

## 📄 Licença

Este projeto está licenciado sob a **MIT License**.\
Veja o arquivo `LICENSE` para mais detalhes.

------------------------------------------------------------------------

## 👩‍💻 Autora

Angeline\
GitHub: https://github.com/angeline1986
