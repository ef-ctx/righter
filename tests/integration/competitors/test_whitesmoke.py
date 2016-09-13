import unittest
from righter.competitor import whitesmoke


class WhitesmokeCheckTestCase(unittest.TestCase):

    def test_check_article(self):
        expected = [
            {
                "originalSymbol": 'grammar.12',
                "selection": "a",
                "start": 7,
                "suggestions": ["an"],
                "symbol": "AR"
            }
        ]
        self.assertEqual(whitesmoke.check("I have a elephant."), expected)

    def test_check_spelling(self):
        expected = [
            {
                "originalSymbol": 'spelling.1',
                "selection": "elephent.",
                "start": 10,
                "suggestions": ["elephant.", 'elephants.', 'element.', 'elements.', 'Selepen.'],
                "symbol": "SP"
            }
        ]
        self.assertEqual(whitesmoke.check("I have an elephent."), expected)

    def test_check_a_vs_an_another_position(self):
        expected = [
            {
                "originalSymbol": 'grammar.12',
                "selection": "a",
                "start": 19,
                "suggestions": ["an"],
                "symbol": "AR"
            }
        ]
        self.assertEqual(whitesmoke.check("I am happy. I have a oyster."), expected)

    def test_check_capitalization(self):
        expected = [
            {
                "originalSymbol": 'grammar.3',
                "selection": "all",
                "start": 20,
                "suggestions": ["All"],
                "symbol": "C"
            }
        ]
        self.assertEqual(whitesmoke.check("I have an elephant. all hail the elephant!"), expected)

    def test_check_week_day_capitalization(self):
        expected = [
            {
                "originalSymbol": 'spelling.1',
                "selection": "tuesday.",
                "start": 26,
                "suggestions": [
                    "Tuesday.",
                    'Tuesdays.',
                    'Thursday.',
                    'Thursdays.',
                    'tubes.'
                ],
                "symbol": "C"
            }
        ]
        result = whitesmoke.check("I bought an elephant last tuesday.")
        self.assertEqual(result, expected)
