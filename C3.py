# C3: Function converting a positive decimal number to a binary string by repeated division by 2.
def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary


print("decimal_to_binary(10) ->", decimal_to_binary(10))
print("decimal_to_binary(25) ->", decimal_to_binary(25))
