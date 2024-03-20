import string 

# inspo = input()
# msg = 'American Computer Science League (ACSL) is fun!'
inspo = '''ACSL, or the American Computer Science League, is an international computer science competition among more than 300 schools.  Originally founded in 1978 as the Rhode Island Computer Science League, it then became the New England Computer Science League.  American Computer Science League (ACSL) is fun!'''
table = str.maketrans('', '', string.punctuation.replace(" ","").replace(".",""))
newinspo = inspo.translate(table)
chars = newinspo.split('.')
for a in range(len(chars)):
    chars[a] = chars[a].split(' ')
    chars[a] = [item for item in chars[a] if item != '']
msg = ''.join(chars[-1])
chars.pop()
print(msg)    

print(chars)

def swf(chars, find, index):
    # print(find, index)
    last = None
    while index > 0:
        counter = 0
        last = None
        s = 0
        for x,y in enumerate(chars):
            w = 0
            s += 1
            for i, j in enumerate(y):
                # print(w,j)
                f = 0
                w += 1
                for v,b in enumerate(j):
                    f +=1
                    if find == b:
                        counter += 1
                        # print(find,index)
                        last = f'{s}.{w}.{f}'
                        if counter == index:
                            return last
        index //= 2
    if last is not None:
        return last
                    # print(s, w, f, b)
final = ''

check = 0
# print(swf(chars, 'u', 45))
for l in range(len(msg)):
    if msg[l].isspace():
        final += '_'
        check += 1
    elif msg[l] in string.punctuation:
        final += msg[l]
        check += 1
    elif msg[l].isalnum():
        if l != 0 and msg[l-1].isalnum():
            final += ' '
        final += swf(chars, msg[l], (l+1)-check)

print(final)
