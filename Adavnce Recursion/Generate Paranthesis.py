def solve(ind, balance, n, brackets, result):
    # If we've placed all 2*n brackets
    if ind == 2 * n:
        if balance == 0:
            result.append("".join(brackets))
        return

    # Option 1: place '(' if we still can
    if balance < n:  # can't open more than n
        brackets[ind] = "("
        solve(ind + 1, balance + 1, n, brackets, result)

    # Option 2: place ')' if it won't break balance
    if balance > 0:
        brackets[ind] = ")"
        solve(ind + 1, balance - 1, n, brackets, result)


def generate_parentheses(n):
    brackets = [""] * (2 * n)
    result = []
    solve(0, 0, n, brackets, result)
    return result


# Example usage
n=int(input("Enter the number :"))
print(generate_parentheses(n))
