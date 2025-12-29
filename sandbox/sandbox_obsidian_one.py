from src.eorbis_docbot.config import load_config
from src.eorbis_docbot.transforms.obsidian import convert_obsidian_images
from pathlib import Path

cfg = load_config()

sample = next(Path(cfg.input_dir).glob("**/*.md"))

md = sample.read_text(encoding="utf-8")
md2, images = convert_obsidian_images(md, cfg.image_base_url)

print("Arquivo:", sample)
print("Imagens encontradas:", len(images))
if images:
    print("Exemplo URL:", f"{cfg.image_base_url}/{images[0]}")

Path("saida_convertida_teste.md").write_text(md2, encoding="utf-8")
print("OK: saida_convertida_teste.md gerado")
