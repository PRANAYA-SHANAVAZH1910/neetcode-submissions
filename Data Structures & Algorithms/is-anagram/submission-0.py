class Solution:
    from collections import Counter 
    def isAnagram(self, s: str, t: str) -> bool:
        char_count_s=Counter(s)
        char_count_t=Counter(t)
        if (dict(char_count_s))==(dict(char_count_t)):
            return True
        else:
            return False 

