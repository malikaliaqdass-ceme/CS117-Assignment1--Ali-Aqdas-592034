# B5: Bins measured 100 ohm resistors by tolerance until the user enters 0.
count_1_percent = 0
count_5_percent = 0
count_reject = 0

measured = float(input("Enter measured resistance (0 to stop): "))

while measured != 0:
    if 99.0 <= measured <= 101.0:
        count_1_percent = count_1_percent + 1
    elif 95.0 <= measured <= 105.0:
        count_5_percent = count_5_percent + 1
    else:
        count_reject = count_reject + 1
    measured = float(input("Enter measured resistance (0 to stop): "))

print("1% tolerance:", count_1_percent)
print("5% tolerance:", count_5_percent)
print("Reject:", count_reject)
