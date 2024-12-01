def fibonacci(n):
    if n <= 0:
        return "Błąd: n musi być większe od 0."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Podaj numer wyrazu ciągu Fibonacciego: "))
wynik = fibonacci(n)
print(f"{n}-ty wyraz ciągu Fibonacciego to: {wynik}")
