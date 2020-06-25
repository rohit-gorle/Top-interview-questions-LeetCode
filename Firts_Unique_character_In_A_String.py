class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        new_dict = {}
        
        for i in s:
            if i in new_dict:
                new_dict[i] = 2
            else:    
                new_dict[i] = 1
        for j in range(0,len(s)):
            if new_dict.get(s[j])==1:
                return j
        return -1   
