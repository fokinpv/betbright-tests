"""Find the anagram
Write a function that accepts a word (string) and a list of words (list or
tuple of strings) and return back a list with the valid anagrams for
the word inside the given words list.
"""
import itertools


def find_anagrams(word, words):
    return list({
        ''.join(anagram)
        for anagram in itertools.permutations(word)
        if ''.join(anagram) in words
    })
