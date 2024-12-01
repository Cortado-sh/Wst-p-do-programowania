def oblicz_bmi(waga, wzrost):
    bmi = waga / (wzrost ** 2)

    if bmi < 18.5:
        return f"BMI: {bmi:.2f} - Niedowaga"
    elif 18.5 <= bmi <= 24.9:
        return f"BMI: {bmi:.2f} - Pożądana masa ciała"
    elif 25 <= bmi <= 29.9:
        return f"BMI: {bmi:.2f} - Nadwaga"
    elif 30 <= bmi <= 34.9:
        return f"BMI: {bmi:.2f} - Otyłość I stopnia"
    elif 35 <= bmi <= 39.9:
        return f"BMI: {bmi:.2f} - Otyłość II stopnia"
    else:
        return f"BMI: {bmi:.2f} - Otyłość III stopnia"


waga = float(input("Podaj wagę w kilogramach: "))
wzrost = float(input("Podaj wzrost w metrach: "))

wynik = oblicz_bmi(waga, wzrost)
print(wynik)
