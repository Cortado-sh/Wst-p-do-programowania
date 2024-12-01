zakupy = {
    "Szynka": 12.0,
    "Kiełbasa": 10.5,
    "Kurczak (1 kg)": 15.0,
    "Wołowina (1 kg)": 28.0
}

for produkt, cena in zakupy.items():
    print(f"{produkt}: {cena:.2f} PLN")

suma = sum(zakupy.values())
print(f"\nCałkowity koszt produktów mięsnych: {suma:.2f} PLN")
