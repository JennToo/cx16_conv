import pytest

from cx16_conv.image import lookup_image_indices, extend_palette_from_image
from cx16_conv.palette import loads, blank_palette, DEFAULT_PALETTE
from cx16_conv.util import chunks

SMILE_TILE_INDEX = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 16, 0, 0, 16, 0, 0],
    [0, 0, 0, 27, 27, 0, 0, 0],
    [0, 16, 0, 27, 27, 0, 16, 0],
    [0, 0, 16, 16, 16, 16, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]


def test_image():
    palette = loads(DEFAULT_PALETTE)
    indices = lookup_image_indices("test/data/smile_tile.png", palette)

    assert list(chunks(indices, 8)) == SMILE_TILE_INDEX


def test_extend_palette():
    with pytest.raises(RuntimeError):
        extend_palette_from_image("test/data/too_many_colors.jpg", blank_palette())


def test_extend_palette_no_op():
    palette = loads(DEFAULT_PALETTE)
    extend_palette_from_image("test/data/smile_tile.png", palette)
    clean_palette = loads(DEFAULT_PALETTE)
    assert palette.colors == clean_palette.colors
