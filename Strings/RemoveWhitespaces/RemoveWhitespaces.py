# Problem: Remove whitespaces in a string
# e.g. "Test is good  " => "Testisgood"

def removeSpaces(str):
    if not str:
        return None

    list_str = list(str)
    index_last_copy, current = 0, 0

    while current < len(list_str):
        if list_str[current] == " ":
            current += 1
            continue

        list_str[index_last_copy] = list_str[current]
        index_last_copy += 1
        current += 1

    return "".join(list_str[:index_last_copy])

# Main program
str = "Test is good"
print("Str:|%s| Removed:|%s|" %("Test is good  ", removeSpaces("Test is good  ")))
print("Str:|%s| Removed:|%s|" %("   Test  ", removeSpaces("   Test  ")))
print("Str:|%s| Removed:|%s|" %("  Test", removeSpaces("  Test")))
print("Str:|%s| Removed:|%s|" %("Test     ", removeSpaces("Test     ")))
print("Str:|%s| Removed:|%s|" %("T", removeSpaces("T")))
print("Str:|%s| Removed:|%s|" %(" ", removeSpaces(" ")))


