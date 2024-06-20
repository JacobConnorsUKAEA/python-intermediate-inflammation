"""Tests for compute_data.py"""

import numpy.testing as npt
from pathlib import Path

def test_analyse_data():
    from inflammation.compute_data import analyse_data
    path = Path.cwd() / "../data"
    result = analyse_data(path)
    expected_output = 0
    npt.assert_almost_equal(result,expected_output)
    # TODO: add assert statement(s) to test the result value is as expected