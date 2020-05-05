# Well-Formed Brackets

## Problem

Given a string containing just the characters: `'(', ')', '{', '}', '['` and `']'`, determine if the input string is valid.
* Note: an empty string is also considered valid

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

## [Implementation](https://github.com/antoniojkim/AlgLib/blob/master/Algorithms/Greedy/Well-formed%20Brackets/wf_brackets.py#L3)

```python
def wf_brackets(string):
    bracket_pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    stack = []
    for c in string:
        if c in bracket_pairs.keys():
            stack.append(c)
        elif c in bracket_pairs.values():
            if len(stack) == 0 or stack[-1] != bracket_pairs[c]:
                return False

            stack.pop()

    if len(stack) > 0:
        return False

    return True
```

### Runtime

Total: `O(n)`
