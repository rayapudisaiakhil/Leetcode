# Contains Duplicate Leet Code Question
from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for i in range(len(nums)):
            if nums[i] in my_set:
                return True
            my_set.add(nums[i])
        return False
    
arr = [1,2,3,3]
obj1= Solution()
print(obj1.hasDuplicate(arr))
