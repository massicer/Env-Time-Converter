from env_time_converter.helper.input_regex_parser import (
    parse_input,
    REGEX
)


def test_assert_regex_not_none():
    assert REGEX is not None


def assert_callable_parse_input():
    assert callable(parse_input)
