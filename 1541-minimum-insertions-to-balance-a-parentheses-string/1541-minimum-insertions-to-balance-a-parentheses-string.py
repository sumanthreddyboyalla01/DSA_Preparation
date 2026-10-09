class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        needed_closing = 0
        
        for char in s:
            if char == '(':
                # If needed_closing is odd, we have an unmatched single ')'
                # that must be completed before starting a new '(' sequence.
                if needed_closing % 2 == 1:
                    insertions += 1
                    needed_closing -= 1
                
                # Each '(' needs two ')'
                needed_closing += 2
            else:  # char == ')'
                needed_closing -= 1
                
                # Missing an opening '(' for this ')'
                if needed_closing < 0:
                    insertions += 1      # Insert '('
                    needed_closing += 2   # The inserted '(' expects two ')' (one is current char)
                    
        return insertions + needed_closing