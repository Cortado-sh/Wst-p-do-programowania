import random

matrix = [[random.randint(0, 50) for _ in range(5)] for _ in range(5)]
greater_than_20 = [cell for row in matrix for cell in row if cell > 20]
count_greater_than_20 = len(greater_than_20)
average = sum(cell for row in matrix for cell in row) / 25

for row in matrix:
    print(row)
print("Liczba elementów większych niż 20:", count_greater_than_20)
print("Średnia dla całej tablicy:", average)
