import unittest

from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase): 
    def test1(self): 
        self.assertIsNone(english_to_french("") ) # test when 2 is given as input the output is 4.
        self.assertIsNone(french_to_english("") ) # test when 2 is given as input the output is 4.
        
        self.assertEqual(english_to_french("Hello"),"Bonjour")  # test when 3.0 is given as input the output is 9.0.
        self.assertEqual(french_to_english("Bonjour"), "Hello")  # test when -3 is given as input the output is not -9.


# class TestDouble(unittest.TestCase): 
#     def test1(self): 
#         self.assertEqual(double(2), 4) # test when 2 is given as input the output is 4.
#         self.assertEqual(double(-3.1), -6.2) # test when -3.1 is given as input the output is -6.2.
#         self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.

unittest.main()