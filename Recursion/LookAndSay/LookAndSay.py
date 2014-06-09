# Problem: Look and Say
# 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211
# Given an integer n, generate the nth sequence

# Functions
def lookAndSay(current_sequence, index, end):
    if index == end - 1:
        return current_sequence

    str = current_sequence[index]
    same_digit_count = 1
    current_index = 1
    sequence = ""

    while current_index < len(str):
        if str[current_index] != str[current_index-1]:
            sequence = sequence + "{0}{1}".format(same_digit_count, str[current_index-1])
            same_digit_count = 1
        elif str[current_index] == str[current_index-1]:
            same_digit_count += 1
        current_index += 1

    sequence = sequence + "{0}{1}".format(same_digit_count, str[-1])
    current_sequence.append(sequence)

    return lookAndSay(current_sequence, index + 1, end)

# Main program
result = lookAndSay(["1"], 0, 7)
print(result)
