class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        # Convert each row into a bitmask integer
        bits1 = [sum(val << c for c, val in enumerate(row)) for row in img1]
        bits2 = [sum(val << c for c, val in enumerate(row)) for row in img2]

        max_overlap = 0

        # Try all row shifts (dr) and column shifts (dc)
        for dr in range(-n + 1, n):
            for dc in range(-n + 1, n):
                overlap = 0

                # Calculate overlap for the given shift vector (dr, dc)
                for r in range(n):
                    if 0 <= r + dr < n:
                        if dc >= 0:
                            row_overlap = (bits1[r] << dc) & bits2[r + dr]
                        else:
                            row_overlap = (bits1[r] >> -dc) & bits2[r + dr]
                        
                        # Count set bits in the overlap
                        overlap += row_overlap.bit_count()

                max_overlap = max(max_overlap, overlap)

        return max_overlap