# 1
imie = input()
print("Witaj", imie)

# 2
wiek = int(input())
print("Twój wiek to:", wiek)

# 3
imie, nazwisko = input().split()
inicjaly = imie[0] + nazwisko[0]
print(inicjaly)

# 4
tekst = input()
print(tekst * 5)

# 5
tekst1 = input()
tekst2 = input()
tekst3 = tekst1 + tekst2
print(tekst3)

# 6
tekst1 = input()
tekst2 = input()
polowa = tekst1[:len(tekst1)//2]
print(polowa)