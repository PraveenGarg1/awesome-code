class Solution:
    @classmethod
    def get_min_diff(self, arr, n, k):
        arr.sort()
        maxo = arr[-1]
        mino = arr[0]
        out = maxo - mino
        low = arr[0] + k
        high = arr[-1] - k
        for i in range(1, n):
            if arr[i] >= k:
                maxo = max(arr[i - 1] + k, high)
                mino = min(arr[i] - k, low)
                out = min(out, maxo - mino)
        return out


print(Solution().get_min_diff([5, 1, 10, 8], 4, 2))
