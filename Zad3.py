import matplotlib.pyplot as plt

time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
speed = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]

plt.scatter(time, speed, color='purple')
plt.title('Prędkość chwilowa pojazdu w czasie')
plt.xlabel('Czas (s)')
plt.ylabel('Prędkość chwilowa (km/h)')
plt.show()
