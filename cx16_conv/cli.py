import click


@click.group()
def common():
    pass


@common.command(help="Convert graphics to VERA format")
@click.option("-p", "--palette", type=click.Path(exists=True))
@click.option("-f", "--format", type=click.Choice(["C-array"]))
@click.argument("input")
@click.argument("output")
def gfx(palette, format, input, output):
    pass
