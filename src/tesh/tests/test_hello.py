"""Tests for the hello function."""
from tesh import hello


def test_hello() -> None:
    """Test the hello function."""
    assert hello() is None