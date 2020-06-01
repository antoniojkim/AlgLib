# -*- coding: utf-8 -*-


def set_intersection(array1, array2):
    i = 0
    j = 0

    intersection = []
    while i < len(array1) and j < len(array2):
        if array1[i] == array2[j]:
            intersection.append(array1[i])
            i += 1
            j += 1

        elif array1[i] < array2[j]:
            i += 1

        else:
            j += 1

    return intersection
