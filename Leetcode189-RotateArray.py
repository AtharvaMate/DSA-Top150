class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            last = len(nums)-1
            temp = nums[last]
            nums.pop(last)
            nums.insert(0, temp)