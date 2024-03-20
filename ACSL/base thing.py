#stuff for function below
import string
di = string.digits + string.ascii_letters

#validation for n
valid = False
while not valid:
    n = input("Please enter how many numbers do you want to generate: ")
    try:
        n = int(n)
        valid = True
    except:
        print("ErRor!!! Please try again!")

#validation for b
valid = False
while not valid:
    b = input("Please enter the number for the base, between 2 and 9 inclusive: ")
    try:
        b = int(b)
        if b >= 2 and b <= 9:
            valid = True
    except:
        print("ErRor!!! Please try again!")

#validation for s
valid = False
while not valid:
    s = input("Please enter a starting number smaller than 16 digits long: ")
    try:
        if len(s) < 16:
            s = int(s)
            valid = True
    except:
        print("ErRor!!! Please try again!")

#function to change bases
def basechanger(x, base):
    if x == 0:
        return 0
    digits = []
    while x:
        digits.append(di[x % base])
        x = x // base
    digits.reverse()
    return ''.join(digits)
    
#add everything into a string
addstr = ''
for i in range(n):
    addstr += basechanger(i+s, b)
    print(basechanger(i+s, b))

#find how many of the maxnum is inside the string
maxnum = int(b-1)
count = 0
for add in addstr:
    if int(add) == maxnum:
        count += 1

print(count, "final count")

    

