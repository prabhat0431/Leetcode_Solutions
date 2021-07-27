# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
         return self.ArrayToBST(nums, 0, len(nums))

    def ArrayToBST(self, nums, left, right):
        if left == right:
            return None
        mid = (left + right) >> 1
        root = TreeNode(nums[mid])
        root.left = self.ArrayToBST(nums, left, mid)
        root.right = self.ArrayToBST(nums, mid + 1, right)
        return root
