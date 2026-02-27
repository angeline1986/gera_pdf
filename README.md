# Gera PDF 📚

Ferramenta Python para converter imagens em PDF multipágina e vice-versa.

## 📁 Estrutura do Projeto

```
Gera_pdf/
├── src/                           # Código-fonte
│   ├── __init__.py
│   ├── imagens_para_pdf.py       # Converte imagens → PDF
│   ├── pdf_para_png.py           # Converte PDF → Imagens
│   └── utils.py                  # Funções utilitárias
├── input/                         # Pasta com imagens para converter
│   ├── O Conto de Fadas da Madrasta cap 51_60/
│   ├── O caçador quer viver em silencio cap 12_18/
│   ├── O caçador quer viver em silencio cap 6_11/
│   └── Semantic Error cap 46_54/
├── output/
│   ├── pdfs/                     # PDFs gerados
│   └── conversoes/               # Imagens extraídas de PDFs
├── temp/                         # Arquivos temporários
├── config.py                     # Configurações e constantes
├── main.py                       # Menu principal (executar isto!)
├── requirements.txt              # Dependências
├── .gitignore                    # Arquivos ignorados pelo Git
└── README.md                     # Este arquivo
```

## 🚀 Como Usar

### Instalação das Dependências

```bash
pip install -r requirements.txt
```

### Executar o Menu Principal

```bash
python main.py
```

Ou diretamente no terminal:

```bash
python3 main.py
```

Você verá um menu como este:

```
============================================================
📚 GERA PDF - Menu Principal
============================================================
1. 📸 Imagens → PDF
2. 📄 PDF → Imagens (PNG)
3. ❌ Sair
============================================================
```

### Operação 1: Imagens → PDF

1. Coloque as imagens em uma pasta dentro de `input/`
2. Escolha a opção **1** no menu
3. Selecione a pasta que deseja converter
4. O PDF será gerado em `output/pdfs/`

**Formatos suportados:** PNG, JPG, JPEG, WEBP

### Operação 2: PDF → Imagens

1. Coloque os PDFs na pasta `output/pdfs/`
2. Escolha a opção **2** no menu
3. Selecione o PDF que deseja converter
4. As imagens serão geradas em `output/conversoes/`

**Formato de saída:** PNG em 200 DPI

## ⚙️ Configurações

Edite o arquivo `config.py` para alterar:

- **Resolução do PDF:** `DEFAULT_PDF_RESOLUTION`
- **DPI das imagens:** `DEFAULT_PDF_DPI`
- **Modo de cor das imagens:** `DEFAULT_IMAGE_MODE`
- **Prefixo das imagens:** `DEFAULT_IMAGE_PREFIX`

## 📦 Dependências

- `Pillow` - Processamento de imagens
- `PyMuPDF` - Manipulação de PDFs
- `tqdm` - Barra de progresso (opcional)

## ✨ Recursos

✅ Converte múltiplas imagens em PDF multipágina  
✅ Corrige rotação automática (EXIF)  
✅ Ordena imagens naturalmente (num1, num2, num10 ao invés de num1, num10, num2)  
✅ Extrai imagens de PDFs com alta qualidade  
✅ Menu interativo e amigável  
✅ Tratamento completo de erros  
✅ Barra de progresso opcional  

## 🐛 Solução de Problemas

### Erro: "Pillow não está instalado"
```bash
pip install Pillow
```

### Erro: "PyMuPDF não está instalado"
```bash
pip install PyMuPDF
```

### Erro: "tqdm não está instalado" (aviso)
```bash
pip install tqdm
```

Nota: `tqdm` é opcional. O programa funciona sem ele, apenas sem a barra de progresso.

## 📝 Exemplos

### Converter pasta de capítulos em PDF

```
1. Salve as imagens em: input/Meu_Capitulo/
2. Execute: python main.py
3. Escolha opção 1
4. Selecione a pasta
5. PDF criado em: output/pdfs/Meu_Capitulo.pdf
```

### Extrair imagens de um PDF

```
1. Coloque o PDF em: output/pdfs/
2. Execute: python main.py
3. Escolha opção 2
4. Selecione o PDF
5. Imagens em: output/conversoes/nome_do_pdf/
```

## 📄 Licença

Este projeto é de uso livre.

---

**Desenvolvido por:** Seu Nome  
**Data:** 2026
