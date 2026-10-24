class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_day(date_str: str) -> int:
            month, day = map(int, date_str.split("-"))
            return sum(days_in_months[:month - 1]) + day
        
        a_arr = date_to_day(arriveAlice)
        a_leave = date_to_day(leaveAlice)
        b_arr = date_to_day(arriveBob)
        b_leave = date_to_day(leaveBob)
        
        latest_arrival = max(a_arr, b_arr)
        earliest_departure = min(a_leave, b_leave)
        
        if latest_arrival <= earliest_departure:
            return earliest_departure - latest_arrival + 1
        
        return 0