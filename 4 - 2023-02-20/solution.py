
def insertion_sort(arr):
    #from https://www.geeksforgeeks.org/python-program-for-insertion-sort/
    if (n := len(arr)) <= 1:
      return
    for i in range(1, n):
         
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def find_min(nums: list[int]):
    x = 1
    
    for i in nums:
        if i < x:
            continue
        elif i > x:
            return x
        else:
            x += 1
    return x
    
nums = [1, 2, 0]
insertion_sort(nums)
print("Solution is: ", find_min(nums))