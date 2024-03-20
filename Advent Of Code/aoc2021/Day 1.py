###Part 1###
numbersarecool = open("day1.txt", "r")
number_list = [line.strip("") for line in numbersarecool]
count = 1
string_numlist = str(number_list)
print(number_list, "bob")
res = []

for idx in range(1, len(number_list)):
    if number_list[idx - 1] < number_list[idx]:
        res.append(True)
    else:
        res.append(False)
        
print("List after filtering : " + str(res))
for r in res:
    if r == True:
        count += 1

print(count)

###Part 2###

#number_list = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
edgy = []
count = 0
sliders = 0
prev_slider = 0
for i in range(len(number_list)-2):
    if i == (len(number_list))-1 or i == (len(number_list))-2:
        sliders = int(number_list[i]) + int(number_list[i-2]) + int(number_list[i-1])
    else:
        sliders = int(number_list[i]) + int(number_list[i+2]) + int(number_list[i+1])
    if i != 0:
        if sliders > prev_slider:
            edgy.append(True)
        else:
            edgy. append(False)
    prev_slider = sliders

for e in edgy:
    if e == True:
        count += 1

print(count)
