"""
CLI application for tltr.

This script provides a dice roller functionality using Click.
"""

import json
import random
import click

@click.group()
def tltr():
    """That's Like... Totally Random!"""
    pass

@tltr.command()
@click.option(
    '--file', '-f', 
    multiple=True,
    required=True,
    type=click.Path(exists=True, readable=True, path_type=str),
    help="Input JSON file(s) containing a JSON string array."
)
def roll(file):
    """Roll dice by randomly selecting items from the provided JSON files."""
    results = []

    for filepath in file:
        try:
            with open(filepath, 'r', encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    click.echo(f"Error: {filepath} does not contain a JSON array.")
                    return
                if not data:
                    click.echo(f"Error: {filepath} is empty.")
                    return
                chosen_item = random.choice(data)
                results.append(chosen_item)
        except json.JSONDecodeError:
            click.echo(f"Error: {filepath} is not a valid JSON file.")
            return

    # Print results
    click.echo("That's Like... Totally Random!")
    for i, result in enumerate(results, start=1):
        click.echo(f"- [chosen item {i}] {result}")

if __name__ == "__main__":
    tltr()
