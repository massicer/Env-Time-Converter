from env_time_converter.helper import recognized_unit_measure
from env_time_converter.helper.input_regex_parser import parse_input

class ConvertUnitNotRecognizedException(Exception):
    pass

class InputNotInValidFormatException(Exception):
    pass


def get_milliseconds_value_for_input(input_string: str) -> float:
    pass