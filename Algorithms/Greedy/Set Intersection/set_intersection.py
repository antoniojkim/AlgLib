
import numpy as np


def naive_set_intersection(array1, array2):
    return list(sorted(set(array1) & set(array2)))


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


def assert_test(actual, expected):
    if set(actual) != set(expected):
        raise Exception(f"{actual} != {expected}")


if __name__ == "__main__":
    
    for i in range(100):
        array1 = sorted(np.random.randint(0, 20, size=np.random.randint(5, 20)))
        array2 = sorted(np.random.randint(0, 20, size=np.random.randint(5, 20)))
        
        assert_test(set_intersection(array1, array2),
                    naive_set_intersection(array1, array2))
        
