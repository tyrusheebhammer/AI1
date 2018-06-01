import random
import numpy as np
dich = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, "Q": 12, 'K': 13, 'A': 14}
player_1_d = []
player_2_d = []
player_1_temp = []
player_2_temp = []
player_1_point_density = []
player_2_point_density = []

fmt = '{:<8} {:<4} {:<4} {:<4} {:<4}'


def main():
    deck = ['A'] * 4 + ['Q'] * 4 + ['J'] * 4 + ['K'] * 4 + ['2'] * 4 + ['3'] * 4 + ['4'] * 4 + ['5'] * 4 + ['6'] * 4 + [
        '7'] * 4 + ['8'] * 4 + ['9'] * 4 + ['10'] * 4
    print(deck)
    round = 0
    for _ in range(10):
        random.shuffle(deck)

    while len(deck) > 0:
        player_1_d.append(deck.pop())
        player_2_d.append(deck.pop())

    player_1_point_density.append(calcptdens(player_1_d))
    player_2_point_density.append(calcptdens(player_2_d))
    while True:
        warchest = []
        if len(player_2_d) == 0 or len(player_1_d) == 0:
            reset()

            if len(player_2_d) == 0 or len(player_1_d) == 0:
                break
        while True:
            player_1_card = player_1_d.pop()
            player_2_card = player_2_d.pop()
            round += 1
            print("----------")
            print(fmt.format("Round:", round, '', '', ''))
            print(fmt.format("Hand:", len(player_1_d), "-", len(player_2_d), ''))
            print(fmt.format("Discard:", len(player_1_temp), "-", len(player_2_temp), ''))
            print(fmt.format("Aces:", player_1_d.count('A') + player_1_temp.count('A'), "-",
                             player_2_temp.count('A') + player_2_d.count('A'), ''))
            print(fmt.format("Density:", calcptdens(player_1_d, player_1_temp), '-',
                             calcptdens(player_2_d, player_2_temp), ''))
            print(fmt.format('', player_1_card, 'v', player_2_card, ''))
            print()

            p1v = dich[player_1_card]
            p2v = dich[player_2_card]
            if p1v > p2v:
                player_1_temp.append(player_1_card)
                player_1_temp.append(player_2_card)
                player_1_temp.extend(warchest)
                break
            elif p1v < p2v:
                player_2_temp.append(player_1_card)
                player_2_temp.append(player_2_card)
                player_2_temp.extend(warchest)
                break
            else:
                warchest.append(player_1_card)
                warchest.append(player_2_card)
                if len(player_2_d) == 0 or len(player_1_d) == 0:
                    reset()
                    if len(player_2_d) == 0 or len(player_1_d) == 0:
                        break

    if len(player_1_d) == 0:
        print("player 2 wins!")
    else:
        print("player 1 wins!")


def reset():
    player_1_d.extend(player_1_temp)
    player_2_d.extend(player_2_temp)

    if len(player_1_d) > 0:
        player_1_point_density.append(calcptdens(player_1_d))
    if len(player_2_d) > 0:
        player_2_point_density.append(calcptdens(player_2_d))
    player_1_temp.clear()
    player_2_temp.clear()
    for _ in range(10):
        random.shuffle(player_1_d)
        random.shuffle(player_2_d)
    player_1_point_density.append(calcptdens(player_1_d))
    player_2_point_density.append(calcptdens(player_2_d))


def calcptdens(list1, list2=[]):
    total = 0
    for c in list1:
        total += dich[c]
    for c in list2:
        total += dich[c]
    if(len(list2) + len(list1)) == 0:
        return 0
    return np.round(total / (len(list2) + len(list1)),2)


if __name__ == '__main__':
    main()
