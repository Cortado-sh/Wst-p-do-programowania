import random
los = random.randint(1, 1500)
spal = float(input("Podaj średnie spalanie samochodu w samych litrach:"))
paliwo = float(input("Podaj cenę paliwa:"))

spalone_paliwo = spal / 100 * los
koszt = spalone_paliwo * paliwo

print(f"Przejechana droga to:{(los)}km")
print(f"Spalone paliwo wynosi:{int(spalone_paliwo)}l")
print(f"Koszt podróży wynosi:{int(koszt)}zł")
