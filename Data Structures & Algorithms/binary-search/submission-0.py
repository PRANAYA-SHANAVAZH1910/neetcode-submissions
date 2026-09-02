from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #nums is a list of integer , target is an integer
        #-> means the function should return an integer
        #the list is sorted in acsending order
        length=len(nums)
        left=0
        right=length-1
        while left<=right:
            mid=(right+left)//2
            if nums[mid]==target: 
                print("Target achieved")
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1    