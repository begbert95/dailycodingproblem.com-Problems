Daily Coding Problem: Problem #1 [Easy] 

Problem:

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?

----------------------------------------------------------------------------------------------------------------------

Thoughts:

Ignoring the Bonus, it's a fairly easy problem that can be solved with nested for loops. 

for i in nums:
    for j in nums:
        if(i != j):
            if(k == (i + j)):
                return True
return False

With the bonus it becomes more difficult. I want to say that a matrix will be part of the solution, but I don't recall anything about matrices at the moment to be sure. 

After some research, matrices aren't really helpful here. I did some more digging and found woodRock's Java solution here https://gist.github.com/woodRock/e71430ea29860a90bc83f9beb7f83ca4

Looking at it, I misunderstood the term pass. woodRock only goes over the entire array once, but accesses some elements multiple times. Good to know. I tested with the numbers provided, and it does check out. Now to do the same thing in python