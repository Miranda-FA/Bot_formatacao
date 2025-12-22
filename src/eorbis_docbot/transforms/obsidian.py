import re
from urllib.parse import quote



PATTERN_IMAGE = re.compile(r"!\[\[(.*?)\]\]")

def extract_image_names(md_text: str) -> list[str]:
    encontrados = PATTERN_IMAGE.findall(md_text)

    vistos = set()
    resultado = []
    for nome in encontrados:
        nome = nome.strip()
        if nome not in vistos:
            vistos.add(nome)
            resultado.append(nome)

    return resultado


def convert_obsidian_images(md_text: str, base_url: str) -> tuple[str, list[str]]:
    base_url = base_url.rstrip("/")
    imagens = []

    def replacer(match):
        nome = match.group(1).strip()
        if nome not in imagens:
            imagens.append(nome)

        url = f"{base_url}/{quote(nome)}"
        return f"![]({url})"

    md_convertido = PATTERN_IMAGE.sub(replacer, md_text)
    return md_convertido, imagens
