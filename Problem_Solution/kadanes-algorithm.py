class Solution:
    # Complete this function
    # Function to find the sum of contiguous subarray with maximum sum.
    def __init__(self):
        pass

    @staticmethod
    def maxSubArraySum(arr, N):
        sum = 0
        max_sum = arr[0]
        for i in range(N):
            sum = sum + arr[i]
            max_sum = max(sum, max_sum)
            if sum < 0:
                sum = 0
        return max_sum


# Driver code
a = [-2, 1, 4, -7, 9, 10, -15]
