class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = []

        i=0
        min_str = min(strs, key=len)
        while(i<len(min_str)):
            flag=0
            for items in strs:
                if(items[i] == min_str[i]):
                    flag+=1
            if(flag == len(strs)):
                ans.append(min_str[i])
                i+=1
            else:
                break

        final = "".join(ans)
        return(final)
                