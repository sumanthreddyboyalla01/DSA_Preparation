class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        list1 = nums1 + nums2
        list1.sort()
        
       
        n = len(list1) // 2
        
        if len(list1) % 2 == 0:
            t = list1[n]
            y = list1[n-1]
            s = t + y
            
            return s / 2.0
            
        else:
            return float(list1[n])
