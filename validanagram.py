class Solution:
    # Using sorted keyword
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s)==sorted(t):
            return True
        return False
    
    # Regular Implementation using dict
    def isAnagramreg(self, s:str, t:str) -> bool:
        if len(s)!=len(t):
            return False
        
        my_dict = {}
        for i in range(len(s)):
            if s[i] not in my_dict:
                my_dict[s[i]]=1
            else:
                my_dict[s[i]]=my_dict[s[i]]+1
        
        for j in range(len(t)):
            if t[j] not in my_dict:
                return False
            elif my_dict[t[j]]==0:
                return False
            my_dict[t[j]]=my_dict[t[j]]-1
        return True

    
obj = Solution()
print(obj.isAnagramreg('race','carq'))

