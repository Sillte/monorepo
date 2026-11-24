import click

from greetings import greeting


@click.group()
def main() -> None:
    """Commands for the hello app."""


@main.command()
@click.option("--name", default="uv workspace", show_default=True, help="Name to greet.")
def greet(name: str) -> None:
    """Print a greeting using the greetings workspace package."""
    click.echo(greeting(name))
