"""Input/Output module."""

from pathlib import Path


def load_content(path: Path) -> str:
    """
    Load content from file.

    Args:
        path: file path

    Returns:
        str
    """
    with open(path) as file:  # NOQA: WPS110
        return file.read()


def get_extension(path: Path) -> str:
    """
    Return file extension.

    Args:
        path: file path

    Returns:
        str
    """
    if isinstance(path, str):
        path = Path(path)
    return path.name.split('.')[-1]
