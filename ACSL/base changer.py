def basechanger(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

for i in range(25):
    print(basechanger(i+324, 5))
