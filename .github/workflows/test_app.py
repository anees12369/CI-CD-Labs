# This Python app will be used to test whether my simple python app will work across different enviroments via the matrix build after i have committed 

import unittest

from app import say_hello

class TestHello(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello(), "Hello, World!")