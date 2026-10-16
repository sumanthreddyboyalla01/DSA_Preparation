class SegmentTree:

  def __init__(self, n):
    self.n = n
    self.tree = [0] * (4 * n)  # Stores sum of squares
    self.lazy_sum = [0] * (4 * n)  # Stores sum of elements (cnt)
    self.lazy_add = [0] * (4 * n)  # Lazy addition tag

  def _push(self, node, left, right):
    v = self.lazy_add[node]
    if v != 0:
      mid = (left + right) // 2
      self._apply(2 * node, left, mid, v)
      self._apply(2 * node + 1, mid + 1, right, v)
      self.lazy_add[node] = 0

  def _apply(self, node, left, right, v):
    length = right - left + 1
    # tree[node] = sum((cnt + v)^2) = sum(cnt^2) + 2*v*sum(cnt) + v^2 * length
    self.tree[node] = (
        self.tree[node] + 2 * v * self.lazy_sum[node] + length * v * v
    ) % 1000000007
    # lazy_sum[node] = sum(cnt + v) = sum(cnt) + v * length
    self.lazy_sum[node] = (self.lazy_sum[node] + length * v) % 1000000007
    # lazy_add accumulates the delta
    self.lazy_add[node] = (self.lazy_add[node] + v) % 1000000007

  def update(self, node, left, right, ql, qr, val):
    if ql <= left and right <= qr:
      self._apply(node, left, right, val)
      return

    self._push(node, left, right)
    mid = (left + right) // 2
    if ql <= mid:
      self.update(2 * node, left, mid, ql, qr, val)
    if qr > mid:
      self.update(2 * node + 1, mid + 1, right, ql, qr, val)

    self.tree[node] = (self.tree[2 * node] + self.tree[2 * node + 1]) % 1000000007
    self.lazy_sum[node] = (
        self.lazy_sum[2 * node] + self.lazy_sum[2 * node + 1]
    ) % 1000000007

  def query(self, node, left, right, ql, qr):
    if ql <= left and right <= qr:
      return self.tree[node]

    self._push(node, left, right)
    mid = (left + right) // 2
    res = 0
    if ql <= mid:
      res = (res + self.query(2 * node, left, mid, ql, qr)) % 1000000007
    if qr > mid:
      res = (res + self.query(2 * node + 1, mid + 1, right, ql, qr)) % 1000000007
    return res


class Solution:

  def sumCounts(self, nums: List[int]) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    seg = SegmentTree(n)
    last_occurrence = {}
    total_sum = 0

    for j in range(n):
      prev_idx = last_occurrence.get(nums[j], -1)
      last_occurrence[nums[j]] = j

      # 1. Update the segment tree for the range [prev_idx + 1, j] by adding 1
      seg.update(1, 0, n - 1, prev_idx + 1, j, 1)

      # 2. Query the sum of squares of all subarrays ending at j (which spans from index 0 to j)
      current_running_sum = seg.query(1, 0, n - 1, 0, j)
      total_sum = (total_sum + current_running_sum) % MOD

    return total_sum