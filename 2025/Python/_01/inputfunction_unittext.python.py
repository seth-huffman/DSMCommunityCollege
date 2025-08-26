import unittest
from inputfunction import max, content

class TestFunctions(unittest.TestCase):

    def correctTotal(self):
        result = max(['-1', '0', '1'])
        self.assertEqual(result, 1)

    def notCorrectContent(self):
        result = max(['a', 'b', 'c'])
        self.assertIsNone(result)

    def correctContent(self):
        result = content(3, ['1', '2', '3'])
        self.assertEqual(result, [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
