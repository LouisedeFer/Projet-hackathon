# ruff: noqa: D100,S311,E501

import argparse

#Global constants
DEFAULT_HEIGHT=3
MIN_HEIGHT=3
MAX_HEIGHT=6
DEFAULT_WIDTH=3
MIN_WIDTH=3
MAX_WIDTH=6


def read_args() -> argparse.Namespace:
    """Read command line arguments."""
    # Parser and its description
    parser = argparse.ArgumentParser(description="Taquin game.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # Play mode
    parser.add_argument("--play", "-p", action="store_true", help="Enable play mode.")

    parser.add_argument("--height", "-H", type = int, default = DEFAULT_HEIGHT,
                        help="Number of lines of the checkerboard."
                        f" Must be between {MIN_HEIGHT} and {MAX_HEIGHT}.")
    parser.add_argument("--width", "-W", type = int, default = DEFAULT_WIDTH,
                        help="Number of columns of the checkerboard."
                        f" Must be between {MIN_WIDTH} and {MAX_WIDTH}.")
    # Parse
    args = parser.parse_args()

    return args  # noqa: RET504
