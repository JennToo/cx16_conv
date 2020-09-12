import os
from tempfile import NamedTemporaryFile
from subprocess import run
from contextlib import contextmanager

SMILE_TILE_IMG = "test/data/smile_tile.png"


def test_gfx_basic():
    with check_file_against("test/data/smile_tile.c") as output:
        run(
            ["cx16-conv", "gfx", SMILE_TILE_IMG, output, "SMILE_TILE"],
            check=True,
        )


def test_pal_default():
    with check_file_against("test/data/default_palette.c") as output:
        run(
            ["cx16-conv", "pal", "export", output, "DEFAULT_PAL"],
            check=True,
        )


def test_pal_smile():
    with check_file_against("test/data/smile_tile.pal") as output:
        os.remove(output)
        run(
            ["cx16-conv", "pal", "generate", SMILE_TILE_IMG, output],
            check=True,
        )


@contextmanager
def check_file_against(expected):
    with NamedTemporaryFile() as temp:
        yield temp.name
        run(["diff", "-Nur", temp.name, expected], check=True)
