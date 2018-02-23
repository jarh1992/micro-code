c = int(input('Cantidad de primos a ver: '))
a = 4
b = 5
n = 7
v = 0
print('1) 2\n2) 3\n3) 5')
while a <= c:
    for j in range(3, b + 1, 2):
        v = (0, 1)[n % j != 0]
        if v == 0:
            break
    if v == 1:
        print(str(a) + ')', n)
        a += 1
        b = n
    n += 2

input()
