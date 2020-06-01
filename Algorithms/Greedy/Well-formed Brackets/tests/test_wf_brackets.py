# -*- coding: utf-8 -*-
import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(file_dir, "../"))

from wf_brackets import wf_brackets


def test_wf_brackets_1():
    assert wf_brackets("()")
    assert not wf_brackets(")(")
    assert not wf_brackets("(()")
    assert not wf_brackets("())")
    assert wf_brackets("(())")
    assert wf_brackets("()()")


def test_wf_brackets_2():
    assert wf_brackets("()[]{}")
    assert not wf_brackets("([)]")
    assert wf_brackets("{[]}")
