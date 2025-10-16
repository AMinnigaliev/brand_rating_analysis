import csv
from collections.abc import Iterable
from typing import TextIO


def read_rows_from_file_obj(f: TextIO) -> Iterable[dict[str, str]]:
    """
    Reads CSV from a file-like object and returns a dictionary generator
    (keys from header).
    """
    reader = csv.DictReader(f)
    for row in reader:
        yield row


def read_rows_from_paths(paths: Iterable[str]) -> list[dict[str, str]]:
    """
    Reads all lines from a list of files and returns a list of dictionaries.
    """
    rows = []
    for p in paths:
        with open(p, newline="", encoding="utf-8") as f:
            rows.extend(read_rows_from_file_obj(f))

    return rows
