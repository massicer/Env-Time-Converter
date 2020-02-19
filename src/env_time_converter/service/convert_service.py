from env_time_converter.helper import recognized_unit_measure
from env_time_converter.helper.input_regex_parser import parse_input


class ConvertUnitNotRecognizedException(Exception):
    pass


class InputNotInValidFormatException(Exception):
    pass


def get_milliseconds_value_for_input(input_string: str) -> float:

    matches = parse_input(input=input_string)

    if len(matches) == 0:
        raise InputNotInValidFormatException('the input is not recognized')

    number_value = None
    try:
        number_value = float(matches[0])
    except ValueError:
        raise InputNotInValidFormatException('the value is not a valid float')

    convert_value = 0

    if matches[1] in recognized_unit_measure.milliseconds_allowed_strings():
        convert_value = 1
    elif matches[1] in recognized_unit_measure.seconds_allowed_strings():
        convert_value = 1000
    elif matches[1] in recognized_unit_measure.minutes_allowed_strings():
        convert_value = 1000 * 60
    elif matches[1] in recognized_unit_measure.hours_allowed_strings():
        convert_value = 1000 * 60 * 60
    elif matches[1] in recognized_unit_measure.days_allowed_strings():
        convert_value = 1000 * 60 * 60 * 24
    elif matches[1] in recognized_unit_measure.days_allowed_strings():
        convert_value = 1000 * 60 * 60 * 24 * 365
    else:
        raise ConvertUnitNotRecognizedException(
            f'no unit conversion value found for unit {matches[1]}'
        )

    return number_value * convert_value
