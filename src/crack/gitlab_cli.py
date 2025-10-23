"""CLI entry point for GitLab license generation."""

import sys

import click

from crack.gitlab.gitlab import GitlabKeyGen


@click.group()
def gitlab() -> None:
    """GitLab license generation tools."""
    pass


@gitlab.command()
def generate() -> None:
    """Generate GitLab license."""
    try:
        keygen = GitlabKeyGen()
        keygen.run()
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


def main() -> None:
    """Main entry point for GitLab CLI."""
    gitlab()


if __name__ == '__main__':
    main()

