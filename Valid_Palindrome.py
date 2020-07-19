solution-1 without using alpha numeric function and using a dictionary-own method


class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        dic = {"a":1, "b":1, "c":1, "d":1, "e":1, "f":1, "g":1, "h":1, "i":1, "j":1, "k":1, "l":1, "m":1, "n":1, "o":1, "p":1, "q":1, "r":1, "s":1, "t":1, "u":1, "v":1, "w":1, "x":1, "y":1, "z":1, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "0":0}
        
        j = len(s)-1
        i = 0
        s = [k.lower() for k in s]
        
        print(s)
        
        while i<j:
            
            
            if (s[i] in dic) and (s[j] in dic):
                if (s[i]!=s[j]):
                    return 0
                if (s[i]==s[j]):
                    i+=1
                    j-=1
                
            if s[i] not in dic:
                i+=1
            if s[j] not in dic:
                j-=1
        return 1 
        
        
 
 Solution-2 using alpha numeric function
 
 
 class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s)-1
        
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                if s[i].lower() != s[j].lower():
                    return 0
                else:
                    i += 1
                    j -= 1
        return 1
