def count_words(count):
    book_split = count.split()
    word_count = len(book_split)
    return word_count

def count_characters(characters):
    character_dictionary = {}
    for char in characters:
        lower_char = char.lower()
        if lower_char in character_dictionary: 
            character_dictionary[lower_char] += 1
        else:
            character_dictionary[lower_char] = 1
    return character_dictionary

def sorted_characters(sorted):
    sorted_list = []
    for char, count in sorted.items():
        sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True , key=lambda item: item["num"])
    return sorted_list