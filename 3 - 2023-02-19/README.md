Daily Coding Problem: Problem #3 [Medium] 

Problem:

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

-----------------------------------------------------------------------------------------------------------------------------

Thoughts:

I don't really know where to start here. I haven't done anything with serialization (at least I'm not familiar with the term). I'm also not very familiar with traversing binary trees, let alone in python. More research is required.