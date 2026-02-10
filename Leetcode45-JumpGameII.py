class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        l = r = 0

        while r < len(nums)-1:
            maxjump = 0
            for i in range(l, r+1):
                maxjump = max(maxjump, i+nums[i])
            
            l = r+1
            r = maxjump
            ans += 1
        
        return ans