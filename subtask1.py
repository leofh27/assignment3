#7.3 flowchart in python


def largest_square(n):
    q = 0
    while (q+1)* 2 <= n:
        q+=1
    return q * 2

# Example usage
n = 37
result = largest_square(n)
print(f"The largest square number less than or equal to {n} is {result}.")

# it looks like I learned how to use git today