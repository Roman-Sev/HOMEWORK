def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            result += item
        except TypeError:
            incorrect_data +=1
    return result, incorrect_data

def calculate_average(numbers):
    try:
        result, incorrect_data = personal_sum(numbers)
        return result / (len(numbers) - incorrect_data)
    except ZeroDivisionError:
        return 0
    except TypeError:
        print("В numbers записан некорректный тип данных")
        return None

print("Результат 1:", calculate_average([1, 2, 3, 4, 5]))
print("Результат 2:", calculate_average([1, 2, "строка", None, 3.0, "еще строка"]))
print("Результат 3:", calculate_average([]))
print("Результат 4:", calculate_average(42))
