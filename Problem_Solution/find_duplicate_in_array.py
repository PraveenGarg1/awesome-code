class Solution(object):
    def find_duplicate(self, nums):
        beg, end = 1, len(nums)-1
        
        while beg + 1 <= end:
            mid, count = (beg + end)//2, 0
            for num in nums:
                if num <= mid: count += 1        
            if count <= mid:
                beg = mid + 1
            else:
                end = mid
        return end

# Driver Code
print(Solution().find_duplicate([1,4,5,3,2,3,6]))
