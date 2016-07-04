#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Tobias'
import unittest

from app.app.Rechner import Rechner


class TddBeispiel(unittest.TestCase):
    def setUp(self):
        self.rech = Rechner()

    def test_rechner_add_method(self):
        res = self.rech.add(2, 2)
        self.assertEqual(4, res)

if __name__ == '__main__':
    unittest.main()