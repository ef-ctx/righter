import unittest
from righter import dictionary


class DictionaryTestCase(unittest.TestCase):

    def test_words(self):
        self.assertTrue(isinstance(dictionary.WORDS, set))
        self.assertEqual(len(dictionary.WORDS), 350241)
        self.assertIn("platypus", dictionary.WORDS)
