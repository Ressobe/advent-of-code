with open('sample.txt', 'r') as file:
    content = [line.strip() for line in file.readlines()]


CARDS = "23456789TJQKA"
content = [line.split(" ") for line in content]


def remove_first_occurrence_by_value(input_dict, value_to_remove):
    for key, value in input_dict.items():
        if value == value_to_remove:
            del input_dict[key]
            break


def check_type_pack_of_cards(pack: str) -> int:
    cards_appear = { c: 0 for c in CARDS}
    for p in pack:
        cards_appear[p] += 1

    max_appear = max(cards_appear.values())

    if max_appear == 5:
        return 5
    if max_appear == 4:
        return 4
    if max_appear == 1:
        return -1
    if max_appear == 3:
        remove_first_occurrence_by_value(cards_appear, 3)
        max_appear = max(cards_appear.values())

        if max_appear == 2:
            return 3                        

        return 2
    if max_appear == 2:
        remove_first_occurrence_by_value(cards_appear, 2)
        max_appear = max(cards_appear.values())
        if max_appear == 2:
            return 1

    return 0


def check_cards(card1: str, card2: str) -> str:
    if CARDS.index(card1) > CARDS.index(card2):
        return card1

    if CARDS.index(card1) < CARDS.index(card2):
        return card2

    return ''


def part_one():
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


part_one()
