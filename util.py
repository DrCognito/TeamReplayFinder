def convert_to_64_bit(number):
    min64b = 76561197960265728
    if not is_64bit(number):
        return number + min64b
    return number

def convert_to_32_bit(number):
    min64b = 76561197960265728
    if is_64bit(number):
        return number - 76561197960265728
    return number


def is_64bit(number):
    min64b = 76561197960265728
    return (number >= min64b)