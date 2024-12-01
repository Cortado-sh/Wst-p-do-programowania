import math


def pole_trojkata(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
        if a <= 0 or b <= 0 or c <= 0:
            return "Boki trójkąta muszą być dodatnie."
        if a + b <= c or a + c <= b or b + c <= a:
            return "Podane długości boków nie tworzą trójkąta."

        s = (a + b + c) / 2
        pole = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return f"Pole trójkąta wynosi: {pole:.2f}"

    except ValueError:
        return "Wprowadzone dane muszą być liczbami."


a = input("Podaj długość boku a: ")
b = input("Podaj długość boku b: ")
c = input("Podaj długość boku c: ")

wynik = pole_trojkata(a, b, c)
print(wynik)
