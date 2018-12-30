import string
from tools import run_euler, DigitalString

UNITS = ('one',
         'two',
         'three',
         'four',
         'five',
         'six',
         'seven',
         'eight',
         'nine')

TEENS = ('eleven',
         'twelve',
         'thirteen',
         'fourteen',
         'fifteen',
         'sixteen',
         'seventeen',
         'eighteen',
         'nineteen')

TENS = ('ten',
        'twenty',
        'thirty',
        'forty',
        'fifty',
        'sixty',
        'seventy',
        'eighty',
        'ninety')


def write_ten_part(digital_string, number_strings):

    # Assign last two digits of digital_string
    unit_digit = digital_string[-1]

    if len(digital_string) > 1:
        ten_digit = digital_string[-2]
    else:
        ten_digit = '0'

    if unit_digit == '0' and ten_digit == '0':
        return ''
    elif unit_digit == '0':
        return number_strings['tens'][ten_digit]
    elif ten_digit == '0':
        return number_strings['units'][unit_digit]
    elif ten_digit == '1':
        return number_strings['teens'][unit_digit]
    else:
        ten_string = number_strings['tens'][ten_digit]
        unit_string = number_strings['units'][unit_digit]
        return '{ten_string}-{unit_string}'.format(ten_string=ten_string,
                                                   unit_string=unit_string)


def write_hundred_part(digital_string, number_strings):
    if len(digital_string) < 3:
        raise ValueError(
            'Digital strings with less than 3 characters '
            'cannot have a hundred part.'
        )

    hundred_digit = digital_string[-3]

    if hundred_digit == '0':
        return ''

    hundred_unit_string = number_strings['units'][hundred_digit]

    return '{hundred_unit_string} hundred'.format(
        hundred_unit_string=hundred_unit_string)


def write_thousand_part(digital_string, number_strings):
    if len(digital_string) < 4:
        raise ValueError(
            'Digital strings with less than 3 characters '
            'cannot have a thousand part.'
        )

    thousand_digit = digital_string[-4]

    if thousand_digit == '0':
        return ''

    thousand_unit_string = number_strings['units'][thousand_digit]

    return '{thousand_unit_string} thousand'.format(
        thousand_unit_string=thousand_unit_string)


def write_number(n):
    keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    number_strings = {
        'units': dict(zip(keys, UNITS)),
        'teens': dict(zip(keys, TEENS)),
        'tens': dict(zip(keys, TENS))
    }

    if n > 9999:
        raise ValueError('Solution only functions up to four digits.')

    digital_string = DigitalString(n)

    ten_part = write_ten_part(digital_string, number_strings)

    if len(digital_string) > 2:
        hundred_part = write_hundred_part(digital_string, number_strings)
    else:
        hundred_part = ''

    if len(digital_string) > 3:
        thousand_part = write_thousand_part(digital_string, number_strings)
    else:
        thousand_part = ''

    backward_string_parts = [ten_part]

    if ten_part and (hundred_part or thousand_part):
        backward_string_parts.append('and')

    if hundred_part:
        backward_string_parts.append(hundred_part)

    if thousand_part:
        backward_string_parts.append(thousand_part)

    return ' '.join(backward_string_parts[::-1])


def count_letters(s):
    letter_count = len([c for c in s if c in string.ascii_letters])
    return letter_count


@run_euler
def count_letters_used_up_to(n):
    written_numbers = [write_number(i) for i in range(1, n + 1)]
    letter_counts = [count_letters(s) for s in written_numbers]
    return sum(letter_counts)


count_letters_used_up_to(1000)
