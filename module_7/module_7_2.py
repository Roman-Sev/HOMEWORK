def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for i, string in enumerate(strings, start=1):
            byte_position = file.tell()
            file.write(string + '\n')
            strings_positions[(i, byte_position)] = string
    return strings_positions


strings = ["Text for tell.", "Используйте кодировку utf-8"]
file_name = 'example.txt'
positions = custom_write(file_name, strings)
print(positions)
