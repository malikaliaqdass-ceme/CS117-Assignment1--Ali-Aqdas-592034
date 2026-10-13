# A1: Reads voltage and resistance, computes current (Ohm's law) and checks if the 2 A fuse will blow.
voltage = float(input("Enter voltage (V): "))
resistance = float(input("Enter resistance (ohm): "))

if resistance <= 0:
    print("Invalid resistance")
else:
    current = voltage / resistance
    print("Current =", current, "A")
    if current > 2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")
