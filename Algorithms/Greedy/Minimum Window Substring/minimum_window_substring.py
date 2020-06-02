# -*- coding: utf-8 -*-
from collections import Counter


def minimum_window_substring(s: str, t: str) -> str:
    if len(t) > len(s):
        return ""
    if len(t) == len(s):
        return s if Counter(t) == Counter(s) else ""
    if len(t) == 1:
        return t if t in s else ""

    t = Counter(t)
    min_dist = (-1, len(s) + 1)
    indices = []
    j = 0
    sc = Counter()
    while j < len(s):
        if s[j] in t:
            indices.append(j)
            sc[s[j]] += 1
            if sc[s[j]] >= t[s[j]]:
                if all(sc.get(k, 0) >= v for k, v in t.items()):
                    start, end = min_dist
                    k = indices[0]
                    if j - k + 1 < end - start:
                        start, end = k, j + 1
                        min_dist = (start, end)

                    while indices:
                        k = indices.pop(0)
                        sc[s[k]] -= 1
                        if sc[s[k]] < t[s[k]]:
                            break
                        if indices:
                            k = indices[0]
                            if j - k + 1 < end - start:
                                start, end = k, j + 1
                                min_dist = (start, end)

        j += 1

    start, end = min_dist
    if start == -1:
        return ""

    return s[start:end]
