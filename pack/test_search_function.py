"""Tests for the work search function defined in the main.py file in the pack directory."""

import unittest
from unittest.mock import patch
from .main import work_search


class TestSearchParser(unittest.TestCase):
    """Test for the work_search function using unittest to test instantiated data samples from OpenAlex"""

    maxDiff = None  # Disable the maximum difference limit

    @patch("builtins.print")  # decorator to print the tests
    def test_work_search_valid_input(self, mock_print):
        # Test the function with a valid input
        work_search("advances in electrochemical energy storage", 35)

        # Test that prints were called with expected arguements
        test_result = (
            "# of Papers = 5\n"
            "\nWork Titles                                                                                                   URL                                     Citations \n"
            "Research Highlights                                                                                           https://openalex.org/W4235470089               158\n"
            "Brown Adipose Tissue                                                                                          https://openalex.org/W2127690282               104\n"
            "Photobiomodulation in Light of Our Biological Clock's Inner Workings                                          https://openalex.org/W2794980609                 6\n"
            "VNUT Is a Therapeutic Target for Type 2 Diabetes and NASH                                                     https://openalex.org/W3146362911                 3\n"
            "References                                                                                                    https://openalex.org/W4210982835                 1"
        )

        # Get all printed lines of the actaul output and check with test
        result = "\n".join([lines[0][0] for lines in mock_print.call_args_list])
        self.assertEqual(result, test_result)

    def test_work_search_invalid_id(self):
        # Test the funciton with invalid input id
        result = work_search("LCA", 100)
        self.assertEqual(result, "Invalid ID")

    def test_work_search_limited_works(self):
        # Test the funciton with limited works returned
        result = work_search("advances in electrochemical energy storage", 35)
        self.assertEqual(result, "Insufficient Works")


if __name__ == "__main__":
    unittest.main()
