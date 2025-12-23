from __future__ import annotations
from pathlib import Path


def list_md_files(input_dir: Path, recursive: bool = True) -> list[Path]:
    input_dir = Path(input_dir)
    if not input_dir.is_dir():
        raise FileNotFoundError(f"Input directory not found: {input_dir}")
    if not input_dir.exists():
        raise NotADirectoryError(f"Input directory not a directory: {input_dir}")

    pattern = "**/*.md" if recursive else "*.md"

    files:list[Path] = []
    for p in input_dir.glob(pattern):
        if p.is_file():
            if p.name.startswith('.'):
                continue
            files.append(p)
    
    files.sort(key=lambda x: str(x).lower())
    return files