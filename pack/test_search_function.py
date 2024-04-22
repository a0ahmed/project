"""Tests for the work search function module."""

import unittest
from unittest.mock import patch
from .main import work_search


class TestSearchParser(unittest.TestCase):
    """Unit test for the work_search function."""

    maxDiff = None  # Disable the maximum difference limit

    @patch("builtins.print")  # decorator to print the tests
    def test_work_search_valid_input(self, mock_print):
        """Test the function with a valid input."""
        work_search("advances in electrochemical energy storage", 35)

        # Get all printed lines of the actual output and check with test
        lines = "\n".join([lines[0][0] for lines in mock_print.call_args_list])

        # Regular expression string matching structue of the output
        structure = (
            r"# of Papers = \d+\n\n"
            r"{'Work Titles':110s}{'URL':40s}{'Citations':10s}\n"
            r"{\w+:110s}{\w+:40s}{\d+:10d}\n"
        )

        self.assertTrue(lines, structure)

    def test_work_search_invalid_id(self):
        """Test the funciton with invalid input id."""
        result = work_search("LCA", 100)
        self.assertEqual(result, "Invalid ID")

    def test_work_search_limited_works(self):
        """Test the funciton with limited works returned."""
        result = work_search("advances in electrochemical energy storage", 35)
        self.assertEqual(result, "Insufficient Works")


if __name__ == "__main__":
    unittest.main()
