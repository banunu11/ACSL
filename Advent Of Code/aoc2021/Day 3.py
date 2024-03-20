###Part 1###
'''
binaryfile = open("day3.txt", "r")
bifiread = binaryfile.read()
binary_data = bifiread.split("\n")
binaryfile.close()
binary_list = [[],[]]
print(binary_data)

gamma_rate = ''
zero = 0
one = 0
for j in range(12):
    for i in range(len(binary_data)):
        if i < 1000:
            if binary_data[i][j] == '0':
                zero += 1
            else:
                one += 1

    if one > zero:
        gamma_rate += '1'
    else:
        gamma_rate += '0'

epsilon_rate = ''
ze = 0
on = 1
for x in range(12):
    for y in range(len(binary_data)):
        if y < 1000:
            if binary_data[y][x] == '0':
                ze += 1
            else:
                on += 1

    if on < ze:
        epsilon_rate += '1'
    else:
        epsilon_rate += '0'

def binary_to_decimal(bina):
    fish = list(map(int, bina))
    fish.reverse()
    base10 = 0
    count = 0

    for fi in fish:
        placevalue = 2**count
        count += 1
        base10 += placevalue * fi
    return base10

grdeci = binary_to_decimal(gamma_rate)
erdeci = binary_to_decimal(epsilon_rate)
print(epsilon_rate)
print(gamma_rate)
print(grdeci * erdeci)

'''
data = open('day3.txt', 'r', encoding='utf-8').read().splitlines()

N = len(data[0])

gamma = 0
epsilon = 0

for n in range(N):
    count0 = sum(1 for line in data if line[n] == '0')
    count1 = len(data) - count0
    gamma *= 2
    epsilon *= 2
    if count0 < count1:
        gamma += 1
    else:
        epsilon += 1
print(gamma)
print(epsilon)
print(gamma * epsilon)


###Part 2###























