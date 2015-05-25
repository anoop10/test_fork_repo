import os
import sys
from collections import OrderedDict
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(os.path.join(os.path.dirname(__file__), "test_data"))
test_data_location = os.path.join(os.path.dirname(__file__), "test_data")
import CustomExceptions
import MaxSharePrice
import unittest

class ValidInputData(unittest.TestCase):        
    def testKnownResults(self):
        """
        1. when no of records per line is equal in all the lines of given csv file
        2. when a price value in a given line can not be evaluated eg : eval(14.3rf) will give SyntaxError
        3. when a price value is like a variable eg : a12.23 will raise NameError 
        """
        test_data_file_object = open(os.path.join(test_data_location,"test_data_sample1.csv"))
        self.assertEquals(OrderedDict(OrderedDict([('Company A', {'yrs_months': [], 'max_price': 0}), (' Company B', {'yrs_months': [], 'max_price': 0}), ('', {'yrs_months': [], 'max_price': 0})])), MaxSharePrice.MaxSharePriceFinder(test_data_file_object).get_max_price()) 
#  
        test_data_file_object1 = open(os.path.join(test_data_location,"test_data_sample2.csv"))
        self.assertEqual(OrderedDict([('Company A', {'yrs_months': ['2013 Sep'], 'max_price': 30})]), MaxSharePrice.MaxSharePriceFinder(test_data_file_object1).get_max_price())

    def testDataValidity(self):
        test_data_file_object2 = open(os.path.join(test_data_location,"test_data_sample3.csv"))
        self.assertRaises(SyntaxError, MaxSharePrice.MaxSharePriceFinder(test_data_file_object2).get_max_price)
        
        test_data_file_object3 = open(os.path.join(test_data_location,"test_data_sample4.csv"))
        self.assertRaises(CustomExceptions.BadInputException, MaxSharePrice.MaxSharePriceFinder(test_data_file_object3).get_max_price)

        test_data_file_object3 = open(os.path.join(test_data_location,"test_data_sample5.csv"))
        self.assertRaises(NameError, MaxSharePrice.MaxSharePriceFinder(test_data_file_object3).get_max_price)

         

if __name__ == "__main__":
    unittest.main()
