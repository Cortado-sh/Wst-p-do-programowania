from datetime import datetime

data_laboratoriow = datetime(2024, 12, 15)
data_kolokwium = datetime(2024, 12, 17)

dni_od_laboratoriow = (datetime.now() - data_laboratoriow).days
dni_do_kolokwium = (data_kolokwium - datetime.now()).days

miesiac = data_kolokwium.strftime("%B")
rok = data_kolokwium.year

print(f"Minęło {dni_od_laboratoriow} dni od ostatnich laboratoriów.")
print(f"Do kolokwium (17 {miesiac} {rok}) pozostało {dni_do_kolokwium} dni.")
