from cx16_conv.palette import loads, dumps, DEFAULT_PALETTE, Color


def test_palette_loading():
    pal = loads(DEFAULT_PALETTE)
    text = dumps(pal)

    assert text.strip() == DEFAULT_PALETTE.strip()
    assert pal.index_by_color[Color(red=187, green=187, blue=187)] == 27
