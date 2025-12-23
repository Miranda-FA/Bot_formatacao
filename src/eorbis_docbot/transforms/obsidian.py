from __future__ import annotations

import re
from urllib.parse import quote
from typing import Tuple,List

_OBSIDIAN_EMBED_REGEX = re.compile(r'!\[\[(.*?)\]\]')
_IMAGE_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.webp', '.tiff'}

def _is_image(filename: str) -> bool:
    lower = filename.lower()
    return lower.endswith(_IMAGE_EXTENSIONS)

def convert_obsidian_images (md_text: str, base_url: str) -> Tuple[str, List[str]]:
    base = base_url.rstrip('/')
    seen: set[str] = set()
    images: list[str] = []

    def replacer(match: re.Match) -> str:
        inner = match.group(1).strip()
        if not _is_image(filename):
            return match.group(0)

        if filename not in seen:
            seen.add(filename)
            images.append(filename)
        
        url = f"{base}/{quote(filename)}"
        return f"![]({url})"
    
    converted = _OBSIDIAN_EMBED_REGEX.sub(replacer_md_text)
    return converted, images