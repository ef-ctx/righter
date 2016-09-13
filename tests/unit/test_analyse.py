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
        self.annotated = flatten(copy.deepcopy(annotated))

    def test_all_correct(self):
        self.assertEqual(precision(self.annotated, self.annotated), 1.)

    def test_no_predictions_with_annotations(self):
        self.assertEqual(precision(self.annotated, set()), 1.)

    def test_no_predictions_empty_annotations(self):
        self.assertEqual(precision(set(), set()), 1.)

    def test_no_annotations(self):
        self.assertEqual(precision(set(), self.annotated), .0)

    def test_missing_document(self):
        predicted = copy.deepcopy(self.annotated)
        predicted.pop()
        self.assertEqual(precision(self.annotated, predicted), 1.)

    def test_missing_change(self):
        predicted = copy.deepcopy(self.annotated)
        predicted.pop()
        self.assertEqual(precision(self.annotated, predicted), 1.)

    def test_wrong_prediction_bad_start(self):
        predicted = copy.deepcopy(self.annotated)
        predicted[0][1] = 0
        self.assertEqual(precision(self.annotated, predicted), 2. / 3.)

    def test_wrong_prediction_bad_symbol(self):
        predicted = copy.deepcopy(self.annotated)
        predicted[0][3] = 'SP'
        self.assertEqual(precision(self.annotated, predicted), 2. / 3.)

    def test_wrong_prediction_bad_selection(self):
        predicted = copy.deepcopy(self.annotated)
        predicted[0][3] = 'xxxx'
        self.assertEqual(precision(self.annotated, predicted), 2. / 3.)

    def test_wrong_prediction_extra_prediction(self):
        predicted = copy.deepcopy(self.annotated)
        predicted.add(('1', 99, 'maybe', 'SP'))
        self.assertEqual(precision(self.annotated, predicted), 3. / 4.)


class AnalysePredictionTestCase(unittest.TestCase):

    def setUp(self):
        self.annotated = flatten(copy.deepcopy(annotated))

    def test_all_correct(self):
        self.assertEqual(recall(self.annotated, self.annotated), 1.)

    def test_no_predictions_with_annotations(self):
        self.assertEqual(recall(self.annotated, set()), 0.)

    def test_no_predictions_empty_annotations(self):
        self.assertEqual(recall(set(), set()), 1.)

    def test_no_annotations(self):
        self.assertEqual(recall(set(), self.annotated), 1.)

    def test_missing_document(self):
        predicted = copy.deepcopy(self.annotated)
        predicted.pop()
        predicted.pop()
        self.assertEqual(recall(self.annotated, predicted), 1. / 3.)

    def test_missing_change(self):
        predicted = copy.deepcopy(self.annotated)
        predicted.pop()
        self.assertEqual(recall(self.annotated, predicted), 2. / 3.)

    def test_wrong_prediction_bad_start(self):
        predicted = list(copy.deepcopy(self.annotated))
        predicted[0] = (predicted[0][0], 0, predicted[0][2], predicted[0][3])
        self.assertEqual(recall(set(self.annotated), set(predicted)), 2. / 3.)

    def test_wrong_prediction_bad_symbol(self):
        predicted = list(copy.deepcopy(self.annotated))
        predicted[0] = (predicted[0][0], predicted[0][1], predicted[0][2], 'SP')
        self.assertEqual(recall(set(self.annotated), set(predicted)), 2. / 3.)

    def test_wrong_prediction_bad_selection(self):
        predicted = list(copy.deepcopy(self.annotated))
        predicted[0] = (predicted[0][0], predicted[0][1], predicted[0][2], 'xxxx')
        self.assertEqual(recall(self.annotated, set(predicted)), 2. / 3.)

    def test_wrong_prediction_extra_prediction(self):
        predicted = copy.deepcopy(self.annotated)
        predicted.add(('1', 99, 'maybe', 'SP'))
        self.assertEqual(recall(self.annotated, predicted), 1.)
