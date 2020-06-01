# -*- coding: utf-8 -*-
import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from alien_dictionary import derive_alien_language


def verify_alien_language(sorted_words, alphabet):
    alphabet = {l: i for i, l in enumerate(alphabet)}

    for w1, w2 in zip(sorted_words, sorted_words[1:]):
        for l1, l2 in zip(w1, w2):
            if l1 != l2:
                if alphabet[l1] > alphabet[l2]:
                    return False

                break

        else:
            if len(w1) > len(w2):
                return False

    return True


def verify_test(words):
    alphabet = derive_alien_language(words)
    assert verify_alien_language(words, alphabet)


def test_alien_language_1():
    assert derive_alien_language(["baa", "abcd", "abca", "cab", "cad"]) == [
        "b",
        "d",
        "a",
        "c",
    ]


def test_alien_language_2():
    assert derive_alien_language(["caa", "aaa", "aab"]) == ["c", "a", "b"]


def test_alien_language_3():
    assert derive_alien_language(["wrt", "wrf", "er", "ett", "rftt"]) == [
        "w",
        "e",
        "r",
        "t",
        "f",
    ]


def test_alien_language_4():
    verify_test(["baa", "abcd", "abca", "cab", "cad"])


def test_alien_language_5():
    verify_test(["caa", "aaa", "aab"])


def test_alien_language_6():
    verify_test(["wrt", "wrf", "er", "ett", "rftt"])
