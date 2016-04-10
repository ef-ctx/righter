import unittest
from righter.competitor import ginger

class SplitSentencesTestCase(unittest.TestCase):

    def test_split_simple(self):
        sentences = [
            "I have an elephant.",
            " What a beautiful elephant!",
            " Wait, is it a flying elephant?",
            " Sure is.",
        ]
        self.assertEqual(ginger.split_sentences("".join(sentences)), sentences)

    def test_split_multiple_punctuation(self):
        sentences = [
            "I have an elephant.",
            " What a beautiful elephant!",
            " Wait, is it a flying elephant?!",
            " Sure is...",
        ]
        self.assertEqual(ginger.split_sentences("".join(sentences)), sentences)

class GingerCheckTestCase(unittest.TestCase):

    def test_check_article(self):
        expected = [
            {
                "correction": "an",
                "originalSymbol": 3,
                "selection": "a",
                "start": 7,
                "suggestions": ["an"],
                "symbol": "AR"
            }
        ]
        self.assertEqual(ginger.check("I have a elephant."), expected)

    def test_check_spelling(self):
        expected = [
            {
                "correction": "elephant",
                "originalSymbol": 1,
                "selection": "elephent",
                "start": 10,
                "suggestions": ["elephant", "elegant"],
                "symbol": "SP"
            }
        ]
        self.assertEqual(ginger.check("I have an elephent."), expected)

    def test_check_capitalization(self):
        expected = [
            {
                "correction": "All",
                "originalSymbol": 1,
                "selection": "all",
                "start": 20,
                "suggestions": ["All"],
                "symbol": "C"
            }
        ]
        self.assertEqual(ginger.check("I have an elephant. all hail the elephant!"), expected)

    def test_big_sentence(self):
        expected = [
            {
                'correction': 'All',
                "originalSymbol": 1,
                'selection': 'all',
                'start': 601,
                "suggestions": ["All"],
                'symbol': 'C'
            }
        ]
        text = " ".join("""
        All work and no play makes Jack a dull boy
        all work and no play makes Jack a dull boy
        all work and no play makes Jack a dull boy
        all work and no play makes Jack a dull boy
        all work and no play makes Jack a dull boy
        all work and no play makes Jack a dull boy
        all work and no play makes Jack a dull boy
        all work and no play makes Jack a dull boy
        all work and no play makes Jack a dull boy
        all work and no play makes Jack a dull boy
        all work and no play makes Jack a dull boy
        all work and no play makes Jack a dull boy
        all work and no play makes Jack a dull boy
        all work and no play makes Jack dull boy.
        all work and no play makes Jack a dull boy
        """.split())
        self.assertEqual(ginger.check(text), expected)
