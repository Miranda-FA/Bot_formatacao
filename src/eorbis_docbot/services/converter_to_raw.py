from __future__ import annotations

from pathlib import Path

from src.eorbis_docbot.model.conversion_report import ConversionReport, ConversionError
from src.eorbis_docbot.transforms.list_md_files import list_md_files
from src.eorbis_docbot.transforms.obsidian import convert_obsidian_images
from src.eorbis_docbot.transforms.write_out_md import write_out_md


def run(*, input_dir: Path, output_dir: Path, base_url: str, recursive: bool = True) -> ConversionReport:
    report = ConversionReport()

    files = list_md_files(input_dir, recursive=recursive)
    report.total_files = len(files)

    for md_file in files:
        try:
            md_text = md_file.read_text(encoding="utf-8")

            md_converted, images = convert_obsidian_images(md_text, base_url)
            report.total_images_found += len(images)

            write_out_md(
                input_dir=input_dir,
                output_dir=output_dir,
                input_file=md_file,
                md_text=md_converted,
            )

            report.converted_files += 1

        except Exception as e:
            report.errors.append(ConversionError(file=str(md_file), error=str(e)))

    return report
