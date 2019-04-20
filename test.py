#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import typeforce


class TestUnsignedInts(unittest.TestCase):
    def test_uint8(self):
        self.assertRaises(ValueError, typeforce.uint8, -1)
        self.assertRaises(ValueError, typeforce.uint8, -20)
        self.assertRaises(ValueError, typeforce.uint8, 2**8)
        self.assertRaises(ValueError, typeforce.uint8, 300)
        for i in range(0, 2**8):
            typeforce.uint8(i)

    def test_uint16(self):
        self.assertRaises(ValueError, typeforce.uint16, -1)
        self.assertRaises(ValueError, typeforce.uint16, -20)
        self.assertRaises(ValueError, typeforce.uint16, 2**16)
        self.assertRaises(ValueError, typeforce.uint16, 5446345)
        for i in range(0, 2**16):
            typeforce.uint16(i)

    def test_uint32(self):
        self.assertRaises(ValueError, typeforce.uint32, -1)
        self.assertRaises(ValueError, typeforce.uint32, -20)
        self.assertRaises(ValueError, typeforce.uint32, 2**32)
        self.assertRaises(ValueError, typeforce.uint32, 45874349824936)
        typeforce.uint32(0)
        typeforce.uint32(1)
        typeforce.uint32(2)
        typeforce.uint32(0xFFFFFFFE)
        typeforce.uint32(0xFFFFFFFF)
        for i in range(0, 0xFFFFFFFF, 4000):
            typeforce.uint32(i)

    def test_uint64(self):
        self.assertRaises(ValueError, typeforce.uint64, -1)
        self.assertRaises(ValueError, typeforce.uint64, -20)
        self.assertRaises(ValueError, typeforce.uint64, 2**64)
        self.assertRaises(ValueError, typeforce.uint64,
                          345837634922573643925763492312573634)
        typeforce.uint64(0)
        typeforce.uint64(1)
        typeforce.uint64(2)
        typeforce.uint64(2**64 - 2)
        typeforce.uint64(2**64 - 1)
        for i in range(0, 0xFFFFFFFFFFFFFFFF, 30000000000000):
            typeforce.uint64(i)


class TestSignedInts(unittest.TestCase):
    def test_int8(self):
        self.assertRaises(ValueError, typeforce.int8, -2**7 - 1)
        self.assertRaises(ValueError, typeforce.int8, -150)
        self.assertRaises(ValueError, typeforce.int8, 2**7)
        self.assertRaises(ValueError, typeforce.int8, 1560)
        for i in range(-128, 127):
            typeforce.int8(i)

    def test_int16(self):
        self.assertRaises(ValueError, typeforce.int16, -2**15 - 1)
        self.assertRaises(ValueError, typeforce.int16, -675832495)
        self.assertRaises(ValueError, typeforce.int16, 2**15)
        self.assertRaises(ValueError, typeforce.int16, 5446345)
        for i in range(-32768, 32767):
            typeforce.int16(i)

    def test_int32(self):
        self.assertRaises(ValueError, typeforce.int32, -2**31 - 1)
        self.assertRaises(ValueError, typeforce.int32, 2**31)
        self.assertRaises(ValueError, typeforce.int32, 45874349824936)
        typeforce.int32(-0x8000000)
        typeforce.int32(-0x8000000 + 1)
        typeforce.int32(-2)
        typeforce.int32(-1)
        typeforce.int32(0)
        typeforce.int32(1)
        typeforce.int32(2)
        typeforce.int32(0x7FFFFFFE)
        typeforce.int32(0x7FFFFFFF)
        for i in range(-0x8000000, 0x7FFFFFFF, 4000):
            typeforce.int32(i)

    def test_int64(self):
        self.assertRaises(ValueError, typeforce.int64, -2**64 - 1)
        self.assertRaises(ValueError, typeforce.int64, 2**64)
        self.assertRaises(ValueError, typeforce.int64,
                          345837634922573643925763492312573634)
        typeforce.int64(-0x8000000000000000)
        typeforce.int64(-0x8000000000000000 + 1)
        typeforce.int64(-2)
        typeforce.int64(-1)
        typeforce.int64(0)
        typeforce.int64(1)
        typeforce.int64(2)
        typeforce.int64(0x7FFFFFFFFFFFFFFE)
        typeforce.int64(0x7FFFFFFFFFFFFFFF)
        for i in range(-0x8000000000000000, 0x7FFFFFFFFFFFFFFF,
                       30000000000000):
            typeforce.int64(i)
