import string

###Part 1###
my_file = open("day2.txt", "r")
content = my_file.read()
puzzle_data = content.split("\n")
my_file.close()

#Intalize values
horiz = 0
depth = 0

#Iterate over commands
for command in puzzle_data:
    if 'down' in command:
        #get number value from command
        number = int(command.strip(string.ascii_letters))
        depth += number
    elif 'up' in command:
        number = int(command.strip(string.ascii_letters))
        depth -= number
    elif 'forward' in command:
        number = int(command.strip(string.ascii_letters))
        horiz += number
          
print(f"Horizontal Postion: {horiz}")
print(f"Depth: {depth}")
print(f"Solution: {horiz*depth}")

###Part 2###
aim = 0
hori = 0
dep = 0

for command in puzzle_data:
    if 'down' in command:
        #get number value from command
        number = int(command.strip(string.ascii_letters))
        aim += number
    elif 'up' in command:
        number = int(command.strip(string.ascii_letters))
        aim -= number
    elif 'forward' in command:
        number = int(command.strip(string.ascii_letters))
        hori += number
        dep += (aim*number)

print(f"\nHorizontal Postion: {hori}")
print(f"Depth: {dep}")
print(f"Aim: {aim}")
print(f"Solution: {hori*dep}")


















        
