def convert_to_64_bit(number):
    min64b = 76561197960265728
    if number < min64b:
        return number + min64b
    return number
