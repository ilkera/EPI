# Problem: Implement Strstr function
# (Search for a substring and return the first occurence index)

# Function
def strStr(str, target):
    if not str or not target:
        return -1

    if len(str) < len(target):
        return -1

    current_str= 0

    while current_str < len(str):
        if str[current_str] != target[0]:
            current_str += 1
            continue

        temp, current_target = current_str + 1, 1
        while temp < len(str) and current_target < len(target) and str[temp] == target[current_target]:
            temp +=1
            current_target +=1

        if current_target == len(target):
            return current_str

        current_str += 1

    return -1

# Main program

# Valid
print(strStr("This is a test", "is"))
print(strStr("This is a test", "test"))
print(strStr("This is a test", "tes"))
print(strStr("This is a test", "This"))
print(strStr("This is a test", "a"))

# Invalid
print(strStr("This is a test", "apple"))
print(strStr("This is a test", "teste"))
print(strStr("This is a test", "tesa"))
print(strStr("This is a test", "Tha"))
print(strStr("This is a test", "Thiss"))