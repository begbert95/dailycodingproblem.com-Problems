Daily Coding Problem: Problem #2 [Hard]


Problem: 

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].


Follow-up: what if you can't use division?

----------------------------------------------------------------------------------------------------------------------------

Thoughts: 

My first thought was something like this: 

returnList = []
for i in range(len(nums)):
    returnList[i] = 1

    for j in range(len(nums)):
        if i != j :
            returnList[i] *= nums[j]

return returnList


I was confused by the follow-up, because I didn't use any division at all. Then I realized I could multiply each element in the array, then divide the total by each element at that position. EZPZ