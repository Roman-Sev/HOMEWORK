import string

class WordsFinder:
    def __init__(self,*file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name,'r',encoding='utf-8') as file:
                    content = file.read().lower()
                    for char in [',','.','=','!','?',';',':',' - ']:
                        content = content.replace(char," ")
                        words = content.split()
                        all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []
                return all_words

 #          print(f"Файл{file_name} не найден.")
    def find(self,word):
        word = word.lower()
        result = {}
        for name, words in self.get_all_words().items():
            try:
                position = words.index(word)
            except ValueError:
                position = -1
                result[name] = position
            return result

    def count(self,word):
        word = word.lower()
        result = {}
        for name, words in self.get_all_words().items():
            result[name] = words.count(word)
            return result

finder = WordsFinder('file1.txt','file2.txt','file3.txt')
found_positions = finder.find('word1')
print(found_positions)
print(finder.get_all_words())
print(finder.find('python'))
print(finder.count('is'))

found_positions = WordsFinder.find('word1','word2')
print("Позиции первого вхождения 'word1':")
print(found_positions)

word_count = WordsFinder.count('word1')
print("Количесвто вхождений 'word1':")
print(word_count)








