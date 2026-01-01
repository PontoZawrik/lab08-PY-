def nod(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a, b = map(int, input("Введите два числа: ").split())
print(f"НОК = {a * b // nod(a, b)}")
