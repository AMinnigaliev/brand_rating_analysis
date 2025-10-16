import io

from src.brand_rating.io import read_rows_from_file_obj


def test_read_rows_from_file_obj():
    csv_text = "name,brand,price,rating\niphone 15 pro,apple,999,4.9\n"
    f = io.StringIO(csv_text)

    rows = list(read_rows_from_file_obj(f))
    assert len(rows) == 1
    assert rows[0]["name"] == "iphone 15 pro"
    assert rows[0]["brand"] == "apple"
    assert rows[0]["rating"] == "4.9"
