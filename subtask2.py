def process_sequence():
    n = 0  
    s = 0  
    m = -1  

    print("Enter natural numbers one by one, and terminate with -1.")

    while True:
        x = int(input("Read x: "))
        if x == -1:
            break
        n += 1
        s += x
        if m == -1 or x < m:
            m = x
    if n == 0:
        m = -1
        a = -1
    else:
        a = s/n

    print(f"Count (n): {n}")
    print(f"Sum (s): {s}")
    print(f"Minimum (m): {m}")
    print(f"Mean (a): {a:.2f}")

process_sequence()