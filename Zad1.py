punkty = int(input("Podaj liczbę punktów: "))
if punkty > 80:
    print("Zaliczasz")
elif 50 <= punkty <= 80:
    print("Możesz poprawić")
else:
    print("Musisz poprawić")