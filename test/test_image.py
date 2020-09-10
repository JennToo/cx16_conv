from cx16_conv.image import lookup_image_indices
from cx16_conv.palette import loads, DEFAULT_PALETTE
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
