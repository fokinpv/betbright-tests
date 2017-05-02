import unittest

from betbright_tests.anagram import find_anagrams


class TestAnagram(unittest.TestCase):

    def test_anagram(self):

        anagrams = find_anagrams('fleet', ['abc', 'lefte'])
        self.assertEqual(anagrams, ['lefte'])
