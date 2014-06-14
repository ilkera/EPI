# Problem: Implement GCD(a,b) function

def gcd(first, second):
    if second == 0:
        return first

    return gcd(second, first % second)

def gcd_iterative(first, second):
    while second != 0:
        temp = second
        second = first % second
        first = temp

    return first

# Main program

print(gcd(54,24))
print(gcd_iterative(54,24))