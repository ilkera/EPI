# Problem: IsPalindrome - Determine if a given string is palindrome
# e.g. racecar - yes, abba - yes, abc - no

# Function
def isPalindrome(str):
    if not str:
        return False

    if len(str) == 1:
        return True

    str = str.lower()  # ignore case-sensitivity
    left = 0
    right = len(str) - 1

    while left < right:

        if not str[left].isalnum():
            left += 1
            continue
        if not str[right].isalnum():
            right -= 1
            continue

        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True

# Main Program

# Valid cases
print("Testing %s is : %r" %("racecar", isPalindrome("racecar")))
print("Testing %s is : %r" %("abba", isPalindrome("abba")))
print("Testing %s is : %r" %("a", isPalindrome("a")))
print("Testing %s is : %r" %("abcba", isPalindrome("abcba")))

# case for uppercase
print("Testing %s is : %r" %("raceCar", isPalindrome("raceCar")))

# case for whitespace and punctuation
print("Testing %s is : %r" %("Madam I'm Adam", isPalindrome("Madam I'm Adam")))

# invalid cases
print("Testing %s is : %r" %("ab", isPalindrome("ab")))
print("Testing %s is : %r" %("abc", isPalindrome("abc")))
print("Testing %s is : %r" %("racecarr", isPalindrome("racecarr")))




