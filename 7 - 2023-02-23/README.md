Daily Coding Problem: Problem #7 [Medium] 

Problem:

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.


----------------------------------------------------------------------------------------------

Thoughts:

Doesn't seem too bad. After completing it, I thought it was surprising I didn't need a hashmap. I'm starting to figure out that most of the time the hashmap isn't necessary when dealing with letters. ord() and chr() should take care of that if needed