class SegmentTree:

  def __init__(self, size):
    self.n = size
    self.tree = [0] * (4 * size)

  def update(self, node, start, end, idx, val):
    if start == end:
      self.tree[node] = val
      return
    mid = (start + end) // 2
    if start <= idx <= mid:
      self.update(2 * node, start, mid, idx, val)
    else:
      self.update(2 * node + 1, mid + 1, end, idx, val)
    self.tree[node] = self.tree[2 * node] ^ self.tree[2 * node + 1]

  def query(self, node, start, end, l, r):
    if r < start or end < l:
      return 0
    if l <= start and end <= r:
      return self.tree[node]
    mid = (start + end) // 2
    return self.query(2 * node, start, mid, l, r) ^ self.query(
        2 * node + 1, mid + 1, end, l, r
    )


class Solution:

  def palindromePath(
      self, n: int, edges: list[list[int]], s: str, queries: list[str]
  ) -> list[bool]:
    adj = [[] for _ in range(n)]
    for u, v in edges:
      adj[u].append(v)
      adj[v].append(u)

    parent = [0] * n
    depth = [0] * n
    heavy = [-1] * n
    head = [0] * n
    pos = [0] * n
    cur_pos = 0

    # 1st DFS: compute subtree sizes, depth, parent, and heavy child
    def dfs1(u, p, d):
      parent[u] = p
      depth[u] = d
      size = 1
      max_sub_size = 0
      for v in adj[u]:
        if v != p:
          sub_size = dfs1(v, u, d + 1)
          size += sub_size
          if sub_size > max_sub_size:
            max_sub_size = sub_size
            heavy[u] = v
      return size

    dfs1(0, -1, 0)

    # 2nd DFS: build HLD chains and positions
    def dfs2(u, h):
      nonlocal cur_pos
      head[u] = h
      pos[u] = cur_pos
      cur_pos += 1
      if heavy[u] != -1:
        dfs2(heavy[u], h)
      for v in adj[u]:
        if v != parent[u] and v != heavy[u]:
          dfs2(v, v)

    dfs2(0, 0)

    seg_tree = SegmentTree(n)
    node_masks = [1 << (ord(c) - ord('a')) for c in s]

    for i in range(n):
      seg_tree.update(1, 0, n - 1, pos[i], node_masks[i])

    def query_path(u, v):
      res = 0
      while head[u] != head[v]:
        if depth[head[u]] < depth[head[v]]:
          u, v = v, u
        res ^= seg_tree.query(1, 0, n - 1, pos[head[u]], pos[u])
        u = parent[head[u]]
      if depth[u] > depth[v]:
        u, v = v, u
      res ^= seg_tree.query(1, 0, n - 1, pos[u], pos[v])
      return res

    ans = []
    for q in queries:
      parts = q.split()
      if parts[0] == 'update':
        u = int(parts[1])
        c = parts[2]
        node_masks[u] = 1 << (ord(c) - ord('a'))
        seg_tree.update(1, 0, n - 1, pos[u], node_masks[u])
      else:
        u, v = int(parts[1]), int(parts[2])
        mask = query_path(u, v)
        # Check if mask has at most one bit set
        if (mask & (mask - 1)) == 0:
          ans.append(True)
        else:
          ans.append(False)

    return ans