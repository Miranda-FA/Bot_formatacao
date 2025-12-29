from __future__ import annotations

from eorbis_docbot.config import load_config
from eorbis_docbot.services.converter_to_raw import run
from eorbis_docbot.view.console_view import render


def main() -> None:
    cfg = load_config()

    report = run(
        input_dir=cfg.input_dir,
        output_dir=cfg.output_dir,
        base_url=cfg.image_base_url,
        recursive=True,
    )

    render(report)
