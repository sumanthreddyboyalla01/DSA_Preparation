class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        # If rec1 is to the left, right, below, or above rec2, they do not overlap
        if rec1[2] <= rec2[0] or rec1[0] >= rec2[2] or rec1[3] <= rec2[1] or rec1[1] >= rec2[3]:
            return False
        return True