Daily Coding Problem: Problem #4 [Hard] 

Problem:

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.

------------------------------------------------------------------------------------------------------------------

Thoughts: 

It seems like sorting is the best path to a solution. I don't what python's built-in sort method is, but I assume it violates the rules. Divide and conquer algorithms aren't allowed, so an insertion sort seems like the obvious choice. 

Powershell has a 'contains' function that would make this super simple, but as far as I can tell python doesn't have an equivalent that would make this easier. You could do the following, but I think the time complexity would be worse.

x = 1

for i in range(len(nums)):
    for j in nums:
        if x == j:
            x += 1
return x
