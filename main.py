#!/usr/bin/env python3
"""
Menu principal - Gera PDF
Ferramenta para converter imagens em PDF e vice-versa
"""

import os
import sys

# Garantir que a raiz do projeto esteja no sys.path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

from src.pdf_para_png import pdf_to_pngs_interactive
from src.imagens_para_pdf_v2 import main as imagens_para_pdf_v2_main


def print_menu():
    """Exibe o menu principal"""
    print("\n" + "=" * 60)
    print("📚 GERA PDF - Menu Principal")
    print("=" * 60)
    print("1. 📸 Imagens → PDF")
    print("2. 📄 PDF → Imagens (PNG)")
    print("3. ❌ Sair")
    print("=" * 60)


def main():
    """Função principal com menu interativo"""
    while True:
        print_menu()

        try:
            choice = input("\nEscolha uma opção: ").strip()

            if choice == "1":
                print("\n📸 Convertendo imagens para PDF...")
                imagens_para_pdf_v2_main()

            elif choice == "2":
                print("\n📄 Convertendo PDF para imagens (PNG)...")
                pdf_to_pngs_interactive()

            elif choice == "3":
                print("\n👋 Até logo!")
                break

            else:
                print("\n⚠️  Opção inválida. Tente novamente.")

        except KeyboardInterrupt:
            print("\n\n👋 Operação cancelada. Até logo!")
            break
        except Exception as e:
            print(f"\n❌ Erro: {e}")


if __name__ == "__main__":
    main()