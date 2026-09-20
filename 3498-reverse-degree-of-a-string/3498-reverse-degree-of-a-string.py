class Solution:
    def reverseDegree(self, s: str) -> int:
        total_degree = 0
        
        for idx, char in enumerate(s, start=1):
            # Calculate position in reversed alphabet: 'a' -> 26, 'b' -> 25, ..., 'z' -> 1
            reversed_alphabet_pos = 26 - (ord(char) - ord('a'))
            
            # Multiply by 1-indexed position in the string and add to total
            total_degree += reversed_alphabet_pos * idx
            
        return total_degree