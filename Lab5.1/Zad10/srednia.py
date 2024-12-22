import random
import math

min_value = 1
max_value = 10

krotka = tuple(random.randint(min_value, max_value) for _ in range(10))

produkt = math.prod(krotka)
srednia_geometryczna = produkt**(1/len(krotka))

krotka, srednia_geometryczna
