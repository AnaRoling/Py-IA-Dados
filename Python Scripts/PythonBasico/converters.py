def lbs_to_kg(weigth):
    return weigth * 0.45


def kg_to_lbs(weigth):
    return weigth/0.45


def find_max(numbers):
    maximum= numbers[0]
    for number in numbers:
       if number> maximum:
        maximum = number