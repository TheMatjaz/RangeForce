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


def limited(value, min, max, name='Value', dtype=None):
    _validate_interval(min, max)
    _validate_type(name, value, dtype)
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


def _validate_type(name, value, dtype):
    if dtype is not None and not isinstance(value, dtype):
        raise TypeError(
            '{:} must be of type {:}. '
            '{:} found instead.'.format(name, dtype.__name__,
                                        type(value).__name__)
        )


def limited_int(value, min, max, name='Value'):
    return limited(value, min, max, name, dtype=int)


def limited_float(value, min, max, name='Value'):
    return limited(value, min, max, name, dtype=float)


def negative_int(value, name='Value'):
    return limited(value, None, -1, name, dtype=int)


def nonpositive_int(value, name='Value'):
    return limited(value, None, 0, name, dtype=int)


def positive_int(value, name='Value'):
    return limited(value, 1, None, name, dtype=int)


def nonnegative_int(value, name='Value'):
    return limited(value, 0, None, name, dtype=int)


def uint8(value, name='Value'):
    return limited(value, 0, 0xFF, name, dtype=int)


def uint16(value, name='Value'):
    return limited(value, 0, 0xFFFF, name, dtype=int)


def uint32(value, name='Value'):
    return limited(value, 0, 0xFFFFFFFF, name, dtype=int)


def uint64(value, name='Value'):
    return limited(value, 0, 0xFFFFFFFFFFFFFFFF, name, dtype=int)


def uint_bits(value, bits, name='Value'):
    return limited(value, 0, (1 << bits) - 1, name, dtype=int)


def int8(value, name='Value'):
    return limited(value, -0x80, 0x7F, name, dtype=int)


def int16(value, name='Value'):
    return limited(value, -0x8000, 0x7FFF, name, dtype=int)


def int32(value, name='Value'):
    return limited(value, -0x80000000, 0x7FFFFFFF, name, dtype=int)


def int64(value, name='Value'):
    return limited(value, -0x8000000000000000, 0x7FFFFFFFFFFFFFFF, name,
                   dtype=int)


def limited_len(sized, min, max, name='value'):
    length = len(sized)
    _validate_non_negative_interval_extremes(min, max)
    limited(length, min, max, name='Length of '+name)
    return sized


def _validate_non_negative_interval_extremes(min, max):
    if min is not None and min < 0:
        raise ValueError(
            'Length lower bound must be non-negative. ' \
            '{:} found instead.'.format(min)
        )
    if max is not None and max < 0:
        raise ValueError(
            'Length upper bound must be non-negative. ' \
            '{:} found instead.'.format(max)
        )

def exact_len(sized, expected, name='value'):
    length = len(sized)
    if expected is None or expected < 0:
        expected = 0
    if length != expected:
        raise RangeError(
            'Length of {:} must be {:}{:}. '
            '{:} found instead.'.format(
                name, expected, unit or ' ' + unit, length)
        )
