class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        for key,val in count.items():
            if val == 1:
                return key
