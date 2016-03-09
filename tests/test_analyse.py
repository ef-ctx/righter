import unittest
import copy
from righter.analyse import precision, recall, flatten

annotated = {
    '1': [
        {
            'symbol': 'NSW',
            'correct': 'always',
            'start': 127,
            'selection': 'alway'
        },
        {
            'symbol': 'NSW',
            'correct': 'terrible',
            'start': 207,
            'selection': 'lerible'
        }
    ],
    '2': [
        {
            'symbol': 'NSW',
            'correct': 'never',
            'start': 22,
            'selection': 'nev'
        }
    ],
}

class FlattenTestCase(unittest.TestCase):

    def setUp(self):
        self.annotated = copy.deepcopy(annotated) 

    def test_multiple(self):
        expected = {
            ('1', 127, 'alway', 'NSW'),
            ('1', 207, 'lerible', 'NSW'),
            ('2', 22, 'nev', 'NSW'),
        }
        self.assertEqual(flatten(self.annotated), expected)

    def test_one_doc(self):
        self.annotated.pop('1')
        expected = {
            ('2', 22, 'nev', 'NSW'),
        }
        self.assertEqual(flatten(self.annotated), expected)

    def test_empty(self):
        self.assertEqual(flatten({}), set())


class AnalysePredictionTestCase(unittest.TestCase):

    def setUp(self):
        self.annotated = copy.deepcopy(annotated)

    def test_all_correct(self):
        self.assertEqual(precision(self.annotated, self.annotated), 1.)

    def test_no_predictions_with_annotations(self):
        self.assertEqual(precision(self.annotated, {}), 1.)

    def test_no_predictions_empty_annotations(self):
        self.assertEqual(precision({}, {}), 1.)

    def test_no_annotations(self):
        self.assertEqual(precision({}, self.annotated), .0)

    def test_missing_document(self):
        predicted = copy.deepcopy(self.annotated)
        predicted.pop('1')
        self.assertEqual(precision(self.annotated, predicted), 1.)

    def test_missing_change(self):
        predicted = copy.deepcopy(self.annotated)
        predicted['1'].pop()
        self.assertEqual(precision(self.annotated, predicted), 1.)

    def test_wrong_prediction_bad_start(self):
        predicted = copy.deepcopy(self.annotated)
        predicted['1'][0]['start'] = 0
        self.assertEqual(precision(self.annotated, predicted), 2. / 3.)

    def test_wrong_prediction_bad_symbol(self):
        predicted = copy.deepcopy(self.annotated)
        predicted['1'][0]['symbol'] = 'SP'
        self.assertEqual(precision(self.annotated, predicted), 2. / 3.)

    def test_wrong_prediction_bad_selection(self):
        predicted = copy.deepcopy(self.annotated)
        predicted['1'][0]['symbol'] = 'xxxx'
        self.assertEqual(precision(self.annotated, predicted), 2. / 3.)

    def test_wrong_prediction_extra_prediction(self):
        predicted = copy.deepcopy(self.annotated)
        predicted['1'].append({
            'symbol': 'SP',
            'correct': 'maye',
            'start': 99,
            'selection': 'maybe'
        })
        self.assertEqual(precision(self.annotated, predicted), 3. / 4.)


class AnalysePredictionTestCase(unittest.TestCase):

    def setUp(self):
        self.annotated = copy.deepcopy(annotated)

    def test_all_correct(self):
        self.assertEqual(recall(self.annotated, self.annotated), 1.)

    def test_no_predictions_with_annotations(self):
        self.assertEqual(recall(self.annotated, {}), 0.)

    def test_no_predictions_empty_annotations(self):
        self.assertEqual(recall({}, {}), 1.)

    def test_no_annotations(self):
        self.assertEqual(recall({}, self.annotated), 1.)

    def test_missing_document(self):
        predicted = copy.deepcopy(self.annotated)
        predicted.pop('1')
        self.assertEqual(recall(self.annotated, predicted), 1. / 3.)

    def test_missing_change(self):
        predicted = copy.deepcopy(self.annotated)
        predicted['1'].pop()
        self.assertEqual(recall(self.annotated, predicted), 2. / 3.)

    def test_wrong_prediction_bad_start(self):
        predicted = copy.deepcopy(self.annotated)
        predicted['1'][0]['start'] = 0
        self.assertEqual(recall(self.annotated, predicted), 2. / 3.)

    def test_wrong_prediction_bad_symbol(self):
        predicted = copy.deepcopy(self.annotated)
        predicted['1'][0]['symbol'] = 'SP'
        self.assertEqual(recall(self.annotated, predicted), 2. / 3.)

    def test_wrong_prediction_bad_selection(self):
        predicted = copy.deepcopy(self.annotated)
        predicted['1'][0]['symbol'] = 'xxxx'
        self.assertEqual(recall(self.annotated, predicted), 2. / 3.)

    def test_wrong_prediction_extra_prediction(self):
        predicted = copy.deepcopy(self.annotated)
        predicted['1'].append({
            'symbol': 'SP',
            'correct': 'maye',
            'start': 99,
            'selection': 'maybe'
        })
        self.assertEqual(recall(self.annotated, predicted), 1.)
