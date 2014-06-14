# Problem: Least Common Multiple
# e.g LCM(4,6) = 12
# Solution = LCM(x,y) = |x * y| / gcd(x,y)

def gcd(first, second):
    if second == 0:
        return first

    return gcd(second, first % second)

def lcm(first, second):
    if first == 0 or second == 0:
        return 0

    return int(abs(first * second) / gcd(first, second))

# MAIN PROGRAM
print(lcm(4,6))
print(lcm(3,5))
