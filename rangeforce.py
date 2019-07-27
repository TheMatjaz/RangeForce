#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright © 2019, Matjaž Guštin <dev@matjaz.it> <https://matjaz.it>.
# Released under the BSD 3-Clause License

__VERSION__ = 'v1.0.0'

import math


class RangeError(Exception):
    pass


def clip(value, min, max):
    if value < min:
        return min
    elif value > max:
        return max
    else:
        return value


def limited(value, min, max, name='Value'):
    _validate_interval(min, max)
    if min is None and max is not None and (value > max or math.isnan(value)):
        raise RangeError(
            '{:} must be in range ]-inf, {:}]. '
            '{:} found instead.'.format(name, max, value)
        )
    elif max is None and min is not None and (
            value < min or math.isnan(value)):
        raise RangeError(
            '{:} must be in range [{:}, +inf[. '
            '{:} found instead.'.format(name, min, value)
        )
    elif min is not None and max is not None and (
            value < min or value > max or math.isnan(value)):
        raise RangeError(
            '{:} must be in range [{:}, {:}]. '
            '{:} found instead.'.format(name, min, max, value)
        )
    else:
        return value


def _validate_interval(min, max):
    if min is None and max is None:
        raise ValueError(
            '[min, max] interval must be closed on at least one extreme.')
    elif min is not None and math.isnan(min):
        raise ValueError('NaN is not a valid interval lower bound.')
    elif max is not None and math.isnan(max):
        raise ValueError('NaN is not a valid interval upper bound.')
    elif min is not None and max is not None and min > max:
        raise ValueError(
            'Interval extremes [{:}, {:}] not in order.'.format(min, max))


def limited_int(value, min, max, name='Value'):
    if not isinstance(value, int):
        raise TypeError(
            '{:} must be an integer. '
            '{:} found instead.'.format(name, type(value))
        )
    else:
        return limited(value, min, max, name)


def limited_float(value, min, max, name='Value'):
    if not isinstance(value, float):
        raise TypeError(
            '{:} must be a float. '
            '{:} found instead.'.format(name, type(value))
        )
    else:
        return limited(value, min, max, name)


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


def uint_bits(value, bits, name='Value'):
    return limited_int(value, 0, (1 << bits) - 1, name)


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
        if length < min or length > max:
            raise RangeError(
                'Length of {:} must be in range [{:}, {:}]{:}. '
                '{:} found instead.'.format(
                    name, min, max, unit or ' ' + unit, length)
            )
    else:
        return sized


def exact_len(sized, expected, name='Value', unit=''):
    length = len(sized)
    if expected is None or expected < 0:
        expected = 0
    if length != expected:
        raise RangeError(
            'Length of {:} must be {:}{:}. '
            '{:} found instead.'.format(
                name, expected, unit or ' ' + unit, length)
        )
