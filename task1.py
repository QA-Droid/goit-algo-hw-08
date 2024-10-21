import heapq

def min_cost_to_connect_cables(cable_lengths):
    heapq.heapify(cable_lengths)
    total_cost = 0
    while len(cable_lengths) > 1:
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths) 
        cost = first + second
        total_cost += cost
        heapq.heappush(cable_lengths, cost)
    return total_cost

cable_lengths = [5, 1, 9, 3, 7, 6]
result = min_cost_to_connect_cables(cable_lengths)
print(f"Мінімальні витрати на з'єднання кабелів: {result}")