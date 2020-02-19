import pytest

from env_time_converter.service.convert_service import (
    ConvertUnitNotRecognizedException,
    InputNotInValidFormatException,
    get_milliseconds_value_for_input
)


def test_convert_value_without_unit_measure_succeeded():
    result = get_milliseconds_value_for_input('90')
    assert result == 90.0


def test_input_string_not_valid_error():
    with pytest.raises(InputNotInValidFormatException):
        get_milliseconds_value_for_input('randomstring')


def test_measure_unit_string_not_valid_error():
    with pytest.raises(ConvertUnitNotRecognizedException):
        get_milliseconds_value_for_input('90 not_valid')


@pytest.mark.parametrize('unit_measure', ['ms', 'milliseconds', 'm'])
def test_convertion_from_milliseconds_unit_measure(unit_measure):
    value = 90
    input_string = f'{value} {unit_measure}'
    result = get_milliseconds_value_for_input(input_string)
    assert result == value


@pytest.mark.parametrize('unit_measure', ['s', 'seconds', 'sec'])
def test_convertion_from_seconds_unit_measure(unit_measure):
    value = 90
    input_string = f'{value} {unit_measure}'
    result = get_milliseconds_value_for_input(input_string)
    assert result == value * 1000
