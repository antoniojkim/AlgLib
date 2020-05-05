# -*- coding: utf-8 -*-
import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from stableMatching import stable_matching


def test_stable_matching_1():
    matching = stable_matching(
        companies=[1, 2, 3, 4],
        company_rankings={
            1: ["A", "B", "C", "D"],
            2: ["A", "D", "C", "B"],
            3: ["A", "C", "B", "D"],
            4: ["A", "B", "C", "D"],
        },
        interns=["A", "B", "C", "D"],
        intern_rankings={
            "A": [1, 3, 4, 2],
            "B": [4, 3, 2, 1],
            "C": [2, 3, 1, 4],
            "D": [3, 4, 2, 1],
        },
    )
    expected = {"A": 1, "D": 2, "C": 3, "B": 4}

    assert matching == expected
