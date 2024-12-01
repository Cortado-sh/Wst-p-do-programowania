stopnie = (
    "Szeregowy",
    "Kapral",
    "Sierżancie",
    "Porucznik",
    "Kapitan",
    "Major",
    "Pułkownik",
)

ilość_stopnii = len(stopnie)
Major_index = stopnie.index("Major")
Pułkownik_wstepowanie = "Pułkownik" in stopnie

print(ilość_stopnii)
print(Major_index)
print(Pułkownik_wstepowanie)
