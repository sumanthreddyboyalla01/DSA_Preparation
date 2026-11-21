from collections import defaultdict


class Solution:

  def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
    n = len(parent)
    orig_children = [[] for _ in range(n)]
    for i in range(1, n):
      orig_children[parent[i]].append(i)

    new_parent = parent[:]
    last_seen = {}

    def assign_parents(u: int):
      ch = s[u]
      prev = last_seen.get(ch, -1)
      if prev != -1 and u != 0:
        new_parent[u] = prev

      last_seen[ch] = u
      for v in orig_children[u]:
        assign_parents(v)

      if prev != -1:
        last_seen[ch] = prev
      else:
        del last_seen[ch]

    assign_parents(0)

    final_children = [[] for _ in range(n)]
    for i in range(1, n):
      final_children[new_parent[i]].append(i)

    ans = [0] * n

    def calc_size(u: int) -> int:
      size = 1
      for v in final_children[u]:
        size += calc_size(v)
      ans[u] = size
      return size

    calc_size(0)
    return ans