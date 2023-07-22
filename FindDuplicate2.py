nums = [1,3,4,2,2]

def find_duplicate(nums):
    duplicate = set()
    seen = set()

    for num in nums:
        if num in seen:
            duplicate.add(num)
        else:
            seen.add(num)
    return list(duplicate)

find_duplicate(nums)
