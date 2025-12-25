class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s)==sorted(t):
            return True
        return False
    
    def isAnagramreg(self, s:str, t:str) -> bool:
    
obj = Solution()
print(obj.isAnagram('race','carr'))
