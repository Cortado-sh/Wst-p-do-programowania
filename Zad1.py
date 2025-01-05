import matplotlib.pyplot as plt

categories = ['Laptopy', 'Telefony', 'Kosmetyki', 'Książki', 'Rowery']
sales = [250, 400, 300, 150, 120]

plt.bar(categories, sales, color='lightcoral')
plt.title('Ilość sprzedanych produktów')
plt.xlabel('Kategorie')
plt.ylabel('Ilość sprzedanych produktów')
plt.show()
