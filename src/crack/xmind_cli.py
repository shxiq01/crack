"""CLI entry point for XMind license generation."""

import sys

import click

from crack.xmind.xmind import XmindKeyGen


@click.group()
def xmind() -> None:
    """XMind license generation tools."""
    pass


@xmind.command()
def generate() -> None:
    """Generate XMind license."""
    try:
        keygen = XmindKeyGen()
        keygen.run()
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


def main() -> None:
    """Main entry point for XMind CLI."""
    xmind()


if __name__ == '__main__':
    main()

