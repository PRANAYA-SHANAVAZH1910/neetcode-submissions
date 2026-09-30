class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={')':'(',']':'[','}':'{'}
        for c in s:
            if c=='(' or c=='[' or c=='{':
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack[-1]!=pairs[c]:
                    return False 
                stack.pop()
        return len(stack)==0
