class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        i,j = 0,0
        n = len(needle)
        
        if len(haystack)<n:
            return -1

        if not needle:
            return 0 
        
        while i<len(haystack):
            if needle[j]==haystack[i] and needle[j:]==haystack[i:(i+n)]:
                return i
           
            else:
                i+=1
        return -1   
