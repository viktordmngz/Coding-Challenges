def digit(n):
    # Write code here
    a = 1
    numbers = ""
    while len(numbers) < n:
        for i in range(1,a):
            numbers += str(i)
        a += 1
    return numbers[n-1]
