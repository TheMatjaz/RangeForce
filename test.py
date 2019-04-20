#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import typeforce as tf


class TestUnsignedInts(unittest.TestCase):
    def test_uint8(self):
        self.assertRaises(tf.IllegalValueError, tf.uint8, -1)
        self.assertRaises(tf.IllegalValueError, tf.uint8, -20)
        self.assertRaises(tf.IllegalValueError, tf.uint8, 2**8)
        self.assertRaises(tf.IllegalValueError, tf.uint8, 300)
        for i in range(0, 2**8):
            self.assertEqual(i, tf.uint8(i))
            self.assertIs(i, tf.uint8(i))

    def test_uint16(self):
        self.assertRaises(tf.IllegalValueError, tf.uint16, -1)
        self.assertRaises(tf.IllegalValueError, tf.uint16, -20)
        self.assertRaises(tf.IllegalValueError, tf.uint16, 2**16)
        self.assertRaises(tf.IllegalValueError, tf.uint16, 5446345)
        for i in range(0, 2**16):
            self.assertEqual(i, tf.uint16(i))
            self.assertIs(i, tf.uint16(i))

    def test_uint32(self):
        self.assertRaises(tf.IllegalValueError, tf.uint32, -1)
        self.assertRaises(tf.IllegalValueError, tf.uint32, -20)
        self.assertRaises(tf.IllegalValueError, tf.uint32, 2**32)
        self.assertRaises(tf.IllegalValueError, tf.uint32, 45874349824936)
        tf.uint32(0)
        tf.uint32(1)
        tf.uint32(2)
        tf.uint32(0xFFFFFFFE)
        tf.uint32(0xFFFFFFFF)
        for i in range(0, 0xFFFFFFFF, 4000):
            self.assertEqual(i, tf.uint32(i))
            self.assertIs(i, tf.uint32(i))

    def test_uint64(self):
        self.assertRaises(tf.IllegalValueError, tf.uint64, -1)
        self.assertRaises(tf.IllegalValueError, tf.uint64, -20)
        self.assertRaises(tf.IllegalValueError, tf.uint64, 2**64)
        self.assertRaises(tf.IllegalValueError, tf.uint64,
                          345837634922573643925763492312573634)
        tf.uint64(0)
        tf.uint64(1)
        tf.uint64(2)
        tf.uint64(2**64 - 2)
        tf.uint64(2**64 - 1)
        for i in range(0, 0xFFFFFFFFFFFFFFFF, 30000000000000):
            self.assertEqual(i, tf.uint64(i))
            self.assertIs(i, tf.uint64(i))

    def test_uint_bits(self):
        self.assertRaises(tf.IllegalValueError, tf.uint_bits, 8, 3)
        self.assertRaises(tf.IllegalValueError, tf.uint_bits, 8, 2)
        self.assertRaises(tf.IllegalValueError, tf.uint_bits, -1, 2)
        self.assertRaises(tf.IllegalValueError, tf.uint_bits, -8, 2)
        for i in range(0, 8):
            self.assertEqual(i, tf.uint_bits(i, 3))
            self.assertIs(i, tf.uint_bits(i, 3))
        for i in range(0, 16):
            self.assertEqual(i, tf.uint_bits(i, 4))
            self.assertIs(i, tf.uint_bits(i, 4))


class TestSignedInts(unittest.TestCase):
    def test_int8(self):
        self.assertRaises(tf.IllegalValueError, tf.int8, -2**7 - 1)
        self.assertRaises(tf.IllegalValueError, tf.int8, -150)
        self.assertRaises(tf.IllegalValueError, tf.int8, 2**7)
        self.assertRaises(tf.IllegalValueError, tf.int8, 1560)
        for i in range(-128, 127):
            self.assertEqual(i, tf.int8(i))
            self.assertIs(i, tf.int8(i))

    def test_int16(self):
        self.assertRaises(tf.IllegalValueError, tf.int16, -2**15 - 1)
        self.assertRaises(tf.IllegalValueError, tf.int16, -675832495)
        self.assertRaises(tf.IllegalValueError, tf.int16, 2**15)
        self.assertRaises(tf.IllegalValueError, tf.int16, 5446345)
        for i in range(-32768, 32767):
            self.assertEqual(i, tf.int16(i))
            self.assertIs(i, tf.int16(i))

    def test_int32(self):
        self.assertRaises(tf.IllegalValueError, tf.int32, -2**31 - 1)
        self.assertRaises(tf.IllegalValueError, tf.int32, 2**31)
        self.assertRaises(tf.IllegalValueError, tf.int32, 45874349824936)
        tf.int32(-0x8000000)
        tf.int32(-0x8000000 + 1)
        tf.int32(-2)
        tf.int32(-1)
        tf.int32(0)
        tf.int32(1)
        tf.int32(2)
        tf.int32(0x7FFFFFFE)
        tf.int32(0x7FFFFFFF)
        for i in range(-0x8000000, 0x7FFFFFFF, 4000):
            self.assertEqual(i, tf.int32(i))
            self.assertIs(i, tf.int32(i))

    def test_int64(self):
        self.assertRaises(tf.IllegalValueError, tf.int64, -2**64 - 1)
        self.assertRaises(tf.IllegalValueError, tf.int64, 2**64)
        self.assertRaises(tf.IllegalValueError, tf.int64,
                          345837634922573643925763492312573634)
        tf.int64(-0x8000000000000000)
        tf.int64(-0x8000000000000000 + 1)
        tf.int64(-2)
        tf.int64(-1)
        tf.int64(0)
        tf.int64(1)
        tf.int64(2)
        tf.int64(0x7FFFFFFFFFFFFFFE)
        tf.int64(0x7FFFFFFFFFFFFFFF)
        for i in range(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF,
                       30000000000000):
            self.assertEqual(i, tf.int64(i))
            self.assertIs(i, tf.int64(i))


class TestNegativePositiveInt(unittest.TestCase):
    def test_negative_int(self):
        self.assertRaises(tf.IllegalValueError, tf.negative_int, 0)
        self.assertRaises(tf.IllegalValueError, tf.negative_int, 1)
        self.assertRaises(tf.IllegalValueError, tf.negative_int, 100)
        self.assertEqual(-20, tf.negative_int(-20))
        self.assertIs(-20, tf.negative_int(-20))

    def test_nonpositive_int(self):
        self.assertRaises(tf.IllegalValueError, tf.nonpositive_int, 1)
        self.assertRaises(tf.IllegalValueError, tf.nonpositive_int, 100)
        self.assertEqual(-20, tf.nonpositive_int(-20))
        self.assertIs(-20, tf.nonpositive_int(-20))
        self.assertEqual(0, tf.nonpositive_int(0))
        self.assertIs(0, tf.nonpositive_int(0))

    def test_positive_int(self):
        self.assertRaises(tf.IllegalValueError, tf.positive_int, 0)
        self.assertRaises(tf.IllegalValueError, tf.positive_int, -1)
        self.assertRaises(tf.IllegalValueError, tf.positive_int, -100)
        self.assertEqual(20, tf.positive_int(20))
        self.assertIs(20, tf.positive_int(20))

    def test_nonnegative_int(self):
        self.assertRaises(tf.IllegalValueError, tf.nonnegative_int, -1)
        self.assertRaises(tf.IllegalValueError, tf.nonnegative_int, -100)
        self.assertEqual(20, tf.nonnegative_int(20))
        self.assertIs(20, tf.nonnegative_int(20))
        self.assertEqual(0, tf.nonnegative_int(0))
        self.assertIs(0, tf.nonnegative_int(0))
