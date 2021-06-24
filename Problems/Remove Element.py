class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        num=0
        while num<len(nums):
            if nums[num]==val:
                nums.remove(val)
            num+=1
        for i in nums:
            if val in nums:
                nums.remove(val)
