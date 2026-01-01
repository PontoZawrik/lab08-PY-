def iseven(num):
    if num % 2 == 0:
        return True
    else:
        return False

a = map(int, input("Введите последовательность a: ").split())
b = map(int, input("Введите последовательность b: ").split())

evenA = 0
oddB = 0

for el in a:
    if iseven(el):
        evenA += 1

for el in b:
    if not iseven(el):
        oddB += 1

print(f"Количество четных чисел в A: {evenA}")
print(f"Количество нечетных чисел в B: {oddB}")