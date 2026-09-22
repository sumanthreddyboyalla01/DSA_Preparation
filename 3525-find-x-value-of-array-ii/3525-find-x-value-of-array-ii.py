from typing import List

class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree_prod = [1] * (4 * self.n)
        self.tree_cnt = [[0] * k for _ in range(4 * self.n)]
        self._build(nums, 1, 0, self.n - 1)

    def _merge(self, node: int, left_node: int, right_node: int):
        left_prod = self.tree_prod[left_node]
        right_prod = self.tree_prod[right_node]
        
        self.tree_prod[node] = (left_prod * right_prod) % self.k
        
        cnt = [0] * self.k
        for r in range(self.k):
            cnt[r] += self.tree_cnt[left_node][r]
            cnt[(left_prod * r) % self.k] += self.tree_cnt[right_node][r]
        
        self.tree_cnt[node] = cnt

    def _build(self, nums: List[int], node: int, l: int, r: int):
        if l == r:
            rem = nums[l] % self.k
            self.tree_prod[node] = rem
            self.tree_cnt[node][rem] = 1
            return
        
        mid = (l + r) // 2
        self._build(nums, 2 * node, l, mid)
        self._build(nums, 2 * node + 1, mid + 1, r)
        self._merge(node, 2 * node, 2 * node + 1)

    def update(self, node: int, l: int, r: int, idx: int, val: int):
        if l == r:
            rem = val % self.k
            self.tree_prod[node] = rem
            self.tree_cnt[node] = [0] * self.k
            self.tree_cnt[node][rem] = 1
            return
        
        mid = (l + r) // 2
        if idx <= mid:
            self.update(2 * node, l, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, r, idx, val)
        self._merge(node, 2 * node, 2 * node + 1)

    def query(self, node: int, l: int, r: int, ql: int, qr: int):
        if ql <= l and r <= qr:
            return self.tree_prod[node], self.tree_cnt[node]
        
        mid = (l + r) // 2
        if qr <= mid:
            return self.query(2 * node, l, mid, ql, qr)
        if ql > mid:
            return self.query(2 * node + 1, mid + 1, r, ql, qr)
        
        left_prod, left_cnt = self.query(2 * node, l, mid, ql, qr)
        right_prod, right_cnt = self.query(2 * node + 1, mid + 1, r, ql, qr)
        
        res_prod = (left_prod * right_prod) % self.k
        res_cnt = [0] * self.k
        for r_idx in range(self.k):
            res_cnt[r_idx] += left_cnt[r_idx]
            res_cnt[(left_prod * r_idx) % self.k] += right_cnt[r_idx]
            
        return res_prod, res_cnt


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        st = SegmentTree(nums, k)
        ans = []
        n = len(nums)
        
        for idx, val, start, x in queries:
            st.update(1, 0, n - 1, idx, val)
            _, cnt = st.query(1, 0, n - 1, start, n - 1)
            ans.append(cnt[x])
            
        return ans