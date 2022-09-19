class Solution:
    def rev_words(self, s):
        str_list = s.split(' ')[::-1]
        return ' '.join(str_list)

    def rev_words_length_wise(self, s):
        str_list = sorted(s.split(' ')[::-1], key=len)
        return ' '.join(str_list)

    def length_of_words_in_string(self, s):
        str_len_list = [len(l) for l in s.split(' ')]
        return str_len_list


# Driver Code

in_s = "My Name is Praveen Garg"
print(Solution().rev_words(in_s))
print(Solution().rev_words_length_wise(in_s))
print(Solution().length_of_words_in_string(in_s))
