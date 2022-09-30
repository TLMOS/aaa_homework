import unittest

from one_hot_encoder import fit_transform


class TestOneHotEncoder(unittest.TestCase):
    def test_str(self):
        word = 'Apple'
        expected = [
            ('Apple', [1])
        ]
        transformed = fit_transform(word)
        self.assertEqual(transformed, expected)

    def test_list(self):
        doc = ['Apple', 'Bee', 'Apple', 'Tree']
        expected = [
            ('Apple', [0, 0, 1]),
            ('Bee',   [0, 1, 0]),
            ('Apple', [0, 0, 1]),
            ('Tree',  [1, 0, 0]),
        ]
        transformed = fit_transform(doc)
        self.assertEqual(transformed, expected)

    def test_args(self):
        doc = ['Apple', 'Bee', 'Apple', 'Tree']
        expected = [
            ('Apple', [0, 0, 1]),
            ('Bee',   [0, 1, 0]),
            ('Apple', [0, 0, 1]),
            ('Tree',  [1, 0, 0]),
        ]
        transformed = fit_transform(*doc)
        self.assertEqual(transformed, expected)

    def test_case_sensetivity(self):
        doc = ['Apple', 'apple', 'aPple']
        transformed = fit_transform(doc)
        self.assertNotIn('appLE', transformed)

    def test_zero_args(self):
        with self.assertRaises(TypeError):
            fit_transform()
