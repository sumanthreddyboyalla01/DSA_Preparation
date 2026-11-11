class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # 1. Satisfy the minimum of both needs using the cheapest combined option
        common = min(need1, need2)
        total_cost = common * min(costBoth, cost1 + cost2)
        
        # 2. Handle remaining requirement for type 1
        rem1 = need1 - common
        total_cost += rem1 * min(costBoth, cost1)
        
        # 3. Handle remaining requirement for type 2
        rem2 = need2 - common
        total_cost += rem2 * min(costBoth, cost2)
        
        return total_cost