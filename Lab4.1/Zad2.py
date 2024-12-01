imiona = ["Anna", "Marek", "Kasia", "Piotr"]

imiona.sort()
print(imiona)

imiona.append("Tomek")
imiona.append("Zofia")
ostatnia = imiona.pop()
print(imiona)
print(ostatnia)

imiona.insert(3, "Jakub")
print(imiona)

imiona.reverse()
imiona = imiona * 2
print(imiona)
