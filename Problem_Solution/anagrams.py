class Solution:
    def __init__(self):
        self.a = ""
        self.b = ""

    def anagrams(self) -> bool:
        inp1 = self.a
        inp2 = self.b
        # if the length of the two strings is not the same, they are not anagrams.
        if len(inp1) != len(inp2):
            return False

        # initialize the dictionary
        counts = {}

        # loop simultaneously through the characters of the two strings.
        for c1, c2 in zip(inp1, inp2):
            if c1 in counts.keys():
                counts[c1] += 1
            else:
                counts[c1] = 1
            if c2 in counts.keys():
                counts[c2] -= 1
            else:
                counts[c2] = -1

        # Loop through the dictionary values.
        # if the dictionary contains even one value which is
        # different than 0, the strings are not anagrams.
        for count in counts.values():
            if count != 0:
                return False
        return True


# test the implementation
def main():
    s = Solution()
    s.a = "listen"
    s.b = "silent"
    if s.anagrams():
        print(f"{s.a} and {s.b} are anagrams")
    else:
        print(f"{s.a} and {s.b} are not anagrams")


if __name__ == "__main__":
    main()

#################################################################

def check(s1, s2):
     
    # the sorted strings are checked
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
         
# driver code 
s1 ="listen"
s2 ="silent"
check(s1, s2)

#################################################################

from collections import Counter
 
# function to check if two strings are
# anagram or not
def check(s1, s2):
    # implementing counter function
    # print(Counter(s1)) => Counter({'s': 1, 'i': 1, 'l': 1, 'e': 1, 'n': 1, 't': 1})

    if(Counter(s1) == Counter(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")
 
 
# driver code
s1 = "listen"
s2 = "silent"
check(s1, s2)

