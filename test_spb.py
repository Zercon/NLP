import unittest
from Finder import AddressNERHypothesis


class TestStreet(unittest.TestCase):
    def setUp(self):
        self.NERInstance = AddressNERHypothesis()

    def test_shkolnaya(self):
        testing_address = 'санкт-петербург школьная 20'
        res = self.NERInstance.getSPb(testing_address)
        self.assertEqual(('санкт-петербург', None), res[0])
        self.assertEqual(('школьная', None), res[1])
        self.assertEqual(('20', None, None), res[2])

    def test_full_gagarina(self):
        testing_address = 'санкт-петербург юрия гагарина 22 к2'
        res = self.NERInstance.getSPb(testing_address)
        self.assertEqual(('санкт-петербург', None), res[0])
        self.assertEqual(('юрия гагарина', None), res[1])
        self.assertEqual(('22', '2', None), res[2])

    def test_short_gagarina(self):
        testing_address = 'питер гагарина 22 к2'
        res = self.NERInstance.getSPb(testing_address)
        #self.assertEqual(('санкт-петербург', None), res[0])
        self.assertEqual(('гагарина', None), res[1])
        self.assertEqual(('22', '2', None), res[2])

    def test_untolovsky(self):
        testing_address = "санкт-петербург;юнтоловский 43 корпус 1"
        res = self.NERInstance.getSPb(testing_address)
        self.assertEqual(('санкт-петербург', None), res[0])
        self.assertEqual(('юнтоловский', None), res[1])
        self.assertEqual(('43', '1', None), res[2])


    def test_untolovsky_str(self):
        testing_address = "санкт-петербург;юнтоловский 43 строение 1"
        res = self.NERInstance.getSPb(testing_address)
        self.assertEqual(('санкт-петербург', None), res[0])
        self.assertEqual(('юнтоловский', None), res[1])
        self.assertEqual(('43',  None, '1'), res[2])

    def test_untolovsky_str(self):
        testing_address = "юнтоловский 43 ст 1"
        res = self.NERInstance.getSPb(testing_address)
        self.assertEqual(('юнтоловский', None), res[1])
        self.assertEqual(('43',  None, '1'), res[2])

if __name__ == '__main__':
    unittest.main()
