import click

from greetings import greeting


@click.command()
@click.option("--name", default="world", show_default=True, help="Name to greet.")
def main(name: str) -> None:
    """Print a greeting."""
    click.echo(greeting(name))
