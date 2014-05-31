# Problem : IsAnagram
# e.g. "abc" is anagram of "cab"

# Functions
# IsAnagram via Sort
def isAnagram_v1(first, second):
    if not first and not second:
        return False

    if len(first) != len(second):
        return False

    return first == ''.join(sorted(second))

def isAnagram_v2(first, second):
    if not first and not second:
        return False

    if len(first) != len(second):
        return False

    seen = {}

    for ch in first:
        if ch in seen:
           seen[ch] += 1
        else:
            seen[ch] = 1

    for ch in second:
        if not ch in seen:
            return False
        else:
            seen[ch] -= 1
            if seen[ch] == 0:
                seen.pop(ch)

    return len(seen) == 0



# Main Program
print("\nValid cases v1")
print("%s" %isAnagram_v1("abc","cab"))
print("%s" %isAnagram_v1("a","a"))
print("%s" %isAnagram_v1("abc","abc"))
print("%s" %isAnagram_v1("aa","aa"))

print("\nInvalid cases v1")
print("%s" %isAnagram_v1("a","b"))
print("%s" %isAnagram_v1("ab","b"))
print("%s" %isAnagram_v1("abc","abb"))
print("%s" %isAnagram_v1(None,None))
print("%s" %isAnagram_v1("",""))


print("\nValid cases v2")
print("%s" %isAnagram_v2("abc","cab"))
print("%s" %isAnagram_v2("a","a"))
print("%s" %isAnagram_v2("abc","abc"))
print("%s" %isAnagram_v2("aa","aa"))

print("\nInvalid cases v2")
print("%s" %isAnagram_v2("a","b"))
print("%s" %isAnagram_v2("ab","b"))
print("%s" %isAnagram_v2("aba","abc"))
print("%s" %isAnagram_v2(None,None))
print("%s" %isAnagram_v2("",""))