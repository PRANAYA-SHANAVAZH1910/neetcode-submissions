class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=""
        for i in s:
            if i.isalnum():
                cleaned=cleaned+i
        cleaned=cleaned.lower()
        if cleaned==cleaned[::-1]:
            return True
        else:
            return False
        