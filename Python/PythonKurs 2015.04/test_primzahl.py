#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Tobias'

from primzahl import *
import unittest


class TestPrim(unittest.TestCase):
    def test_isprim(self):
        self.assertTrue(is_prim(2))
        self.assertTrue(is_prim(3))
        self.assertTrue(is_prim(5))
        self.assertTrue(is_prim(97))
        self.assertFalse(is_prim(96))
        self.assertFalse(is_prim(1))

    def test_calc_primes(self):
        self.assertEqual(len(calc_primes(100)), 25)
        self.assertEqual(calc_primes(5), [2, 3])

if __name__ == '__main__':
    unittest.main()
