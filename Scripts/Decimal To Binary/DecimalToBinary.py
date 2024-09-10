

def DecToBin(value, startBit=32, endBits = 32):
    # Split into integer and fraction
    integer_part = int(value)
    fraction_part = value - integer_part

    # Convert before the Dot
    bitString = ""
    if integer_part == 0:
        bitString = "0"
    else:
        while integer_part > 0:
            bitString = str(integer_part % 2) + bitString
            integer_part //= 2

    # Ensure the bit string is padded to the desired length
    bitString = bitString.zfill(startBit)

    # Add decimal point before converting fractional part
    bitString += "."

    # Convert After the Dot
    power_of_two = 0.5
    num_bits = endBits
    while num_bits > 0 and fraction_part > 0:
        if fraction_part >= power_of_two:
            bitString += '1'
            fraction_part -= power_of_two
        else:
            bitString += '0'
        power_of_two /= 2
        num_bits -= 1

    return bitString

# Testing the function with examples
print(DecToBin(0.375, 0))  # Output should focus on fractional part only
print(DecToBin(0.1, 0))    # Output should focus on fractional part only
