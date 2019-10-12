
import numpy as np

class Node:
    
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def insert(self, val):
        if val < self.val:
            if self.left is not None:
                self.left.insert(val)
                
            else:
                self.left = Node(val)
                
        else:
            if self.right is not None:
                self.right.insert(val)
                
            else:
                self.right = Node(val)
                
    def print(self):
        if self.left is not None:
            self.left.print()
            
        print(self.val)
        
        if self.right is not None:
            self.right.print()
        
        
def binary_tree_to_doubly_linked_list(root):
    if root is None or (root.left is None and root.right is None):
        return root, root
    
    ll = None
    rr = None
    
    if root.left is not None:
        ll, lr = binary_tree_to_doubly_linked_list(root.left)

        lr.right = root
        root.left = lr
    
    else:
        ll = root
        
    if root.right is not None:
        rl, rr = binary_tree_to_doubly_linked_list(root.right)

        rl.left = root
        root.right = rl
    
    else:
        rr = root
        
    ll.left = rr
    rr.right = ll
    
    return ll, rr


if __name__ == '__main__':
    
    vals = np.random.randint(0, 20, size=10)
    root = None
    for val in vals:
        if root is None:
            root = Node(val)
        else:
            root.insert(val)
            
    print(vals)
    
    start, end = binary_tree_to_doubly_linked_list(root)
    
    current = start
    while current != end:
        print(current.val)
        current = current.right
        
    print(end.val)
    
        
        
