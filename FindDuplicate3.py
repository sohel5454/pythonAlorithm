nums = [1,3,4,2,2]

def find_duplicate(nums):
    duplicate = {}

    for num in nums:
        duplicate[num] = duplicate.get(num,0)+1
    return[num for num,count in duplicate.items() if count>1]

find_duplicate(nums)
