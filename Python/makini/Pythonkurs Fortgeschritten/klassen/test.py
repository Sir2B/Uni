import unittest
from app import Rechner
import klass1
from klass1 import Klasse1

class TddBeispiel(unittest.TestCase):
    def setUp(self):
        self.rech = Rechner()
        self.klasse = klass1.Klasse1

    def test_rechner_add_method_gibt_richtiges_ergebnis(self):
        res = self.rech.add(2, 2)
        self.assertEqual(4, res)

    def test_rechner_gibt_fehler_wenn_beide_args_nicht_zahlen(self):
        self.assertRaises(ValueError, self.rech.add, 'zwei', 'drei')

    def test_klasstest(self):
        self.rech.addklass1()
        print type(self.rech.klass1)
        print klass1.Klasse1
        #import pdb; pdb.set_trace()
        type(self.rech.klass1)
        Klasse1
        assert type(self.rech.klass1) == Klasse1


if __name__ == '__main__':
    unittest.main()