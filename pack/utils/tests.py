"""Test for all files in the utils directory."""

from .fields import FieldInfo
from .siblings import SibInfo


def test_field_info():
    """Test that the fields summary is correct."""
    field_ids = [
        "27",
        "33",
        "22",
        "12",
        "17",
        "13",
        "11",
        "23",
        "31",
        "14",
        "25",
        "20",
        "36",
        "32",
        "16",
        "19",
        "28",
        "26",
        "24",
        "18",
        "21",
        "29",
        "30",
        "35",
        "15",
        "34",
    ]

    field_urls = [
        "https://openalex.org/fields/27",
        "https://openalex.org/fields/33",
        "https://openalex.org/fields/22",
        "https://openalex.org/fields/12",
        "https://openalex.org/fields/17",
        "https://openalex.org/fields/13",
        "https://openalex.org/fields/11",
        "https://openalex.org/fields/23",
        "https://openalex.org/fields/31",
        "https://openalex.org/fields/14",
        "https://openalex.org/fields/25",
        "https://openalex.org/fields/20",
        "https://openalex.org/fields/36",
        "https://openalex.org/fields/32",
        "https://openalex.org/fields/16",
        "https://openalex.org/fields/19",
        "https://openalex.org/fields/28",
        "https://openalex.org/fields/26",
        "https://openalex.org/fields/24",
        "https://openalex.org/fields/18",
        "https://openalex.org/fields/21",
        "https://openalex.org/fields/29",
        "https://openalex.org/fields/30",
        "https://openalex.org/fields/35",
        "https://openalex.org/fields/15",
        "https://openalex.org/fields/34",
    ]

    # Test that the len of fields, ids, and urls returned matches the
    # expected count and that the elements are unique.
    assert len(FieldInfo().fields) == len(set(FieldInfo().fields))
    assert field_ids == FieldInfo().field_id
    assert field_urls == FieldInfo().field_url
    assert len(FieldInfo().fields) == 26
    assert len(FieldInfo().field_url) == 26
    assert len(FieldInfo().field_id) == 26


def test_siblings_info():
    """Test that the siblings summary is correct."""
    # Define a test case using data for field id = 34
    sib_ids_34 = ["35", "36", "27", "29"]
    sib_fields_34 = ["Dentistry", "Health Professions", "Medicine", "Nursing"]
    sib_urls_34 = [
        "https://openalex.org/fields/35",
        "https://openalex.org/fields/36",
        "https://openalex.org/fields/27",
        "https://openalex.org/fields/29",
    ]

    assert sib_ids_34 == SibInfo(34).field_id
    assert sib_fields_34 == SibInfo(34).fields
    assert sib_urls_34 == SibInfo(34).field_url
