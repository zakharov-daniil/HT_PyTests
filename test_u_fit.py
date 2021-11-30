import unittest
from one_hot_encoder import fit_transform


class TestFitTransform(unittest.TestCase):

    def setUp(self):
        self.texts = [
            ['Moscow', 'New York', 'Moscow', 'London'],
            ['hello', 'world'],
            ['red', 'red', 'green'],
            ['123']
        ]
        self.expected = [
            [('Moscow', [0, 0, 1]), ('New York', [0, 1, 0]), ('Moscow', [0, 0, 1]), ('London', [1, 0, 0])],
            [('hello', [0, 1]), ('world', [1, 0])],
            [('red', [0, 1]), ('red', [0, 1]), ('green', [1, 0])],
            [('123', [1])]
        ]

    def tearDown(self):
        self.texts = []
        self.expected = []

    def test_none(self):
        with self.assertRaises(TypeError):
            result = fit_transform()

    def test_empty(self):
        result = fit_transform([])
        self.assertIsNotNone(result)
        self.assertEqual(result, [])

    def test_texts(self):
        for i in range(4):
            text = self.texts[i]
            result = fit_transform(text)
            self.assertIsNotNone(result)
            self.assertEqual(self.expected[i], result)


if __name__ == '__main__':
    unittest.main()
