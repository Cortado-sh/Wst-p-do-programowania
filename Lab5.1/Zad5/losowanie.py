import random

kulki = list(range(1, 50))
wylosowane = random.sample(kulki, 6)

print("Wylosowane liczby:", sorted(wylosowane))
