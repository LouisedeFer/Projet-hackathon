# ruff: noqa: D100,S311,E501

import argparse

def read_args() -> argparse.Namespace:
    """Read command line arguments."""
    # Parser and its description
    parser = argparse.ArgumentParser(description="Taquin game.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # Play mode
    parser.add_argument("--play", "-p", action="store_true", help="Enable play mode.")

    # Parse
    args = parser.parse_args()

    return args  # noqa: RET504
