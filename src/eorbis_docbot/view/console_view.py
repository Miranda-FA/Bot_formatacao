from __future__ import annotations

from src.eorbis_docbot.model.conversion_report import ConversionReport


def render(report: ConversionReport) -> None:
    print("\n=== Resultado da Conversão ===")
    print(f"Total arquivos encontrados : {report.total_files}")
    print(f"Arquivos convertidos       : {report.converted_files}")
    print(f"Imagens encontradas        : {report.total_images_found}")
    print(f"Erros                      : {len(report.errors)}")

    if report.errors:
        print("\n--- Primeiros erros ---")
        for err in report.errors[:10]:
            print(f"- {err.file}")
            print(f"  {err.error}")
