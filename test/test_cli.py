from tempfile import NamedTemporaryFile
from subprocess import run
from contextlib import contextmanager


def test_gfx_basic():
    with check_file_against("test/data/smile_tile.c") as output:
        run(
            ["cx16-conv", "gfx", "test/data/smile_tile.png", output, "SMILE_TILE"],
            check=True,
        )


def test_pal_default():
    with check_file_against("test/data/default_palette.c") as output:
        run(
            ["cx16-conv", "pal", "export", output, "DEFAULT_PAL"],
            check=True,
        )


@contextmanager
def check_file_against(expected):
    with NamedTemporaryFile() as temp:
        yield temp.name
        run(["diff", "-Nur", temp.name, expected], check=True)
