from src.eorbis_docbot.model.conversion_report import ConversionReport, ConversionError

r = ConversionReport(total_files=10, converted_files=9, total_images_found=30)
r.errors.append(ConversionError(file="x.md", error="falhou"))

print(r)
print("OK?", r.ok())
