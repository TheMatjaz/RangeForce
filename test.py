#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# # Copyright © 2019, Matjaž Guštin <dev@matjaz.it> <https://matjaz.it>.
# # Released under the BSD 3-Clause License

import unittest

import rangeforce as rf


class TestClip(unittest.TestCase):
    def test_in_range(self):
        self.assertEqual(2, rf.clip(2, 0, 3))
        self.assertEqual(2, rf.clip(2, 1, 3))
        self.assertEqual(2, rf.clip(2, 2, 3))
        self.assertEqual(2, rf.clip(2, 2, 2))
        self.assertEqual(3, rf.clip(3, 2, 3))
        self.assertEqual(3, rf.clip(3, -22, 3))

    def test_negative_in_range(self):
        self.assertEqual(-3, rf.clip(-3, -20, -1))
        self.assertEqual(-3, rf.clip(-3, -5, -1))
        self.assertEqual(-3, rf.clip(-3, -3, -2))
        self.assertEqual(-3, rf.clip(-3, -3, -3))
        self.assertEqual(-3, rf.clip(-3, -3, 1))

    def test_smaller_than_range(self):
        self.assertEqual(10, rf.clip(5, 10, 20))
        self.assertEqual(10, rf.clip(9, 10, 20))
        self.assertEqual(10, rf.clip(0, 10, 20))
        self.assertEqual(10, rf.clip(-10, 10, 20))
        self.assertEqual(-10, rf.clip(-15, -10, 20))

    def test_larger_than_range(self):
        self.assertEqual(20, rf.clip(30, 10, 20))
        self.assertEqual(20, rf.clip(25, 10, 20))
        self.assertEqual(20, rf.clip(21, -10, 20))
        self.assertEqual(-20, rf.clip(-2, -50, -20))
        self.assertEqual(-20, rf.clip(0, -50, -20))
        self.assertEqual(-20, rf.clip(1, -50, -20))


class TestUnsignedInts(unittest.TestCase):
    def test_uint8(self):
        self.assertRaises(rf.IllegalValueError, rf.uint8, -1)
        self.assertRaises(rf.IllegalValueError, rf.uint8, -20)
        self.assertRaises(rf.IllegalValueError, rf.uint8, 2**8)
        self.assertRaises(rf.IllegalValueError, rf.uint8, 300)
        for i in range(0, 2**8):
            self.assertEqual(i, rf.uint8(i))
            self.assertIs(i, rf.uint8(i))

    def test_uint16(self):
        self.assertRaises(rf.IllegalValueError, rf.uint16, -1)
        self.assertRaises(rf.IllegalValueError, rf.uint16, -20)
        self.assertRaises(rf.IllegalValueError, rf.uint16, 2**16)
        self.assertRaises(rf.IllegalValueError, rf.uint16, 5446345)
        for i in range(0, 2**16):
            self.assertEqual(i, rf.uint16(i))
            self.assertIs(i, rf.uint16(i))

    def test_uint32(self):
        self.assertRaises(rf.IllegalValueError, rf.uint32, -1)
        self.assertRaises(rf.IllegalValueError, rf.uint32, -20)
        self.assertRaises(rf.IllegalValueError, rf.uint32, 2**32)
        self.assertRaises(rf.IllegalValueError, rf.uint32, 45874349824936)
        rf.uint32(0)
        rf.uint32(1)
        rf.uint32(2)
        rf.uint32(0xFFFFFFFE)
        rf.uint32(0xFFFFFFFF)
        for i in range(0, 0xFFFFFFFF, 4000):
            self.assertEqual(i, rf.uint32(i))
            self.assertIs(i, rf.uint32(i))

    def test_uint64(self):
        self.assertRaises(rf.IllegalValueError, rf.uint64, -1)
        self.assertRaises(rf.IllegalValueError, rf.uint64, -20)
        self.assertRaises(rf.IllegalValueError, rf.uint64, 2**64)
        self.assertRaises(rf.IllegalValueError, rf.uint64,
                          345837634922573643925763492312573634)
        rf.uint64(0)
        rf.uint64(1)
        rf.uint64(2)
        rf.uint64(2**64 - 2)
        rf.uint64(2**64 - 1)
        for i in range(0, 0xFFFFFFFFFFFFFFFF, 30000000000000):
            self.assertEqual(i, rf.uint64(i))
            self.assertIs(i, rf.uint64(i))

    def test_uint_bits(self):
        self.assertRaises(rf.IllegalValueError, rf.uint_bits, 8, 3)
        self.assertRaises(rf.IllegalValueError, rf.uint_bits, 8, 2)
        self.assertRaises(rf.IllegalValueError, rf.uint_bits, -1, 2)
        self.assertRaises(rf.IllegalValueError, rf.uint_bits, -8, 2)
        for i in range(0, 8):
            self.assertEqual(i, rf.uint_bits(i, 3))
            self.assertIs(i, rf.uint_bits(i, 3))
        for i in range(0, 16):
            self.assertEqual(i, rf.uint_bits(i, 4))
            self.assertIs(i, rf.uint_bits(i, 4))


class TestSignedInts(unittest.TestCase):
    def test_int8(self):
        self.assertRaises(rf.IllegalValueError, rf.int8, -2**7 - 1)
        self.assertRaises(rf.IllegalValueError, rf.int8, -150)
        self.assertRaises(rf.IllegalValueError, rf.int8, 2**7)
        self.assertRaises(rf.IllegalValueError, rf.int8, 1560)
        for i in range(-128, 127):
            self.assertEqual(i, rf.int8(i))
            self.assertIs(i, rf.int8(i))

    def test_int16(self):
        self.assertRaises(rf.IllegalValueError, rf.int16, -2**15 - 1)
        self.assertRaises(rf.IllegalValueError, rf.int16, -675832495)
        self.assertRaises(rf.IllegalValueError, rf.int16, 2**15)
        self.assertRaises(rf.IllegalValueError, rf.int16, 5446345)
        for i in range(-32768, 32767):
            self.assertEqual(i, rf.int16(i))
            self.assertIs(i, rf.int16(i))

    def test_int32(self):
        self.assertRaises(rf.IllegalValueError, rf.int32, -2**31 - 1)
        self.assertRaises(rf.IllegalValueError, rf.int32, 2**31)
        self.assertRaises(rf.IllegalValueError, rf.int32, 45874349824936)
        rf.int32(-0x8000000)
        rf.int32(-0x8000000 + 1)
        rf.int32(-2)
        rf.int32(-1)
        rf.int32(0)
        rf.int32(1)
        rf.int32(2)
        rf.int32(0x7FFFFFFE)
        rf.int32(0x7FFFFFFF)
        for i in range(-0x8000000, 0x7FFFFFFF, 4000):
            self.assertEqual(i, rf.int32(i))
            self.assertIs(i, rf.int32(i))

    def test_int64(self):
        self.assertRaises(rf.IllegalValueError, rf.int64, -2**64 - 1)
        self.assertRaises(rf.IllegalValueError, rf.int64, 2**64)
        self.assertRaises(rf.IllegalValueError, rf.int64,
                          345837634922573643925763492312573634)
        rf.int64(-0x8000000000000000)
        rf.int64(-0x8000000000000000 + 1)
        rf.int64(-2)
        rf.int64(-1)
        rf.int64(0)
        rf.int64(1)
        rf.int64(2)
        rf.int64(0x7FFFFFFFFFFFFFFE)
        rf.int64(0x7FFFFFFFFFFFFFFF)
        for i in range(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF,
                       30000000000000):
            self.assertEqual(i, rf.int64(i))
            self.assertIs(i, rf.int64(i))


class TestNegativePositiveInt(unittest.TestCase):
    def test_negative_int(self):
        self.assertRaises(rf.IllegalValueError, rf.negative_int, 0)
        self.assertRaises(rf.IllegalValueError, rf.negative_int, 1)
        self.assertRaises(rf.IllegalValueError, rf.negative_int, 100)
        self.assertEqual(-20, rf.negative_int(-20))
        self.assertIs(-20, rf.negative_int(-20))

    def test_nonpositive_int(self):
        self.assertRaises(rf.IllegalValueError, rf.nonpositive_int, 1)
        self.assertRaises(rf.IllegalValueError, rf.nonpositive_int, 100)
        self.assertEqual(-20, rf.nonpositive_int(-20))
        self.assertIs(-20, rf.nonpositive_int(-20))
        self.assertEqual(0, rf.nonpositive_int(0))
        self.assertIs(0, rf.nonpositive_int(0))

    def test_positive_int(self):
        self.assertRaises(rf.IllegalValueError, rf.positive_int, 0)
        self.assertRaises(rf.IllegalValueError, rf.positive_int, -1)
        self.assertRaises(rf.IllegalValueError, rf.positive_int, -100)
        self.assertEqual(20, rf.positive_int(20))
        self.assertIs(20, rf.positive_int(20))

    def test_nonnegative_int(self):
        self.assertRaises(rf.IllegalValueError, rf.nonnegative_int, -1)
        self.assertRaises(rf.IllegalValueError, rf.nonnegative_int, -100)
        self.assertEqual(20, rf.nonnegative_int(20))
        self.assertIs(20, rf.nonnegative_int(20))
        self.assertEqual(0, rf.nonnegative_int(0))
        self.assertIs(0, rf.nonnegative_int(0))


class TestLimited(unittest.TestCase):
    def test_in_range(self):
        pass
    # TODO

class TestLimitedInt(unittest.TestCase):
    pass
    # TODO


class TestLimitedLen(unittest.TestCase):
    def test_upper_limit_only(self):
        pass
    # TODO
