"""CLI entry point for Typora license generation."""

import sys

import click

from crack.typora.typora import TyporaKeyGen


@click.group()
def typora() -> None:
    """Typora license generation tools."""
    pass


@typora.command()
def generate() -> None:
    """Generate Typora license."""
    try:
        keygen = TyporaKeyGen()
        keygen.run()
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


def main() -> None:
    """Main entry point for Typora CLI."""
    typora()


if __name__ == '__main__':
    main()

