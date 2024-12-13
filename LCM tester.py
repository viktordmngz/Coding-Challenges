def lcm(a, b):
    # Write code here
    if a%b == 0 or b%a == 0:
        return max(a,b)
    for i in range(1, 1000):
        if a*i%b == 0:
            return a*i

# print(lcm(6, 10))
