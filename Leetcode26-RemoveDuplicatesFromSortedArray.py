class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        expectedNums = []
        k = 0
        for i in range(0, len(nums)):
            if nums[0] not in expectedNums:
                nums.append(nums[0])
                expectedNums.append(nums[0])
                k += 1
            
            nums.pop(0)
        
        return(k)