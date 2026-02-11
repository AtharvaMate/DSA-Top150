class Solution:
    def reverseWords(self, s: str) -> str:
        l = list(s.split(" "))
        l.reverse()
        for _ in range(len(l)):
            if "" in l:
                l.remove("")
        
        return "".join(l[i] + " " for i in range(len(l)-1)) + l[-1]