#!/usr/bin/env python3
import sys

import click

sys.path.insert(0, str(__file__).rsplit("/", 2)[0])

from optimizer.evaluator import evaluate


@click.command()
@click.argument("path")
def main(path: str) -> None:
    """Evaluate duplicate code clusters found by dryer at PATH."""
    result = evaluate(path)
    if result.num_clusters == 0:
        click.echo("No clusters found.")
    else:
        score = result.num_yes / result.num_clusters
        click.echo(f"Score: {result.num_yes}/{result.num_clusters} = {score:.3f}")
        if result.suggestion:
            click.echo(f"Suggestion: {result.suggestion}")


if __name__ == "__main__":
    main()
