"""CLI entry point for FinalShell license generation."""

import sys

import click

from crack.finalshell.finalshell import md5, keccak384


@click.group()
def finalshell() -> None:
    """FinalShell license generation tools."""
    pass


@finalshell.command()
@click.argument('machine_code')
def generate(machine_code: str) -> None:
    """Generate FinalShell license from machine code.
    
    Args:
        machine_code: The machine code for FinalShell
    """
    try:
        click.echo("版本号 < 3.9.6 (旧版)")
        click.echo(f"高级版: {md5(f'61305{machine_code}8552'.encode())[8:24]}")
        click.echo(f"专业版: {md5(f'2356{machine_code}13593'.encode())[8:24]}")
        
        click.echo("版本号 >= 3.9.6 (新版)")
        click.echo(f"高级版: {keccak384(f'{machine_code}hSf(78cvVlS5E'.encode())[12:28]}")
        click.echo(f"专业版: {keccak384(f'{machine_code}FF3Go(*Xvbb5s2'.encode())[12:28]}")
        
        click.echo("版本号 (4.5)")
        click.echo(f"高级版: {keccak384(f'{machine_code}wcegS3gzA$'.encode())[12:28]}")
        click.echo(f"专业版: {keccak384(f'{machine_code}b(xxkHn%z);x'.encode())[12:28]}")
        
        click.echo("版本号 (4.6)")
        click.echo(f"高级版: {keccak384(f'{machine_code}csSf5*xlkgYSX,y'.encode())[12:28]}")
        click.echo(f"专业版: {keccak384(f'{machine_code}Scfg*ZkvJZc,s,Y'.encode())[12:28]}")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


def main() -> None:
    """Main entry point for FinalShell CLI."""
    finalshell()


if __name__ == '__main__':
    main()

