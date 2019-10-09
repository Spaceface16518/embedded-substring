import unittest

from embedded_substring import match


class TestEmbeddedString(unittest.TestCase):
    def test_basic(self):
        target = "filler filler filler a filler filler filler b filler filler filler c filler"
        substring = "abc"

        expected = [21, 44, 67]
        actual = match(target, substring)
        self.assertIsNotNone(actual)
        self.assertEqual(expected, actual)

    def test_starting(self):
        target = "a filler filler filler b filler filler filler c filler filler filler d filler"
        substring = "abcd"

        expected = [0, 23, 46, 69]
        actual = match(target, substring)
        self.assertIsNotNone(actual)
        self.assertEqual(expected, actual)

    def test_none_none(self):
        target = "filler filler filler filler filler filler filler filler filler filler"
        substring = "abcd"

        actual = match(target, substring)
        self.assertIsNone(actual)

    def test_none_incomplete(self):
        target = "filler filler filler a filler filler filler b filler filler filler c filler"
        substring = "abcd"

        actual = match(target, substring)
        self.assertIsNone(actual)


if __name__ == '__main__':
    unittest.main()
