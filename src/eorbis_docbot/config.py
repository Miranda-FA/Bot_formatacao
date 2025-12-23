from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv


def _clean(value: str | None) -> str | None:
    if value is None:
        return None
    return value.strip().strip('"').strip("'")

@dataclass(frozen=True)
class Config:
    input_dir: Path
    output_dir: Path
    image_base_url: str
    doc_version: str | None = None
    logo_eorbis: str | None = None
    logo_metaprime: str | None = None


def load_config() -> Config:
    load_dotenv() 

    image_base_url = _clean(os.getenv("IMAGE_BASE_URL"))

    if not image_base_url:
        owner = _clean(os.getenv("GITHUB_OWNER"))
        repo = _clean(os.getenv("GITHUB_REPO"))
        branch = _clean(os.getenv("GITHUB_BRANCH")) or "main"
        images_dir = _clean(os.getenv("GITHUB_IMAGES_DIR"))

        if not owner or not repo or not images_dir:
            raise ValueError("Defina IMAGE_BASE_URL OU (GITHUB_OWNER, GITHUB_REPO, GITHUB_IMAGES_DIR).")

        image_base_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{images_dir.strip('/')}"

    input_dir = _clean(os.getenv("INPUT_DIR"))
    output_dir = _clean(os.getenv("OUTPUT_DIR"))
    if not input_dir or not output_dir:
        raise ValueError("INPUT_DIR e OUTPUT_DIR são obrigatórios (devem ser pastas).")

    return Config(
        input_dir=Path(input_dir),
        output_dir=Path(output_dir),
        image_base_url=image_base_url,
        doc_version=_clean(os.getenv("DOC_VERSION")),
        logo_eorbis=_clean(os.getenv("LOGO_EORBIS")),
        logo_metaprime=_clean(os.getenv("LOGO_METAPRIME")),
    )
