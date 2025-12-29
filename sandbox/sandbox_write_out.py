from pathlib import Path
from src.eorbis_docbot.config import load_config
from src.eorbis_docbot.transforms.write_out_md import write_out_md

cfg = load_config()

# pega um arquivo md qualquer do input
sample = next(cfg.input_dir.glob("**/*.md"))

texto = sample.read_text(encoding="utf-8")
out_path = write_out_md(
    input_dir=cfg.input_dir,
    output_dir=cfg.output_dir,
    input_file=sample,
    md_text=texto,
)

print("Input:", sample)
print("Output:", out_path)
print("Existe?", out_path.exists())
