#!/usr/bin/env python3
import sys
from argparse import ArgumentParser

from tabulate import tabulate

from src.brand_rating.io import read_rows_from_paths
from src.brand_rating.reports import (ReportResult, available_reports,
                                      get_report)


def build_parser() -> ArgumentParser:
    p = ArgumentParser(
        prog="brand-rating",
        description="Generates reports based on CSV files with products."
    )
    p.add_argument(
        "--files", "-f", nargs="+", required=True,
        help="Paths to CSV files (supports multiple transfers)."
    )

    reports = available_reports()

    p.add_argument(
        "--report", "-r", required=True, choices=reports if reports else None,
        help="Report Title. Available: " + (
            ", ".join(reports) if reports else "none"
        )
    )
    return p


def render_report(result: ReportResult) -> str:
    table = []
    for row in result.rows:
        display = []
        for cell in row:
            if isinstance(cell, (list, tuple, set)):
                display.append(", ".join(map(str, cell)))

            elif cell is None:
                display.append("")

            else:
                display.append(str(cell))

        table.append(display)

    index_seq = range(1, len(table) + 1)

    return tabulate(
        table, headers=result.headers, tablefmt="psql", showindex=index_seq
    )


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        rows = read_rows_from_paths(args.files)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2

    try:
        report_fn = get_report(args.report)
    except KeyError as e:
        print(e, file=sys.stderr)
        return 3

    report_data = report_fn(rows)

    out = render_report(report_data)
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
