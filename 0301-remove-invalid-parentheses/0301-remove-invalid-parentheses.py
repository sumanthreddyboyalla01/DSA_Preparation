class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Step 1: Calculate minimum misplaced '(' and ')'
        left_rem = 0
        right_rem = 0
        
        for char in s:
            if char == '(':
                left_rem += 1
            elif char == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1
                    
        ans = set()
        
        # Step 2: DFS to generate valid combinations
        def dfs(index, current, left_count, right_count, l_rem, r_rem):
            if index == len(s):
                if l_rem == 0 and r_rem == 0 and left_count == right_count:
                    ans.add("".join(current))
                return
            
            char = s[index]
            
            # Option 1: Remove current parenthesis (if budget permits)
            if char == '(' and l_rem > 0:
                dfs(index + 1, current, left_count, right_count, l_rem - 1, r_rem)
            elif char == ')' and r_rem > 0:
                dfs(index + 1, current, left_count, right_count, l_rem, r_rem - 1)
                
            # Option 2: Keep current character
            current.append(char)
            if char != '(' and char != ')':
                dfs(index + 1, current, left_count, right_count, l_rem, r_rem)
            elif char == '(':
                dfs(index + 1, current, left_count + 1, right_count, l_rem, r_rem)
            elif char == ')' and left_count > right_count: # Only keep ')' if valid prefix
                dfs(index + 1, current, left_count, right_count + 1, l_rem, r_rem)
            current.pop()

        dfs(0, [], 0, 0, left_rem, right_rem)
        return list(ans)