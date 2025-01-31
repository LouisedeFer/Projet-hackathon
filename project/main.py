# ruff: noqa: D100,S311,E501

from .cmd_line import read_args
from .taquin import Taquin


def main() -> None:
    """Read arguments and start the simulation."""
    # Read command line arguments
    args = read_args()

    # Start automata
    Taquin(play_mode=args.gui).start()
