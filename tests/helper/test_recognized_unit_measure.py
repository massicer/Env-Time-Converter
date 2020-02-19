import pytest

from env_time_converter.helper import recognized_unit_measure


@pytest.mark.parametrize('unit', [
    's', 'seconds', 'sec'
])
def test_seconds_unit(unit):
    assert unit in recognized_unit_measure.seconds_allowed_strings()


@pytest.mark.parametrize('unit', [
    'ms', 'milliseconds', 'm'
])
def test_milliseconds_unit(unit):
    assert unit in recognized_unit_measure.milliseconds_allowed_strings()


@pytest.mark.parametrize('unit', [
    'h', 'hours', 'hrs', 'hour'
])
def test_hour_unit(unit):
    assert unit in recognized_unit_measure.hours_allowed_strings()


@pytest.mark.parametrize('unit', [
    'd', 'days', 'day'
])
def test_days_unit(unit):
    assert unit in recognized_unit_measure.days_allowed_strings()


@pytest.mark.parametrize('unit', [
    'y', 'years', 'yrs', 'year'
])
def test_years_unit(unit):
    assert unit in recognized_unit_measure.years_allowed_strings()


@pytest.mark.parametrize('unit', [
    'min', 'minute', 'minutes'
])
def test_minutes_unit(unit):
    assert unit in recognized_unit_measure.minutes_allowed_strings()
