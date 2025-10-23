"""CLI entry point for Atlassian license generation."""

import sys

import click

from crack.atlassian.atlassian import generate as atlassian_generate


@click.group()
def atlassian() -> None:
    """Atlassian license generation tools."""
    pass


@atlassian.command()
def generate() -> None:
    """Generate Atlassian license."""
    try:
        atlassian_generate()
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


def main() -> None:
    """Main entry point for Atlassian CLI."""
    atlassian()


if __name__ == '__main__':
    main()

