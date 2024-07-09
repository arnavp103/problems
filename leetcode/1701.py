# 1701 Average Waiting Time


class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        current_time = 1
        num_customers = len(customers)
        total_waiting = 0

        for arrival, time in customers:
            current_time = max(arrival, current_time)

            total_waiting += (current_time - arrival) + time
            current_time += time

        return total_waiting / num_customers
