from typing import Iterable
import unittest

from count_vectorizer import CountVectorizer


class TestCountVectorizer(unittest.TestCase):
    def two_corpus_compare(self,
                           corpus_1: Iterable[str], corpus_2: Iterable[str]):
        vectorizer_1 = CountVectorizer()
        vectorizer_2 = CountVectorizer()
        self.assertEqual(vectorizer_1.fit_transform(corpus_1),
                         vectorizer_2.fit_transform(corpus_2))
        self.assertEqual(vectorizer_1.get_feature_names(),
                         vectorizer_2.get_feature_names())

    def test_empty_corpus(self):
        vectorizer = CountVectorizer()
        self.assertEqual(vectorizer.fit_transform([]), [])
        self.assertEqual(vectorizer.get_feature_names(), [])

    def test_multi_document_corpus(self):
        corpus = [
            'Crock Pot Pasta Never boil pasta again',
            'Pasta Pomodoro Fresh ingredients Parmesan to taste'
            ]
        vectorizer = CountVectorizer()
        self.assertEqual(vectorizer.fit_transform(corpus),
                         [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                          [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]])
        self.assertEqual(vectorizer.get_feature_names(),
                         ['crock', 'pot', 'pasta', 'never', 'boil', 'again',
                          'pomodoro', 'fresh', 'ingredients', 'parmesan',
                          'to', 'taste'])

    def test_case_sensetivity(self):
        corpus_1 = ['Aplle Bee Table NINE bee']
        corpus_2 = ['aplle bee table nine bee']
        self.two_corpus_compare(corpus_1, corpus_2)

    def test_double_spaces(self):
        corpus_1 = ['Aplle     Bee Table  NINE bee']
        corpus_2 = ['aplle bee table nine bee']
        self.two_corpus_compare(corpus_1, corpus_2)

    def test_special_symbols(self):
        corpus_1 = ['aplle$ bee table nine, bee!']
        corpus_2 = ['aplle bee table nine bee']
        self.two_corpus_compare(corpus_1, corpus_2)

    def test_unfitted_get_feature_names(self):
        vectorizer = CountVectorizer()
        with self.assertRaises(ValueError):
            vectorizer.get_feature_names()


if __name__ == '__main__':
    unittest.main()
