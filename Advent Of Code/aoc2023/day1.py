# https://adventofcode.com/2023/day/1

# part1 
# ans 55871
# with open(r"input\day1.txt") as input:
#     # word = [inp.split() for inp in (input.readline().strip())]
#     allwords = [inp.strip().split() for inp in input]
# input.close()

# total = 0
# for all in allwords:
#     word = [a for al in all for a in al] 
#     final = ''
#     for w in word:
#         try:
#             w = int(w)
#             final += str(w)
#         except:
#             continue
#     if len(final) == 1:
#         final += final
#     elif len(final) > 2:
#         final = final[0] + final[-1]
#     total += int(final)

# print(total)

# part 2
numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}
with open(r"day1short.txt") as input:
    allwords = [inp.strip().split() for inp in input]
    for a in allwords[0]:
        print((a))
input.close()

# total = 0
# for all in allwords:
#     word = [a for al in all for a in al] 
#     final = ''
#     for w in word:
#         try:
#             w = int(w)
#             final += str(w)
#         except:
#             continue
#     if len(final) == 1:
#         final += final
#     elif len(final) > 2:
#         final = final[0] + final[-1]
#     total += int(final)