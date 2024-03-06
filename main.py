import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)  # Перетворення списку в min-heap

    total_cost = 0
    while len(cables) > 1:
        # Беремо два найменших кабелі з min-heap
        first_cable = heapq.heappop(cables)
        second_cable = heapq.heappop(cables)

        # З'єднуємо кабелі та оновлюємо загальні витрати
        connection_cost = first_cable + second_cable
        total_cost += connection_cost

        # Додаємо новий кабель до min-heap
        heapq.heappush(cables, connection_cost)

        print(f"Connecting {first_cable} and {second_cable}, cost: {connection_cost}. Total cost: {total_cost}")

    return total_cost

# Приклад використання
cable_lengths = [4, 2, 7, 6, 1, 8, 5, 3]
min_total_cost = min_cost_to_connect_cables(cable_lengths)

print("Minimum total cost for connecting cables:", min_total_cost)