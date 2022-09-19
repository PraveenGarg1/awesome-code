# Strong Password
s = "Hello@123bye"

isUpper = False
isLower = False
isNumeric = False
isSpecial = False
allow_special_chars = ['@', '#', '$', '^']
for i in s:
    i_ascii = ord(i)
    if 65 <= i_ascii <= 90:
        isUpper = True
    if 97 <= i_ascii <= 122:
        isLower = True
    if 48 <= i_ascii <= 57:
        isNumeric = True
    if i in allow_special_chars:
        isSpecial = True
if isUpper and isLower and isNumeric and isSpecial:
    print("Strong Password: ", s)
else:
    print("Weak Password: ", s)
