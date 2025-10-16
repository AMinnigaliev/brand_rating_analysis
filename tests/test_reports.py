from src.brand_rating.reports import average_rating


def _rows_from_list(items):
    """
    items: list of tuples (name, brand, price, rating)
    returns list of dicts like csv.DictReader would produce.
    """
    rows = []
    for name, brand, price, rating in items:
        rows.append({
            "name": name,
            "brand": brand,
            "price": str(price),
            "rating": str(rating)
        })
    return rows


def test_average_rating():
    items = [
        ("a1", "brandA", 999, 4.9),
        ("a2", "brandA", 1000, 5.0),
        ("g1", "brandB", 1199, 1.0),
    ]
    rows = _rows_from_list(items)
    res = average_rating(rows)

    assert res.headers == ["Brand", "Average rating"]

    assert len(res.rows) == 2
    assert res.rows[0][0] == "brandA"
    assert res.rows[0][1] == 4.95
    assert res.rows[-1][0] == "brandB"
