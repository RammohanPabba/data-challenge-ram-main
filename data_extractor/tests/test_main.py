import pytest

from data_extractor.main import main


class TestMain:
    def test_main(self, capsys):
        main()

        captured = capsys.readouterr()
        expected_output = (
            "Running pipeline 🚀\n"  # Adjust this based on your expected output
        )
        assert captured.out == expected_output
