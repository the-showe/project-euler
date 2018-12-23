import string
from tools import run_euler

keys = [1, 2, 3, 4, 5, 6, 7, 8, 9]

units_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens_list = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens_list = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

units_dict = dict(zip(keys, units_list))
teens_dict = dict(zip(keys, teens_list))
tens_dict = dict(zip(keys, tens_list))


def write_number(n):
    digits = [int(d) for d in str(n)]

    unit = digits[-1]

    if unit == 0:
        unit_string = ''
    else:
        unit_string = units[unit - 1]
    full_string = unit_string

    if len(digits) > 1:
        ten = digits[-2]

        if ten == 0:
            ten_string = unit_string
            full_string = unit_string
        elif ten == 1 and unit > 0:
            ten_string = teens[unit - 1]
            full_string = ten_string
        else:
            ten_string = tens[ten - 1]
            full_string = '{0}-{1}'.format(ten_string,
                                           unit_string)

    if len(digits) > 2:
        hundred = digits[-3]

        if hundred == 0:
            full_string = ten_string
        else:
            full_string = '{0} hundred and {1}'.format(units[hundred - 1], full_string)

    if len(digits) > 3:
        thousand = digits[-4]

        full_string = '{0} thousand and {1}'.format(units[thousand - 1], full_string)

    if full_string.endswith(' and '):
        full_string = full_string.replace(' and ', '')

    if full_string.endswith('-'):
        full_string = full_string.replace('-', '')

    return full_string


def count_letters(s):
    letter_count = len([c for c in s if c in string.ascii_letters])
    return letter_count


@run_euler
def count_letters_used_up_to(n):
    written_numbers = [write_number(i) for i in range(1, n + 1)]
    letter_counts = [count_letters(s) for s in written_numbers]
    return sum(letter_counts)


count_letters_used_up_to(1000)
