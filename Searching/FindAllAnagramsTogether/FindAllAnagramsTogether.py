# Problem: Print all Anagrams together
# Given an array of words, print all anagrams together.
# For example, if the given array is {“cat”, “dog”, “tac”, “god”, “act”},
# then output may be “cat tac act dog god”.

def groupAnagrams(anagrams):
    if not anagrams:
        return []

    anagram_table = {}

    for anagram in anagrams:
        sorted_anagram = "".join(sorted(anagram))
        if not sorted_anagram in anagram_table:
            anagram_table[sorted_anagram] = [anagram]
        else:
            anagram_table[sorted_anagram].append(anagram)

    return list(anagram_table.values())

# Main program
anagram_list = ["cat", "dog", "tac", "god", "act"]
print(groupAnagrams(anagram_list))

