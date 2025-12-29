from src.eorbis_docbot.config import load_config
from src.eorbis_docbot.services.converter_to_raw import run

cfg = load_config()

report = run(
    input_dir=cfg.input_dir,
    output_dir=cfg.output_dir,
    base_url=cfg.image_base_url,
    recursive=True,
)

print("Total arquivos:", report.total_files)
print("Convertidos:", report.converted_files)
print("Imagens encontradas:", report.total_images_found)
print("Erros:", len(report.errors))

if report.errors:
    print("Primeiro erro:")
    print(report.errors[0].file)
    print(report.errors[0].error)
