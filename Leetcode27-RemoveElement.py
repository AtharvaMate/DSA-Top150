class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(0, len(nums)):
            if nums[0] == val:
                nums.pop(0)
            else:
                k += 1
                nums.append(nums[0])
                nums.pop(0)
            
        return(k)