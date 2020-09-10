from tempfile import NamedTemporaryFile
from subprocess import run


def test_gfx_basic():
    with NamedTemporaryFile() as temp:
        run(
            ["cx16-conv", "gfx", "test/data/smile_tile.png", temp.name, "SMILE_TILE"],
            check=True,
        )
        run(["diff", "-Nur", temp.name, "test/data/smile_tile.c"], check=True)
