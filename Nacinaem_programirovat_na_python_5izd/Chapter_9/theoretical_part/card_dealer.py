# эмитациия раздачи карт из колоды

# emitting the distribution of cards from the deck

import random


# создаем словарь в котором хранится колода карт пара карта:очки_карты
def create_deck():
    deck = {'2 червей': 2, '3 червей': 3, '4 червей': 4, '5 червей': 5, '6 червей': 6,
            '7 червей': 7, '8 червей': 8, '9 червей': 9, '10 червей': 10, 'Валет червей': 10,
            'Дама червей': 10, 'Король червей': 10, 'Туз червей': 1,

            '2 бубей': 2, '3 бубей': 3, '4 бубей': 4, '5 бубей': 5, '6 бубей': 6,
            '7 бубей': 7, '8 бубей': 8, '9 бубей': 9, '10 бубей': 10, 'Валет бубей': 10,
            'Дама бубей': 10, 'Король бубей': 10, 'Туз бубей': 1,

            '2 треф': 2, '3 треф': 3, '4 треф': 4, '5 треф': 5, '6 треф': 6,
            '7 треф': 7, '8 треф': 8, '9 треф': 9, '10 треф': 10, 'Валет треф': 10,
            'Дама треф': 10, 'Король треф': 10, 'Туз треф': 1,

            '2 пик': 2, '3 пик': 3, '4 пик': 4, '5 пик': 5, '6 пик': 6,
            '7 пик': 7, '8 пик': 8, '9 пик': 9, '10 пик': 10, 'Валет пик': 10,
            'Дама пик': 10, 'Король пик': 10, 'Туз пик': 1,
            }
    return deck


def deal_caeds(desk, number):
    hand_value = 0

    # если пользователь запросил карт больше чем карт в колоде, сдаем сколько есть в колоде
    if number > len(desk): number = len(desk)
    print(f'[#] > Вам сдали:')

    # мой варант
    hand_cards = random.choices(list(desk), k=number)  # используя choices мы получаем сразу
    for card in hand_cards:                            # набор карт в котором нет повторов
        print(f'[#] > {card}')
        hand_value += desk[card]

    # код приведенный в книге
    # for cout in range(number):
    #     card = random.choice(list(desk))        # в решении из учебника есть один недостаток,
    #     print(f'[#] > {card}')                  # есть шанс на то, что будут сданы одинаковые
    #     hand_value += desk[card]                # карты, чего в реальной жизни быть не может

    print(f'[#] > Величина карт в руках: {hand_value}')


def main():
    deck = create_deck()
    num_cards = ' '
    while not num_cards.isdigit():  # добавил проверку на то что вводится целое число
        num_cards = input(f'[#] > Сколько карт раздать?\n'
                          f'[#] > > '
                          )
    deal_caeds(deck, int(num_cards))


if __name__ == '__main__':
    main()
