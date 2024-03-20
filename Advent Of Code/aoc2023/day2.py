# https://adventofcode.com/2023/day/2

game = []
with open(r"short.txt") as input:
    for i in input:
        game.append([i[5:6], i[8:9]])
        print(i)
input.close()