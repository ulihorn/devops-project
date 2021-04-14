#!/usr/bin/env python

"""This is a test"""

import click

# import glob

from mylib.myadd import add




@click.command()
@click.option("--value1", default=1, help="The first number to add")
@click.option("--value2", default=1, help="The second number to add")
@click.argument("name")
def calculate(value1, value2, name):
    """This adds two numbers: --value1 and --value2"""
    result = add(value1, value2)

    click.echo(click.style(f"Adding numbers: {value1}, {value2}", bg="black", fg="red"))
    click.echo(click.style(f"Result: {result}", fg="blue"))
    click.echo(click.style(f"Name: {name}", bg="black", fg="green"))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    calculate()
