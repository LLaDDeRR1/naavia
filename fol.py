n = 103 * 7 ** 103 - 5 * 7 ** 57 + 98
otvet = 0

while n > 0:
    ost = n % 7
    n = n // 7
    otvet += ost
po=908
print(otvet)