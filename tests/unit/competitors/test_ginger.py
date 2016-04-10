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


class MergeSentecesTestCase(unittest.TestCase):

    def test_merge_inexact(self):
        sentences = [
            "I ate a lot of pasta.",
            " Now I feel unwell.",
            " Too much pasta is a bit of nasta.",
        ]
        max_size = len(sentences[0]) + len(sentences[1]) + 3
        expected = [
            sentences[0] + sentences[1],
            sentences[2]
        ]
        self.assertEqual(ginger.merge_sentences(sentences, max_size), expected)

    def test_merge_exact(self):
        sentences = [
            "I ate a lot of pasta.",
            " Now I feel unwell.",
            " Too much pasta is a bit of nasta.",
        ]
        max_size = len(sentences[0]) + len(sentences[1])
        expected = [
            sentences[0] + sentences[1],
            sentences[2]
        ]
        self.assertEqual(ginger.merge_sentences(sentences, max_size), expected)

    def test_merge_fits_all(self):
        sentences = [
            "I ate a lot of pasta.",
            " Now I feel unwell.",
            " Too much pasta is a bit of nasta.",
        ]
        max_size = len(sentences[0]) + len(sentences[1]) + len(sentences[2])
        expected = [
            sentences[0] + sentences[1] + sentences[2]
        ]
        self.assertEqual(ginger.merge_sentences(sentences, max_size), expected)

    def test_sentence_too_big(self):
        sentences = [
            "I ate a lot of pasta.",
            " Now I feel unwell.",
            " Too much pasta is a bit of nasta.",
        ]
        self.assertRaises(ginger.SentenceTooBigError, ginger.merge_sentences, sentences, 14)
