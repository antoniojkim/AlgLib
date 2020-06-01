# -*- coding: utf-8 -*-

import numpy as np
from string import ascii_lowercase

letters = {l: i for i, l in enumerate(ascii_lowercase)}


def is_caesar(str1, str2):
    """
    Is one of the two strings a caesar cipher of the other?
    """
    # Strings must be of same length
    if len(str1) != len(str2):
        return False

    arr1 = np.array(list(map(lambda l: letters[l], str1)))
    arr2 = np.array(list(map(lambda l: letters[l], str2)))

    diff = np.abs(arr2 - arr1) % len(ascii_lowercase)

    if np.all(diff == diff[0]):
        return True

    return False


if __name__ == "__main__":

    assert is_caesar("abcdef", "bcdefg")
    assert is_caesar("bcdefg", "abcdef")
    assert is_caesar("abcdef", "uvwxyz")
    assert not is_caesar("abcdef", "tuwxyz")
