"""
provides arithmetic operation cmd-commands
"""

# std-lib
import click

# local-lib
from . import calc


@click.command()
@click.argument("a", nargs=1)
@click.argument("b", nargs=1)
def add(a: int, b: int):
    """ cmd command for addition operations """
    r = calc.add(int(a), int(b))
    click.echo(f"{a} + {b} = {r}")
    return r


@click.command()
@click.argument("a", nargs=1)
@click.argument("b", nargs=1)
def sub(a: int, b: int):
    """ cmd command for subtraction operations """
    r = calc.sub(int(a), int(b))
    click.echo(f"{a} - {b} = {r}")
    return r


@click.command()
@click.argument("a", nargs=1)
@click.argument("b", nargs=1)
def multi(a: int, b: int):
    """ cmd command for multiplication operations """
    r = calc.multi(int(a), int(b))
    click.echo(f"{a} * {b} = {r}")
    return r


@click.command()
@click.argument("a", nargs=1)
@click.argument("b", nargs=1)
def divide(a: int, b: int):
    """ cmd command for division operations """
    r = calc.divide(int(a), int(b))
    click.echo(f"{a} / {b} = {r}")
    return r


@click.group()
def cli():
    """ creates command group"""
    pass


# add commands to cli group
cli.add_command(add)
cli.add_command(sub)
cli.add_command(multi)
cli.add_command(divide)
