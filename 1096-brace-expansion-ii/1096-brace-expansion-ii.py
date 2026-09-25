class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        # Stack maintains operations for grammar evaluation:
        # We handle implicitly concatenated terms by taking cross products,
        # and ',' delimited terms by taking set unions.
        
        stack = [[]]  # Current list of sets being multiplied/concatenated
        union_stack = []  # Stack to manage union operations across braces
        
        i = 0
        while i < len(expression):
            char = expression[i]
            
            if char.isalpha():
                # Single letter is a singleton set {char}
                stack[-1].append({char})
                i += 1
                
            elif char == '{':
                # Push state for a new nested group
                union_stack.append([])
                stack.append([])
                i += 1
                
            elif char == ',':
                # Take cross product of terms accumulated in the current group
                # and add to the top union set
                curr_set = self._concat_group(stack.pop())
                union_stack[-1].append(curr_set)
                stack.append([])  # Start a new product group for after comma
                i += 1
                
            elif char == '}':
                # Complete the final product group inside the braces
                curr_set = self._concat_group(stack.pop())
                union_stack[-1].append(curr_set)
                
                # Take union of all comma-separated sets within these braces
                brace_res = set().union(*union_stack.pop())
                
                # Append the resulting set back to the outer product group
                stack[-1].append(brace_res)
                i += 1
                
        # Final evaluation for outer expression
        final_set = self._concat_group(stack.pop())
        return sorted(list(final_set))

    def _concat_group(self, sets_list: list[set[str]]) -> set[str]:
        """Performs Cartesian product concatenation across a sequence of sets."""
        if not sets_list:
            return set()
        
        res = sets_list[0]
        for s in sets_list[1:]:
            res = {w1 + w2 for w1 in res for w2 in s}
        return res