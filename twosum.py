from typing import List
class Solution:
    def twosum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,num in enumerate(nums):
            complement = target-num
            if complement in map:
                return [map[complement],i]
            map[num]=i

obj1 = Solution()
print(obj1.twosum([4,5,6],10))
