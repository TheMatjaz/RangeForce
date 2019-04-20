#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def clip(value, min, max):
    if value < min:
        return min
    elif value > max:
        return max
    else:
        return value


def limited_int(value, min, max, name='Value'):
    if min > max:
        min, max = max, min
    if not isinstance(value, int):
        raise TypeError(
            '{:} must be an integer. '
            '{:} found instead.'.format(name, type(value))
        )
    elif min is None and max is not None and value > max:
        raise ValueError(
            '{:} must be in range ]-inf, {:}]. '
            '{:} found instead.'.format(name, max, value)
        )
    elif max is None and min is not None and value < min:
        raise ValueError(
            '{:} must be in range [{:}, +inf[. '
            '{:} found instead.'.format(name, min, value)
        )
    elif min is not None and max is not None and value < min or value > max:
        raise ValueError(
            '{:} must be in range [{:}, {:}]. '
            '{:} found instead.'.format(name, min, max, value)
        )
    else:
        return value


def negative_int(value, name='Value'):
    return limited_int(value, None, -1, name)


def nonpositive_int(value, name='Value'):
    return limited_int(value, None, 0, name)


def positive_int(value, name='Value'):
    return limited_int(value, 1, None, name)


def nonnegative_int(value, name='Value'):
    return limited_int(value, 0, None, name)


def uint8(value, name='Value'):
    return limited_int(value, 0, 0xFF, name)


def uint16(value, name='Value'):
    return limited_int(value, 0, 0xFFFF, name)


def uint32(value, name='Value'):
    return limited_int(value, 0, 0xFFFFFFFF, name)


def uint64(value, name='Value'):
    return limited_int(value, 0, 0xFFFFFFFFFFFFFFFF, name)


def int8(value, name='Value'):
    return limited_int(value, -0x80, 0x7F, name)


def int16(value, name='Value'):
    return limited_int(value, -0x8000, 0x7FFF, name)


def int32(value, name='Value'):
    return limited_int(value, -0x80000000, 0x7FFFFFFF, name)


def int64(value, name='Value'):
    return limited_int(value, -0x8000000000000000, 0x7FFFFFFFFFFFFFFF, name)


def limited_len(sized, min, max, name='Value', unit=''):
    length = len(sized)
    if min is None or min < 0:
        min = 0
    if max is not None:
        if max < 0:
            max = 0
        if length > max:
            raise ValueError(
                'Length of {:} must be in range [{:}, {:}]{:}. '
                '{:} found instead.'.format(
                    name, min, max, unit or '' + unit, length)
            )
    else:
        return sized


def exact_len(sized, expected, name='Value', unit=''):
    length = len(sized)
    if expected is None or expected < 0:
        expected = 0
    if length != expected:
        raise ValueError(
            'Length of {:} must be {:}{:}. '
            '{:} found instead.'.format(
                name, expected, unit or ' ' + unit, length)
        )
