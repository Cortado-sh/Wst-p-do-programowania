import numpy as np

macierz = np.random.randint(1, 100, size=(5, 5))
najwiekszy = np.max(macierz)
najmniejszy = np.min(macierz)
max_wiersze = np.max(macierz, axis=1)
max_kolumny = np.max(macierz, axis=0)
suma_wierszy = np.sum(macierz, axis=1)

print("Macierz 5x5:")
print(macierz)
print(f"\nNajwiększy element: {najwiekszy}")
print(f"Najmniejszy element: {najmniejszy}")
print("\nNajwiększe elementy w każdym wierszu:")
print(max_wiersze)
print("\nNajwiększe elementy w każdej kolumnie:")
print(max_kolumny)
print("\nSuma wartości w poszczególnych wierszach:")
print(suma_wierszy)
