"""CLI entry point for JetBrains license generation."""

import sys
from typing import Optional

import click

from crack.jetbrains.jetbrains import JetbrainsKeyGen
from crack.jetbrains.plugins import JetBrainPlugin
from crack.jetbrains.server import app as jetbrains_app


@click.group()
def jetbrains() -> None:
    """JetBrains license generation and server tools."""
    pass


@jetbrains.command()
@click.option('--license-id', help='Custom license ID')
@click.option('--license-name', help='Custom license name')
@click.option('--no-patch', is_flag=True, help='Skip patch generation')
def generate(license_id: Optional[str], license_name: Optional[str], no_patch: bool) -> None:
    """Generate JetBrains license."""
    try:
        keygen = JetbrainsKeyGen()
        keygen.run(patch=not no_patch, license_id=license_id, license_name=license_name)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


@jetbrains.command()
@click.option('--host', default='0.0.0.0', help='Server host')
@click.option('--port', default=5000, help='Server port')
def server(host: str, port: int) -> None:
    """Start JetBrains license server."""
    try:
        import uvicorn
        click.echo(f"Starting JetBrains license server on {host}:{port}")
        uvicorn.run(jetbrains_app, host=host, port=port)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


@jetbrains.command()
def update_plugins() -> None:
    """Update JetBrains plugins database."""
    try:
        click.echo("Updating JetBrains plugins database...")
        plugin_manager = JetBrainPlugin()
        plugin_manager.update().make_licenses()
        click.echo("Plugins database updated successfully!")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


def main() -> None:
    """Main entry point for JetBrains CLI."""
    jetbrains()


if __name__ == '__main__':
    main()

