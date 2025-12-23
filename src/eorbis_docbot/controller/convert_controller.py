from __future__ import annotations
from dataclasses import dataclass, field

@dataclass
class ConversionError:
    file: str
    error: str

@dataclass
class ConversionReport:
    total_files: int = 0
    converted_files: int = 0
    total_images_found: int = 0
    errors: list[ConversionError] = field(default_factory=list)
