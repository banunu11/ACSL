
row = list(input())
for ro in range(len(row)):
    while len(row) != 4:
        row.append([0])
    row[ro] = list(map(int, row[ro]))
hand = input().split(' ')
for ha in range(len(hand)):
    if len(hand[ha]) == 1:
        hand[ha] = hand[ha] + '0'
    hand[ha] = list(map(int, hand[ha]))
draw = input().split(' ')
for dr in range(len(draw)):
    if len(draw[dr]) == 1:
        draw[dr] = draw[dr] + '0'
    draw[dr] = list(map(int, draw[dr]))

def is_valid_placement(tile, row):
    # Check if the tile can be placed at the right end of the row
    if type(row[-1]) == int: 
        # print(tile[0], tile[1], 'tile')
        # print(row[-1], 'rpw=1')
        return tile[0] == row[-1] or tile[1] == row[-1]
    elif type(row[-1]) == list:
        return tile[0] == row[-1][1] or tile[1] == row[-1][1]

def place_tile(tile, row):
    # Place the tile at the right end of the row
    if type(row[-1]) == int:     
        if tile[0] == row[-1]:
            row.append([tile[0], tile[1]])        
        elif tile[1] == row[-1]:
            row.append([tile[1], tile[0]])
    elif type(row[-1]) == list:
        if tile[0] == row[-1][1]:
            row.append([tile[0], tile[1]])        
        elif tile[1] == row[-1][1]:
            row.append([tile[1], tile[0]])

def sum_digits(numbers):
    # Calculate the sum of single-digit numbers
    return sum([num for sublist in numbers for num in sublist])

while True:
    placed_tile = False  # Flag to check if a tile is placed in the current iteration
    for tile in hand:
        for w in range(len(row)):
            # Check if the tile can be placed at the right end of the row
            if is_valid_placement(tile, row[w]):
                # print(tile, 'tile')
                place_tile(tile, row[w])
                print('row', row)
                hand.remove(tile)  # Remove the placed tile from the hand
                print(hand, 'hand')
                print('draw', draw)
                placed_tile = True
                break
        if placed_tile:
            break
    if not placed_tile:
        # If no tiles were placed in the current iteration, draw new tiles until a match is found or draw pile is empty
        if not draw:
            break  # No more tiles to draw, exit the loop

        hand.append(draw.pop(0))

# Calculate the sum of remaining digits in the hand
remaining_sum = sum_digits(hand)
print(remaining_sum)



