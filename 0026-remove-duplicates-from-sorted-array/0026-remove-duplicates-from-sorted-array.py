class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list1 = []
        for i in nums:
            if i not in list1:
                list1.append(i)
        
        s = len(list1)
        for i in range(s):
            nums[i] = list1[i]
        return s
