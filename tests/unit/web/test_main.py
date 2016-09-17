import json
import unittest

from righter.web.main import app

ESSAY_C178718 = {
    "id": "C178718",
    "text": "\n            Dear James, How are you?  Some serious problems have been brought to my attention relating to your working styly and habits. This is a formal letter of warning to ask you to improve your work. let me outline the areas in which you need to improve your communicate with colleagues.You often doesn't think about teamwork and never update the databse. You must be more carful with time mannagement. You has been late for appointments before.You must be more tidy because this is your workplace. You must be more professional. I am looking forward that you will become better, otherwise you will out of here. Yours sincerely, Paul\n            ",
     "nationality": "cn",
     "changes": [
        {
            "selection": "James",
            "start": 18,
            "symbol": "C"
        },
        {
            "selection": "How",
            "start": 25,
            "symbol": "C"
        },
        {
            "selection": "let",
            "start": 206,
            "symbol": "C"
        },
        {
            "selection": "Paul",
            "start": 635,
            "symbol": "C"
        },
        {
            "selection": "styly",
            "start": 120,
            "symbol": "SP"
        },
        {
            "selection": "doesn",
            "start": 303,
            "symbol": "SP"
        },
        {
            "selection": "databse",
            "start": 353,
            "symbol": "SP"
        },
        {
            "selection": "carful",
            "start": 379,
            "symbol": "SP"
        },
        {
            "selection": "mannagement",
            "start": 396,
            "symbol": "SP"
        }
    ],
    "level": "7"
}



class MainTestCase(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.app = app.test_client()

    def test_healthcheck(self):
        response = self.app.get('/healthcheck')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(), b'Atchoo!')

    def test_static_index(self):
        response = self.app.get('/static/index.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(), b'<p>\nhello\n</p>\n')

    def test_retrieve_random_essay(self):
        response = self.app.get('/essays?random=1')
        self.assertEqual(response.status_code, 200)
        received = json.loads(response.get_data().decode())
        expected = dict(ESSAY_C178718)
        expected.pop("changes")
        expected.pop("level")
        expected.pop("nationality")
        self.assertEqual(received, expected)

    def test_retrieve_essay_C17871(self):
        response = self.app.get('/essays/C178718')
        self.assertEqual(response.status_code, 200)
        received = json.loads(response.get_data().decode())
        expected = dict(ESSAY_C178718)
        expected.pop("changes")
        expected.pop("level")
        expected.pop("nationality")
        self.assertEqual(received, expected)

    def test_predict_essay_C17871(self):
        decorated_essay = dict(ESSAY_C178718)
        decorated_essay["algorithm"] = "righter"
        response = self.app.post(
            '/predict',
            data=json.dumps(decorated_essay),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        received = json.loads(response.get_data().decode())
        expected = {
            'changes': [
                {'selection': 'James', 'start': 18, 'symbol': 'C'},
                {'selection': 'How', 'start': 25, 'symbol': 'C'},
                {'selection': 'let', 'start': 206, 'symbol': 'C'},
                {'selection': 'Paul', 'start': 635, 'symbol': 'C'},
                {'selection': 'styly', 'start': 120, 'symbol': 'SP'},
                {'selection': 'doesn', 'start': 303, 'symbol': 'SP'},
                {'selection': 'databse', 'start': 353, 'symbol': 'SP'},
                {'selection': 'mannagement', 'start': 396, 'symbol': 'SP'}
            ],
            'analysis': {
                'precision': 1.0,
                'recall': 0.8888888888888888
            }
        }
        self.assertEqual(received, expected)
