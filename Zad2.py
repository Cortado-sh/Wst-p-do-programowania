import matplotlib.pyplot as plt

categories = ['Laptopy', 'Telefony', 'Kosmetyki', 'Książki', 'Rowery']
sales = [250, 400, 300, 150, 120]

plt.pie(sales, labels=categories, autopct='%1.1f%%', colors=['lightcoral', 'lightblue', 'lightgreen', 'lightyellow', 'lightpink'])
plt.title('Procentowy udział różnych kategorii w sprzedaży')
plt.show()
