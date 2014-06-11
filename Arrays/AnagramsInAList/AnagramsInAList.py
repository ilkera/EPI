# Problem: Find all anagrams in a list of words

# Function
def sorted_word(word):
    if not word:
        return word

    sorted_chars = sorted(word)

    return "".join(sorted_chars)

def getAllAnagrams(array, str):
    if not array:
        return []

    result = []

    for same_length_word in (word for word in array if len(word) == len(str)):
        if sorted_word(same_length_word) == sorted_word(str):
            result.append(same_length_word)

    return result


# Main Program

list = ["abc", "cab", "ded", "book", "bac", "cook", "yes"]
print(getAllAnagrams(list, "cba"))
