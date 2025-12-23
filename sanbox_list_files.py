from src.eorbis_docbot.config import load_config
from src.eorbis_docbot.transforms.list_md_files import list_md_files

cfg = load_config()

files = list_md_files(cfg.input_dir, recursive=True)

print("Total .md encontrados:", len(files))
print("Primeiros 10:")
for f in files[:100]:
    print("-", f)
