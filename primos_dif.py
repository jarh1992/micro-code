"""
promedio entre 2 primos consecutivos
"""

array_base_primos = [2, 3, 5]


def gen_primos(num, array_base_primos):
    a, b, n, v = 4, 5, 7, 0
    while a <= num:
        for j in range(3, b + 1, 2):
            v = (0, 1)[n % j != 0]
            if v == 0:
                break
        if v == 1:
            array_base_primos.append(n)
            a += 1
            b = n
        n += 2
    return array_base_primos


def primos_dif(array_primos):
    n_array = []
    for i, j in enumerate(array_primos):
        if i < len(array_primos) - 1:
            n_array.append((array_primos[i + 1] + array_primos[i]) / 2)
    return n_array


if __name__ == '__main__':
    inp = int(input('cantidad: '))
    array_primos = gen_primos(inp, array_base_primos)
    print(array_primos)
    flag = True
    while flag:
        res = primos_dif(array_primos)
        print(res)
        i = input()
        array_primos = res
        if i == '1':
            flag = False
