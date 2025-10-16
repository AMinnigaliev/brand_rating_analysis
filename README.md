# Brand rating analysis
The script reads files with product rating data and generates reports.

In short: the script reads CSV files with products (header format: `name,brand,price,rating`) and generates reports on all transferred files.

### Quick Start

1. Clone the repository.
2. It is recommended to use a virtual environment:
    ```bash
    python -m venv .venv
    ```
    macOS / Linux
    ```bash
    source .venv/bin/activate
    ```
    Windows (cmd)
    ```bash
    .venv\Scripts\activate
    ```
3. Install development dependencies:
    ```bash
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    ```
4. Running the script:
    ```bash
    python -m  src.brand_rating_analysis.main --files data1.csv data2.csv --report average-rating
   ```
5. Example output:
    ```bash
   +----+---------+------------------+
   |    | Brand   |   Average rating |
   |----+---------+------------------|
   |  1 | apple   |             4.55 |
   |  2 | samsung |             4.53 |
   |  3 | xiaomi  |             4.37 |
   +----+---------+------------------+
    ```

### How to add a new report

In `src/brand_rating_analysis/reports.py` add a new function and decorate it with `@register_report("new_report_name")`.

The function should accept rows: `list[dict[str, str]]` and return an instance of the `ReportResult` data class.

### Tests

1. Run all tests
    ```bash
    pytest
    ```
2. Run one test from a file
    ```bash
    pytest tests/test_cli.py::test_main_cli_success
    ```

3. With coverage report
    ```bash
    pytest --cov=src --cov-report=term-missing
    ```
