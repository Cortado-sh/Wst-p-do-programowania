imie = input("Podaj imię: ")
print("Witaj", imie)

wiek = int(input("Podaj wiek: "))
print("Twój wiek to:", wiek)

imie_nazwisko = input("Podaj imię i nazwisko: ")
imiona = imie_nazwisko.split()
inicjaly = imiona[0][0] + imiona[1][0]
print("Inicjały:", inicjaly)

lancuch = input("Podaj łańcuch: ")
print(lancuch * 5)

lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
lancuch3 = lancuch1 + lancuch2
print("Połączony łańcuch:", lancuch3)

polowa1 = lancuch1[:len(lancuch1)//2]
polowa2 = lancuch2[len(lancuch2)//2:]
lancuch4 = polowa1 + polowa2
print("Nowy łańcuch:", lancuch4)
