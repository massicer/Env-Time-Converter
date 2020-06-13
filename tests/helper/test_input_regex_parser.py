import pytest

from pytime_converter.helper.input_regex_parser import (
    parse_input,
    REGEX
)


def test_assert_regex_not_none():
    assert REGEX is not None


def assert_callable_parse_input():
    assert callable(parse_input)


@pytest.mark.parametrize('input, first_group, second_group', [
    pytest.param('89', '89', None, id='no misure unit'),
    pytest.param('89 ms', '89', 'ms', id='with misure unit'),
    pytest.param('-89 ms', '-89', 'ms', id='unit and negative value'),
    pytest.param('-89.90', '-89.90', 'ms', id='unit and negative dec value'),
    pytest.param('-89.90  ms', '-89.90', 'ms', id='multiple spaces value'),
])
def test_parse_values(input, first_group, second_group):
    result = parse_input(input=input)
    assert result is not None

    assert result[0] == first_group
    if result[1] is not None and result[1] != '':
        assert result[1] == second_group
