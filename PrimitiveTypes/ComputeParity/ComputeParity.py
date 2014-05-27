#Problem: Compute Parity

# Usage: Parity checks are used to detect single bit errors in data storage and communication

# Function

# Calculates the bit count
def bitCount(int_type):
    count = 0
    while(int_type):
        int_type &= int_type - 1
        count += 1
    return(count)

# Calculates the parity of an integer,
# Returning 0 if there are an even number of set bits, and -1 if there are an odd number
def computeParity(num):
    parity = 0
    while num:
        parity = ~parity
        num &= (num - 1)  # drops the lowest set bit of num
    return parity

# Main Program
input = 5
pValue = computeParity(input)

print("Parity for %d is %d" %(input, pValue))
print("Bitcount of %d is %d" %(input, bitCount(input)))

input = 8
pValue = computeParity(input)

print("Parity for %d is %d" %(input, pValue))
print("Bitcount of %d is %d" %(input, bitCount(input)))