class Solution:
    def rotate(self, nums: list, k: int) -> list:
        """
        modify nums in-place also.
        """
        n = len(nums)
        k = k if k < n else k % n
        sec_part = nums[0:n-k]
        first_part = nums[n-k:n]
        for i, j in enumerate(first_part+sec_part):
            nums[i] = j
        return nums

print(Solution().rotate([1, 2, 3, 4, 5],101))
