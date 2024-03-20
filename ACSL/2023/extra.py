def ideal_slot_strategy(rack, draw_card, n, s):
    interval_size = n // s if n % s == 0 else n // s + 1
    slot = (draw_card - 1) // interval_size + 1
    ideal_min = (slot - 1) * interval_size + 1
    ideal_max = min(slot * interval_size, n)
    for i in range(len(rack)):
        if rack[i] < ideal_min or rack[i] > ideal_max:
            return i
    return -1

def ascending_order_strategy(rack, draw_card):
    for i in range(len(rack) - 2):
        if rack[i] > rack[i + 1] > rack[i + 2]:
            if draw_card > rack[i + 1]:
                return i + 3
    return -1

def rack_o_game(s, n, initial_rack, draw_pile):
    rack = initial_rack[:]
    while True:
        if all(rack[i] <= rack[i + 1] for i in range(len(rack) - 1)):
            break  # Rack is in ascending order
        if not draw_pile:
            break  # Draw pile is empty

        draw_card = draw_pile.pop(0)
        print(rack)
        # Apply Strategy A (Ideal Slot)
        ideal_slot_index = ideal_slot_strategy(rack, draw_card, n, s)
        if ideal_slot_index != -1:
            rack[ideal_slot_index] = draw_card
            continue

        # Apply Strategy B (Ascending Order)
        ascending_order_index = ascending_order_strategy(rack, draw_card)
        if ascending_order_index != -1:
            rack[ascending_order_index - 1] = draw_card
        print(rack)

    return ' '.join(map(str, rack))

# Example input
# s, n = map(int, input().split())
# initial_rack = list(map(int, input().split()))
# draw_pile = list(map(int, input().split()))

s, n = 9, 70
hand = [40, 35, 30, 56, 32, 58, 44, 17, 45]
draw = [31, 37, 10, 28, 21, 62, 7, 64, 16, 12]

# Output the final rack configuration
# print(rack_o_game(s, n, initial_rack, draw_pile))
print(rack_o_game(s, n, hand, draw))

