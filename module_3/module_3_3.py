def print_params(a=1, b="строка", c=True):
    print(F"a={a}, b= {b}, c = {c}")
print_params()
print_params(10)
print_params(10, 25)
print_params(10, 25, False)
print_params(b=25)
print_params(c=[1, 2, 3])


values_list = [42, "текст", False]
values_dict = {"a": 99, "b": "словарь строка", "c": True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [7, "отдельные параметры"]
print_params(*values_list_2, 42)

def append_to_list(item, list_my = None):
    if list_my is None:
        list_my = []
    list_my.append(item)
    print(list_my)
append_to_list(1)
append_to_list(2)
append_to_list(3, [5])