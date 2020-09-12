import click

from .palette import loads, DEFAULT_PALETTE, palette_to_bytes
from .image import image_to_bytes
from .array import convert
from .util import write_file


@click.group()
def common():
    pass


@common.group(help="Palette-related commands")
def pal():
    pass


@common.command(help="Convert graphics to VERA format")
@click.option("-p", "--palette", type=click.Path(exists=True))
@click.option("-f", "--format", type=click.Choice(["C-array"]), default="C-array")
@click.argument("input")
@click.argument("output")
@click.argument("symbol_name")
def gfx(palette, format, input, output, symbol_name):
    if not palette:
        loaded_palette = loads(DEFAULT_PALETTE)
    else:
        raise NotImplementedError()

    bytes_ = image_to_bytes(input, loaded_palette)
    data_out = convert(format, symbol_name, bytes_)
    write_file(output, data_out)


@pal.command()
@click.option("-p", "--palette", type=click.Path(exists=True))
@click.option("-f", "--format", type=click.Choice(["C-array"]), default="C-array")
@click.argument("output")
@click.argument("symbol_name")
def export(palette, format, output, symbol_name):
    if not palette:
        loaded_palette = loads(DEFAULT_PALETTE)
    else:
        raise NotImplementedError()
    bytes_ = palette_to_bytes(loaded_palette)
    data_out = convert(format, symbol_name, bytes_)
    write_file(output, data_out)
