import unittest
from extract import extract_title

class TestAdd(unittest.TestCase):
    def test_extract(self):
        assert extract_title('# hello') == 'hello'

    def test_extract_fail(self):
        with self.assertRaises(Exception):
            extract_title('hello')

if __name__ == "__main__":
    unittest.main()