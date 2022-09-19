# Removing Minimum and Maximum From Array

class Solution:
    def minimumDeletions(self, nums):
        nums_size = len(nums)
        if nums_size <= 2:
            return nums_size
        else:
            i = nums.index(min(nums))
            j = nums.index(max(nums))
            a, b = min(i, j), max(i, j)
            return min(a + 1 + nums_size - b, b + 1, nums_size - a)

# Driver code
print(Solution().minimumDeletions([2,4,5,7,1,6,10]))
