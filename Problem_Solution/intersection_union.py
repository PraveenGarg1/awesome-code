class Solution:
    # Function to return the count of number of elements in union of two arrays.
    @classmethod
    def do_union(self, a, b):
        list1 = set(a)
        list2 = set(b)
        return (list1 | list2)

    @staticmethod
    def do_intersection(a, b):
        list1 = set(a)
        list2 = set(b)
        return (list1 & list2)

a = [1,4,7,9,10]
b = [2,3,5,7,9,11]

print(Solution().do_union(a,b))
print(Solution.do_intersection(a,b))
