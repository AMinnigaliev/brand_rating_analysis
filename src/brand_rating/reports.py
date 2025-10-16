from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any


@dataclass
class ReportResult:
    headers: list[str]
    rows: list[tuple[Any, ...]]


Report = Callable[[list[dict[str, str]]], ReportResult]
_REPORTS: dict[str, Report] = {}


def register_report(name: str):
    def decorator(fn):
        _REPORTS[name] = fn
        return fn

    return decorator


def get_report(name: str) -> Report:
    try:
        return _REPORTS[name]
    except KeyError as e:
        raise KeyError(
            f"Report '{name}' not found. Available: {', '.join(
                sorted(_REPORTS)
            )}"
        ) from e


def available_reports() -> list[str]:
    return sorted(_REPORTS.keys())


@register_report("average-rating")
def average_rating(rows: list[dict[str, str]]) -> ReportResult:
    """
    Given input rows (each row is a dictionary with the fields name, brand,
    price, rating), it returns a list of tuples (brand, average_rating),
    sorted in descending order of rating.
    """
    sums = defaultdict(float)
    counts = defaultdict(int)

    for r in rows:
        brand = r.get("brand")
        if brand is None or brand == "":
            continue

        rating_raw = r.get("rating")
        if rating_raw is None or rating_raw == "":
            continue

        try:
            rating = float(rating_raw)
        except ValueError:
            continue

        sums[brand] += rating
        counts[brand] += 1

    rows = []
    for brand, total in sums.items():
        cnt = counts[brand]
        if cnt == 0:
            continue
        avg = round(total / cnt, 2)
        rows.append((brand, avg))

    # sort by: first by descending average rating, then by brand name
    rows.sort(key=lambda x: (-x[1], x[0].lower()))
    headers = ["Brand", "Average rating"]

    return ReportResult(headers=headers, rows=rows)
