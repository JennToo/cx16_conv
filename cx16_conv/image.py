from typing import List

from PIL import Image

from .palette import Color, Palette


def image_to_bytes(image_path: str, palette: Palette) -> bytes:
    return b"".join(
        [
            index.to_bytes(1, "little")
            for index in lookup_image_indices(image_path, palette)
        ]
    )


def lookup_image_indices(path: str, palette: Palette) -> List[int]:
    indices = []
    img = Image.open(path)
    (width, height) = img.size
    for y in range(0, height):
        for x in range(0, width):
            (red, green, blue, alpha) = img.getpixel((x, y))
            if alpha == 0:
                indices.append(0)
            else:
                color = Color(red=red, green=green, blue=blue)
                indices.append(palette.index_by_color[color])
    return indices
