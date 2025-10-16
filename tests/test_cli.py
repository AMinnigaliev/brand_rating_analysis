from src.brand_rating.main import main


def test_main_cli_success(tmp_path, capsys):
    data = ("name,brand,price,rating\niphone,apple,999,4.9\n"
            "galaxy,samsung,1199,4.8\n")
    p = tmp_path / "data.csv"
    p.write_text(data, encoding="utf-8")

    exit_code = main(["--files", str(p), "--report", "average-rating"])

    # Checking the exit code
    assert exit_code == 0

    # Read the captured stdout and stderr
    captured = capsys.readouterr()

    # Check that stdout contains key data
    assert "Brand" in captured.out
    assert "apple" in captured.out
    assert "Average" in captured.out
    assert captured.err == ""
