def solve(index, flag, numbers, result):
    if index >= len(numbers):
        result.append("".join(numbers))   # join without spaces
        return

    # Place '0' always
    numbers[index] = "0"
    solve(index + 1, True, numbers, result)

    # Place '1' only if previous was '0' (flag == True)
    if flag:
        numbers[index] = "1"
        solve(index + 1, False, numbers, result)


def generateBinaryStrings(n):
    numbers = ["0"] * n   # initialize with strings
    result = []
    solve(0, True, numbers, result)
    return result


# --- User Input ---
n = int(input("Enter the number: "))
print("Unique combinations are:")
print(generateBinaryStrings(n))
