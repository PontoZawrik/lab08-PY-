import math

def example(a, b):
    return (a + math.sin(b)) / (b + math.sin(a))

print(f"y = {example(1, 4) + example(7, 5) + example(3, 2)}")