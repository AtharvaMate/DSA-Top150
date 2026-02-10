class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        unique = set(nums)
        for ele in unique:
            counter = nums.count(ele)
            if counter > int(len(nums)/2):
                return ele