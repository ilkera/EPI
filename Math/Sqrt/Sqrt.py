# Problem: Find sqrt of a double number
# e.g. Sqrt(16) = 4

# Functions
def sqrt(number):
    if number < 0:
        return float('NaN')

    low = 0
    high = (number / 2) + 1
    precision = 0.00000001

    while high - low >= precision:
        mid = low + (high - low) / 2
        squared = mid * mid
        if squared == number:
            return mid
        elif squared > number:
            high = mid
        else:
            low = mid

    return low

# Main Program
print("Sqrt of %f is %.2f" %(16.0, sqrt(16.0)))
print("Sqrt of %f is %.2f" %(4.0, sqrt(4.0)))
print("Sqrt of %f is %.2f" %(1.0, sqrt(1.0)))
print("Sqrt of %f is %.2f" %(0.0, sqrt(0.0)))
print("Sqrt of %f is %.2f" %(2.0, sqrt(2.0)))
print("Sqrt of %f is %.2f" %(6.4, sqrt(6.4)))
print("Sqrt of %f is %.2f" %(-6.4, sqrt(-6.4)))