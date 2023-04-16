class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        index = n - 1
        while index > 0 and nums[index-1] >= nums[index]:
            index -= 1
        if index > 0:
            i = n - 1
            while i > index-1 and nums[i] <= nums[index-1]:
                i -= 1
            nums[i], nums[index-1] = nums[index-1], nums[i]
        n -= 1
        while index < n:
            nums[index], nums[n] = nums[n], nums[index]
            index += 1
            n -= 1