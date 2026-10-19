class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        less_than = 0
        equal_to = 0
        
        for num in nums:
            if num < target:
                less_than += 1
            elif num == target:
                equal_to += 1
                
        # The indices start at 'less_than' and span for 'equal_to' counts
        return list(range(less_than, less_than + equal_to))