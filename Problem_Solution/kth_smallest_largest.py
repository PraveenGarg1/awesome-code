# kth smallest/largest element
class Solution:
    def kthSmallest_sorted(self, arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        tmp_list = sorted(arr)   # for largest tmp_list = sorted(arr)[::-1]
        if k > r or k < l:
            return -1
        return tmp_list[k - 1]

    def kthSmallest_sort(self, arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        arr.sort()                 # for largest arr.sort(reverse=True)
        if k > r or k < l:
            return -1
        return arr[k - 1]


sol = Solution()
print(sol.kthSmallest_sort([3, 2, 6, 1, 4, 9, 5], 0, 6, 4))
print(sol.kthSmallest_sorted([3, 2, 6, 1, 4, 9, 5], 0, 6, 4))

