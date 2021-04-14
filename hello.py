#!/usr/bin/env python

"""This is a test"""

import click

# import glob

from mylib.myadd import add


@click.command()
@click.option("--value1", help="The first number to add")
@click.option("--value2", help="The second number to add")
def calculate(value1, value2):
    """This adds two numbers: --value1 and --value2"""
    result = add(value1, value2)

    click.echo(click.style(f"Adding numbers: {value1}, {value2}", bg="black", fg="red"))
    click.echo(click.style(f"Result: {result}", fg="blue"))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    calculate()
