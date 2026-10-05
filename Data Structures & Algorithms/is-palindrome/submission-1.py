class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=""
        for i in s:
            if i.isalnum():
                cleaned=cleaned+i
        cleaned=cleaned.lower()
        left=0
        right=len(cleaned)-1
        while left<right:
            if cleaned[left]!=cleaned[right]:
                return False
            left=left+1
            right=right-1
        return True
