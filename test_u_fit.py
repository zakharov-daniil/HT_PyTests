import unittest
from one_hot_encoder import fit_transform


class TestFitTransform(unittest.TestCase):

    def test_none(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_empty(self):
        result = fit_transform([])
        self.assertIsNotNone(result)
        self.assertEqual(result, [])

    def test_texts(self):
        texts = [
            (['Moscow', 'New York', 'Moscow', 'London'],
             [('Moscow', [0, 0, 1]), ('New York', [0, 1, 0]), ('Moscow', [0, 0, 1]), ('London', [1, 0, 0])]),
            (['hello', 'world'], [('hello', [0, 1]), ('world', [1, 0])]),
            (['red', 'red', 'green'], [('red', [0, 1]), ('red', [0, 1]), ('green', [1, 0])]),
            (['123'], [('123', [1])])
        ]

        for text in texts:
            result = fit_transform(text[0])
            self.assertIsNotNone(result)
            self.assertEqual(result, text[1])


if __name__ == '__main__':
    unittest.main()
