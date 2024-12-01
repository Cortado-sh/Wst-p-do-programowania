def wyswietl_parametry(*args):
    for parametr in args:
        print(parametr)

def max_parametr(*args):
    if len(args) == 0:
        return "Brak argumentów."
    return max(args)

wyswietl_parametry(1, 2, 3, "Hello", 5.6)

wynik = max_parametr(1, 2, 3, 4, 5)
print(f"Największa wartość to: {wynik}")
