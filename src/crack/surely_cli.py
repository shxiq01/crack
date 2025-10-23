"""CLI entry point for Surely license generation."""

import base64
import sys

import click

from crack.surely.surely import md5


@click.group()
def surely() -> None:
    """Surely license generation tools."""
    pass


@surely.command()
@click.option('--domain', default='_', help='Domain for the license')
def generate(domain: str) -> None:
    """Generate Surely license.
    
    Args:
        domain: The domain for the license (default: '_')
    """
    try:
        key = base64.b64encode(
            f"ORDER:00001,EXPIRY=33227712000000,DOMAIN={domain},ULTIMATE=1,KEYVERSION=1".encode()
        )
        sign = md5(key)
        license_key = f"{sign}{key.decode()}"
        click.echo(f"License Key: {license_key}")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


def main() -> None:
    """Main entry point for Surely CLI."""
    surely()


if __name__ == '__main__':
    main()

