def divisionSolution(nums: list[int]):
    total = 1

    for i in nums:
        total *= i

    returnList = []
    for i in range(len(nums)):
        returnList.append(total // nums[i])

    return returnList


def noDivisionSolution(nums: list[int]):
    returnList = []
    for i in range(len(nums)):
        returnList.append(1)

        for j in range(len(nums)):
            if i != j :
                returnList[i] *= nums[j]

    return returnList



nums = [1, 2, 3, 4, 5]

print("Division: ", divisionSolution(nums))
print()
print("No division: ", noDivisionSolution(nums))