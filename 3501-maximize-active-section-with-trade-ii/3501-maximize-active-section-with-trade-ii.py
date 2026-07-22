from bisect import bisect_left, bisect_right
from typing import List

class SparseTable:
    def __init__(self, arr: list[int], mode: str = 'max'):
        self.mode = mode
        n = len(arr)
        if n == 0:
            self.st = []
            return
        K = n.bit_length()
        self.st = [[0] * n for _ in range(K)]
        self.st[0] = list(arr)
        
        for i in range(1, K):
            j = 0
            length = 1 << (i - 1)
            while j + (1 << i) <= n:
                if mode == 'max':
                    self.st[i][j] = max(self.st[i - 1][j], self.st[i - 1][j + length])
                else:
                    self.st[i][j] = min(self.st[i - 1][j], self.st[i - 1][j + length])
                j += 1

    def query(self, L: int, R: int) -> int:
        if L > R or not self.st:
            return float('-inf') if self.mode == 'max' else float('inf')
        length = R - L + 1
        k = length.bit_length() - 1
        if self.mode == 'max':
            return max(self.st[k][L], self.st[k][R - (1 << k) + 1])
        else:
            return min(self.st[k][L], self.st[k][R - (1 << k) + 1])


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones = s.count('1')
        
        
        P_char, P_start, P_end, P_len = [], [], [], []
        block_idx = [0] * n
        
        curr_char = s[0]
        start_i = 0
        
        for i in range(1, n):
            if s[i] != curr_char:
                P_char.append(curr_char)
                P_start.append(start_i)
                P_end.append(i - 1)
                P_len.append(i - start_i)
                
                b_id = len(P_char) - 1
                for k in range(start_i, i):
                    block_idx[k] = b_id
                    
                curr_char = s[i]
                start_i = i
                
        P_char.append(curr_char)
        P_start.append(start_i)
        P_end.append(n - 1)
        P_len.append(n - start_i)
        b_id = len(P_char) - 1
        for k in range(start_i, n):
            block_idx[k] = b_id
            
        m = len(P_char)
        
        
        V0 = [k for k in range(m) if P_char[k] == '0']
        V1 = [k for k in range(m) if P_char[k] == '1']
                
        
        M = [-1] * m
        for k in range(1, m - 1):
            if P_char[k] == '1':
                M[k] = P_len[k - 1] + P_len[k + 1]
                
        
        A1 = [P_len[k] for k in V1]
        A0 = [P_len[k] for k in V0]
        
        st_M = SparseTable(M, 'max')
        st_A1 = SparseTable(A1, 'min')
        st_A0 = SparseTable(A0, 'max')
        
        ans = []
        
        
        for l, r in queries:
            i = block_idx[l]
            j = block_idx[r]
            
            
            if j - i < 2:
                ans.append(total_ones)
                continue
                
            
            v_start = bisect_left(V1, i + 1)
            v_end = bisect_right(V1, j - 1) - 1
            
            if v_start > v_end:
                ans.append(total_ones)
                continue
                
            max_gain = 0
            
            
            k1 = V1[v_start]
            eff_L1 = (P_end[i] - l + 1) if (k1 - 1 == i) else P_len[k1 - 1]
            eff_R1 = (r - P_start[j] + 1) if (k1 + 1 == j) else P_len[k1 + 1]
            max_gain = max(max_gain, eff_L1 + eff_R1)
                
            
            if v_end > v_start:
                k2 = V1[v_end]
                eff_L2 = (P_end[i] - l + 1) if (k2 - 1 == i) else P_len[k2 - 1]
                eff_R2 = (r - P_start[j] + 1) if (k2 + 1 == j) else P_len[k2 + 1]
                max_gain = max(max_gain, eff_L2 + eff_R2)
                    
            
            if v_start + 1 <= v_end - 1:
                k_first = V1[v_start + 1]
                k_last = V1[v_end - 1]
                max_gain = max(max_gain, st_M.query(k_first, k_last))
                    
            
            min_1_len = st_A1.query(v_start, v_end)
            
            max_0_len = 0
            if P_char[i] == '0':
                max_0_len = max(max_0_len, P_end[i] - l + 1)
            if P_char[j] == '0':
                max_0_len = max(max_0_len, r - P_start[j] + 1)
                
            u_start = bisect_left(V0, i + 1)
            u_end = bisect_right(V0, j - 1) - 1
            if u_start <= u_end:
                max_0_len = max(max_0_len, st_A0.query(u_start, u_end))
                    
            gain2 = max_0_len - min_1_len
            max_gain = max(max_gain, gain2)
                
            ans.append(total_ones + max_gain)
            
        return ans