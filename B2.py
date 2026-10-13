# B2: Reads n resistors connected in series and prints the total resistance.
count = int(input("How many resistors? "))
total_resistance = 0

for i in range(1, count + 1):
    value = float(input("Enter R" + str(i) + ": "))
    total_resistance = total_resistance + value

print("Total resistance =", total_resistance, "ohm")
