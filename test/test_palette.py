from cx16_conv.palette import loads, dumps, DEFAULT_PALETTE


def test_palette_loading():
    pal = loads(DEFAULT_PALETTE)
    text = dumps(pal)

    assert text == DEFAULT_PALETTE.strip()
