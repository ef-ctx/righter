import unittest
from righter.competitor import language_tool

class LanguageToolCheckTestCase(unittest.TestCase):

    def test_check_article(self):
        expected = [
            {
                "explanation": "Use 'an' instead of 'a' if the following word starts with a vowel sound, e.g. 'an article', 'an hour'",
                "originalSymbol": 'EN_A_VS_AN',
                "selection": "a",
                "start": 7,
                "suggestions": ["an"],
                "symbol": "AR"
            }
        ]
        self.assertEqual(language_tool.check("I have a elephant."), expected)

    def test_check_spelling(self):
        expected = [
            {
                "explanation": "Possible spelling mistake found",
                "originalSymbol": 'MORFOLOGIK_RULE_EN_US',
                "selection": "elephent",
                "start": 10,
                "suggestions": ["elephant"],
                "symbol": "SP"
            }
        ]
        self.assertEqual(language_tool.check("I have an elephent."), expected)

    def test_check_capitalization(self):
        expected = [
            {
                "explanation": "This sentence does not start with an uppercase letter",
                "originalSymbol": 'UPPERCASE_SENTENCE_START',
                "selection": "all",
                "start": 20,
                "suggestions": ["All"],
                "symbol": "C"
            }
        ]
        self.assertEqual(language_tool.check("I have an elephant. all hail the elephant!"), expected)

    def test_check_week_day_capitalization(self):
        expected = [
            {
                "explanation": "Possible spelling mistake found",
                "originalSymbol": 'MORFOLOGIK_RULE_EN_US',
                "selection": "tuesday",
                "start": 26,
                "suggestions": ["Tuesday"],
                "symbol": "C"
            }
        ]
        self.assertEqual(language_tool.check("I bought an elephant last tuesday."), expected)
