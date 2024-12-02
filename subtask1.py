def largest_square_number(n):
    q = 0
    while (q + 1)**2 <= n:
        q += 1
    return q**2

# Example
n = 24
q = largest_square_number(n)
print(f"The largest square number less than or equal to {n} is {q}.")
