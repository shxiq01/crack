"""CLI entry point for DBeaver license generation."""

import sys
from typing import Optional

import click

from crack.dbeaver.dbeaver import DBeaverKeyGen


@click.group()
def dbeaver() -> None:
    """DBeaver license generation tools."""
    pass


@dbeaver.command()
@click.option('--no-patch', is_flag=True, help='Skip patch generation')
def generate(no_patch: bool) -> None:
    """Generate DBeaver license."""
    try:
        keygen = DBeaverKeyGen()
        keygen.run(patch=not no_patch)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


def main() -> None:
    """Main entry point for DBeaver CLI."""
    dbeaver()


if __name__ == '__main__':
    main()

