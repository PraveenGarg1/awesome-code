# Consecutive characters frequency
from itertools import groupby

# initializing string
test_str = "geekksforgggeeksLL"
# exp_out = 122111132112

# printing original string
print("The original string is : " + test_str)

# Consecutive characters frequency
# Using list comprehension + groupby()
res = [len(list(j)) for _, j in groupby(test_str)]

# printing result
print("The Consecutive characters frequency : " + str(res))
