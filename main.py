card = input(' введите номер карты ')
def card_number(card):
    return '*' * len(card[:-4]) + card[ -4:]
print(card_number)
