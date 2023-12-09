from functools import cmp_to_key
from collections import defaultdict


with open('input.txt', 'r') as file:
    content = [line.strip() for line in file.readlines()]


CARDS = "J23456789TQKA"

content = [line.split(" ") for line in content]



def check_type_pack_of_cards(pack: str) -> int:
    counts = defaultdict(int)
    print(counts)
    jokers = 0

    for x in pack:
        if x == "J":
            jokers += 1
        else:
            counts[x] += 1

    amounts = sorted(counts.values())

    if jokers >= 5 or amounts[-1] + jokers >= 5:
        return 5
    if jokers >= 4 or amounts[-1] + jokers >= 4:
        return 4

    if amounts[-1] + jokers >= 3:
        rem_jokers = amounts[-1] + jokers - 3
        if len(amounts) >= 2 and amounts[-2] + rem_jokers >= 2 or rem_jokers >= 2:
            return 3
        return 2

    if amounts[-1] + jokers >= 2:
        rem_jokers = amounts[-1] + jokers - 2
        if len(amounts) >= 2 and amounts[-2] + rem_jokers >= 2 or rem_jokers >= 2:
            return 1
        return 0

    return -1



def check_cards(card1: str, card2: str) -> str:
    if CARDS.index(card1) > CARDS.index(card2):
        return card1

    if CARDS.index(card1) < CARDS.index(card2):
        return card2

    return ''


def part_two():
    ranks = [0] * len(content)

    for i in range(len(content)):
        current_rank = 1
        current_card = content[i][0]
        
        for j in range(len(content)):
            if i == j: continue

            second_card = content[j][0]

            type_of_first_pack = check_type_pack_of_cards(current_card)
            type_of_second_pack = check_type_pack_of_cards(second_card)

            if type_of_first_pack > type_of_second_pack:
                current_rank += 1

            if type_of_first_pack == type_of_second_pack:
                for k in range(len(current_card)):
                        if check_cards(current_card[k], second_card[k]) == current_card[k]:
                            current_rank += 1
                            break
                        if check_cards(current_card[k], second_card[k]) == second_card[k]:
                            break

        ranks[i] = current_rank


    result = 0
    for i in range(len(content)):
        bid_amount = int(content[i][1])
        result += bid_amount * ranks[i]

    print(result)

part_two()
