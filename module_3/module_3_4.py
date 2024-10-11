def single_root_words(root_word, *other_words):
    root_word_lower = root_word.lower()
    same_words = []
    for word in other_words:
        word_lower = word.lower()
        if root_word_lower in word_lower or word_lower in root_word_lower:
            return same_words


result = single_root_words("able", "Disablement", "Table", "capable", "label", "Able")
print(result)
