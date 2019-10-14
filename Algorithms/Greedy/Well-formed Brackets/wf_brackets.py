
import numpy as np


def wf_brackets(string):
    '''
    Given a string containing just the characters '(', ')', determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed in the correct order.
    '''
    left_paren_count = 0
    for c in string:
        if c == "(":
            left_paren_count += 1
        
        elif c == ")":
            if left_paren_count > 0:
                left_paren_count -= 1
            else:
                return False
            
    if left_paren_count > 0:
        return False
            
    return True


def wf_brackets2(string):
    '''
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
    determine if the input string is valid. (Note that an empty string is also considered valid.)
    An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.

    '''
    left_paren_stack = []
    for c in string:
        if c in ("(", "{", "["):
            left_paren_stack.append(c)
        
        elif c in (")", "}", "]"):
            if len(left_paren_stack) == 0 or \
               (c == ")" and left_paren_stack[-1] != "(") or \
               (c == "}" and left_paren_stack[-1] != "{") or \
               (c == "]" and left_paren_stack[-1] != "["):
                return False
            
            left_paren_stack.pop()
            
    if len(left_paren_stack) > 0:
        return False
            
    return True
    
    
    
if __name__ == "__main__":
    
    assert(wf_brackets("()") == True)
    assert(wf_brackets(")(") == False)
    assert(wf_brackets("(()") == False)
    assert(wf_brackets("())") == False)
    assert(wf_brackets("(())") == True)
    assert(wf_brackets("()()") == True)
    
    assert(wf_brackets2("()") == True)
    assert(wf_brackets2(")(") == False)
    assert(wf_brackets2("(()") == False)
    assert(wf_brackets2("())") == False)
    assert(wf_brackets2("(())") == True)
    assert(wf_brackets2("()()") == True)
    
    assert(wf_brackets2("()[]{}") == True)
    assert(wf_brackets2("([)]") == False)
    assert(wf_brackets2("{[]}") == True)
