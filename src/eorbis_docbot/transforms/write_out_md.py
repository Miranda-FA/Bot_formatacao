from __future__ import annotations
from pathlib import Path

def write_out_md(*, input_dir: Path, output_dir: Path, input_file: Path, md_text: str) -> Path:
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)   
    input_file = Path(input_file)   

    relative_path = input_file.relative_to(input_dir)
    output_file = output_dir / relative_path
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(md_text, encoding="utf-8")
    
    return output_file