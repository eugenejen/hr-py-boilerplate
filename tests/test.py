"""
test runner
"""
from hr_problem.main import main


def test_main():
    """ test """
    input_data = ''
    output_data = main(input_data)
    expected_data = ''
    assert expected_data == output_data
