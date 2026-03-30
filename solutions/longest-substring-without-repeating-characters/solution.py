class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        dict_ = {}
        max_length = 0
        start = 0
    
        for end, char in enumerate(s):
            if char in dict_ and dict_[char] >= start:
                start = dict_[char] + 1
            dict_[char] = end
            max_length = max(max_length, end - start + 1)
    
        return max_length
        