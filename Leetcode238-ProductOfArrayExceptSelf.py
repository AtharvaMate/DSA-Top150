class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = postfix = 1
        ans = [1]

        for i in range(len(nums)-1):
            prefix *= nums[i]
            ans.append(prefix)
        
        for j in range(len(nums)-1, -1, -1):
            ans[j] *= postfix
            postfix *= nums[j]
        
        return ans
