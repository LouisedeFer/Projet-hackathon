# ruff: noqa: D100,S311,E501

from .cmd_line import read_args
from .taquin import start_play, start_auto


def main() -> None:
    """Read arguments and start the simulation."""
    # Read command line arguments
    args = read_args()

    # Start automata
    if args.play:
        start_play()
    else:
        start_auto()
