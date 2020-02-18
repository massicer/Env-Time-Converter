import re

REGEX = "/^(-?(?:\d+)?\.?\d+)\
     *(milliseconds?|msecs?|ms|seconds?|secs?|s|\
        minutes?|mins?|m|hours?|hrs?|h|days?|d|weeks?|w|years?|yrs?|y)?$/i"


def parse_input(input: str):
    m = re.match(REGEX, input)
    return m.groups()
