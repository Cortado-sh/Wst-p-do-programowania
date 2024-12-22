import f_mat


kwadrat_10 = f_mat.kwadrat(10)
szescian_3 = f_mat.szescian(3)
dodaj_10_5 = f_mat.dodaj(10, 5)

print("[Import całego modułu]")
print(f"Kwadrat liczby 10: {kwadrat_10}")
print(f"Sześcian liczby 3: {szescian_3}")
print(f"Suma liczb 10 i 5: {dodaj_10_5}")

from f_mat import kwadrat, szescian, dodaj


kwadrat_10_b = kwadrat(10)
szescian_3_b = szescian(3)
dodaj_10_5_b = dodaj(10, 5)

print("\n[Import wybranych funkcji]")
print(f"Kwadrat liczby 10: {kwadrat_10_b}")
print(f"Sześcian liczby 3: {szescian_3_b}")
print(f"Suma liczb 10 i 5: {dodaj_10_5_b}")
