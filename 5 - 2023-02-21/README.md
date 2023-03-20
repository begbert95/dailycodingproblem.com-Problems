Daily Coding Problem: Problem #5 [Medium]

Problem:

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.


----------------------------------------------------------------------------------------------

Thoughts:

I did some basic work to try and figure out what is was asking for, then realized what I need to do. Looked up pairs in python, aka tuples. I thought it would be easy, but I wasn't grasping the full problem. I found this solution which helps explain the problem https://galaiko.rocks/posts/dcp/problem-5/

Here's my initial shot

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    return pair[0]

def cdr(pair):
    return pair[1]



car(cons(3, 4))
cdr(cons(3, 4))