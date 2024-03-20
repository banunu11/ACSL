import math

# s, n = map(int, input().split())
# hand = list(map(int, input().split()))
# draw = list(map(int, input().split()))
s, n = 9, 70
hand = [40, 35, 30, 56, 32, 58, 44, 17, 45]
draw = [31, 37, 10, 28, 21, 62, 7, 64, 16, 12]

def interval(s, n):
    if n%s == 0:
        return  n/s
    else:
        return math.trunc(n/s)+1
    # check interval size and return right num
    
def step_down(hand):
    step = 0
    for h in range(1, len(hand)):
        if hand[h] < hand[h-1]:
            step += 1
        else:
            continue
    return step
    # calculate num of step downs
        
def strata(s, n, hand, draw):
    if len(draw) != 0:
        inte = interval(s, n)
        where = math.trunc(draw[0] / (inte-1)) -1
        # if n - (where-1)*s == s-1:
        # print(draw[0],where, s)
        if hand[where] < where*inte and hand[where] > ((where-1)*inte)+1:
            return False, hand
            # no replace
        else:
            print(where)
            temp = hand
            temp[where] = draw[0]
            return step_down(temp), temp
            # replace
    else:
        return False, hand
    # intervals
    
# print(strata(s,n,hand,draw))    
    
def stratb(s, n, hand, draw):
    if len(draw) != 0:
        for i in range(0, len(hand), 3):
            # print(i, hand[i], hand[i+1], hand[i+2])
            if hand[i] > hand[i+1] or hand[i+1] > hand[i+2] or (hand[i+2]-hand[i]) >= 1:
                temp = hand
                if draw[0] > hand[i] and hand[i+2] < draw[0]:
                    temp[i+1] = draw[0]
                    # middle swap
                elif draw[0] < hand[i+1] and hand[i+2] > draw[0]:
                    temp[i] = draw[0]
                    # first swap
                elif draw[0] > hand[i+2] and hand[i+1] < draw[0]:
                    # last swap
                    temp[i+2] = draw[0]
                else:
                    return False, hand
                return step_down(temp), temp
            else:
                continue
    else:
        return False, hand
    # look at first 3 without increase and see if can replace

# print(stratb(s,n,hand,draw))

def main(s, n, hand, draw):
    while len(draw) != 0 and step_down(hand) != 0:
        if step_down(hand) == 0 or len(draw) == 0:
            break
        else:     
            print(draw)
            if len(draw) != 0:
                last = 0
                # print(draw, 'dr')           
                # print(strata(s, n, hand, draw))
                tfa, handa = strata(s, n, hand, draw)
                tfb, handb = stratb(s,n,hand,draw)
                print(tfa, tfb, handa, handb)
                if tfa != False and tfb == False:
                    hand = handa
                    last = 'a'
                elif tfb != False and tfa == False:
                    hand = handb
                    last = 'b'
                elif tfa != False and tfb != False:
                    if tfa >= tfb:
                        hand = handa
                        last = 'a'
                    else:
                        hand = handb
                        last = 'b'
                else:
                    continue
                draw.pop(0)
            else:
                break    
        print(hand, last)
    return hand
  
print(main(s, n, hand, draw))