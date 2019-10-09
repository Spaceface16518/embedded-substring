import unittest

from embedded_substring import match


class TestEmbeddedString(unittest.TestCase):
    @staticmethod
    def list_from_substring(s):
        return [char for char in s]

    def test_basic(self):
        target = "filler filler filler a filler filler filler b filler filler filler c filler"
        substring = "abc"

        expected = [range(21, 22), range(44, 45), range(67, 68)]
        actual = match(target, self.list_from_substring(substring))
        self.assertIsNotNone(actual)
        self.assertEqual(expected, actual)

    def test_starting(self):
        target = "a filler filler filler b filler filler filler c filler filler filler d filler"
        substring = "abcd"

        expected = [range(0, 1), range(23, 24), range(46, 47), range(69, 70)]
        actual = match(target, self.list_from_substring(substring))
        self.assertIsNotNone(actual)
        self.assertEqual(expected, actual)

    def test_none_none(self):
        target = "filler filler filler filler filler filler filler filler filler filler"
        substring = "abcd"

        actual = match(target, self.list_from_substring(substring))
        self.assertIsNone(actual)

    def test_none_incomplete(self):
        target = "filler filler filler a filler filler filler b filler filler filler c filler"
        substring = "abcd"

        actual = match(target, self.list_from_substring(substring))
        self.assertIsNone(actual)

    def test_multi_character_patterns(self):
        target = "this definitely is some cool filler text"
        patterns = ["this", "is", "cool"]

        expected = [range(0, 4), range(16, 18), range(24, 28)]
        actual = match(target, patterns)
        self.assertEqual(expected, actual)

    def test_one_match(self):
        target = "test"
        patterns = ["test"]

        expected = [range(0, 4)]
        actual = match(target, patterns)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
