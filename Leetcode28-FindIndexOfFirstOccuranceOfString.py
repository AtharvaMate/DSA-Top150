class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = len(needle)
        flag = 0
        
        for i in range(len(haystack)):
            l = haystack[i:i+k]
            
            if(l == needle):
                return(i)
                flag = 1
                break
        
        if flag == 0:
            return(-1)