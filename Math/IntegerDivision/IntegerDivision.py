# Problem: Integer Division

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("dividend is zero")
    if dividend == 0:
        return 0

    is_positive = True
    if divisor < 0:
        divisor = -divisor
        is_positive = not is_positive

    if dividend < 0:
        dividend = -dividend
        is_positive = not is_positive

    step = divisor
    stepRes = 1
    result = 0

    # Enlarge the divisor as long as it is <= dividend
    while (step << 1) <= dividend:
        step = step << 1
        stepRes = stepRes << 1

    while step >= divisor:
        while dividend >= step:
            dividend -= step
            result += stepRes
        # if current step is too large, try smaller step (Divisor)
        step = step >> 1
        stepRes = stepRes >> 1

    if is_positive:
        return result
    else:
        return -result

# Main program
print(divide(6, 3))   # positive
print(divide(12, 4))  # positive
print(divide(3, 1))  # positive
print(divide(5, 2))  # non-divisible
print(divide(1, 4)) # divisor > dividend
print(divide(1, 1))
print(divide(5, 5))  # same number
print(divide(0, 1))  # zero
print(divide(-6, -3))  # negative
print(divide(-6, 3))  # negative
print(divide(6, -3))  # negative
print(divide(25000,1)) #  big number
print(divide(512, 2))