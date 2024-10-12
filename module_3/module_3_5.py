def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        remaining_product = get_multiplied_digits(int(str_number[1:]))
        if remaining_product == 0:
            return first
        else:
            return first * remaining_product
    else:
        return first
result = get_multiplied_digits (123405)
print(result)
