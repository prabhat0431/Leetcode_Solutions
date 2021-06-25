class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length=len(nums)
        if target==0:
            return 0
        for i in range(length):
            if nums[i]==target:
                return i
            elif nums[i]>target:
                return i
        for i in nums:
            if i<target:
                return len(nums)
