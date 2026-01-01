def geom_progress(b, q, n):
    if n <= 1:
        return b
    else:
        return q * geom_progress(b, q, n-1)

def sum_progress(b, q, n):
    if n <= 1:
        return b
    else:
        return sum_progress(b, q, n-1) + geom_progress(b, q, n)

b = float(input("b: "))
q = float(input("q: "))
n = float(input("n: "))

print(f"b-n: {geom_progress(b, q, n)}")
print(f"Сумма до n: {sum_progress(b, q, n)}")