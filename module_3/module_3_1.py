calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()
def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in [item.lower() for item in list_to_search]
info = string_info("Hello World")
contains = is_contains("hello", ["Hi", "Hello", "Greetings"])
print("string_info result: ", info)
print("is_contains result: ", contains)
print("Total calls: ", calls)

