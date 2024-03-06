# Купи, або піраміди

## Завдання 1

Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель, використовуючи з'єднувачі, у порядку, який призведе до найменших витрат. Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин, а загальні витрати дорівнюють сумі з'єднання всіх кабелів.

Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати (пірамідальне сортування за допомогою модуля heapq).

### Приклад використання

````
cable_lengths = [4, 2, 7, 6, 1, 8, 5, 3]
min_total_cost = min_cost_to_connect_cables(cable_lengths)

Connecting 1 and 2, cost: 3. Total cost: 3
Connecting 3 and 3, cost: 6. Total cost: 9
Connecting 4 and 5, cost: 9. Total cost: 18
Connecting 6 and 6, cost: 12. Total cost: 30
Connecting 7 and 8, cost: 15. Total cost: 45
Connecting 9 and 12, cost: 21. Total cost: 66
Connecting 15 and 21, cost: 36. Total cost: 102
Minimum total cost for connecting cables: 102
````