class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next
        index = 1

        first = -1
        last = -1
        minDist = float('inf')

        while curr.next:
            # Check whether curr is a critical point
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):

                if first == -1:
                    # First critical point
                    first = index
                else:
                    # Distance from previous critical point
                    minDist = min(minDist, index - last)

                last = index

            prev = curr
            curr = curr.next
            index += 1

        if first == last:
            return [-1, -1]

        maxDist = last - first

        return [minDist, maxDist]