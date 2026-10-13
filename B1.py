# B1: Prints the current through a fixed 10 ohm resistor for supplies of 1 V to 10 V.
resistance = 10

for voltage in range(1, 11):
    current = voltage / resistance
    print("V =", voltage, "V, I =", current, "A")
