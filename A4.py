# A4: Reads two bits and prints the output of AND, OR and XOR gates.
a = int(input("Enter A: "))
b = int(input("Enter B: "))

if (a != 0 and a != 1) or (b != 0 and b != 1):
    print("Bits must be 0 or 1")
else:
    if a == 1 and b == 1:
        and_out = 1
    else:
        and_out = 0

    if a == 1 or b == 1:
        or_out = 1
    else:
        or_out = 0

    if a != b:
        xor_out = 1
    else:
        xor_out = 0

    print("AND =", and_out)
    print("OR =", or_out)
    print("XOR =", xor_out)
