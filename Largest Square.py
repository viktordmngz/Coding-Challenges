def sum(a, b, c):
    # Write code here
    n = [a, b, c]
    n_max = max(a, b, c)
    n.sort()
    n.pop(-1)
    n.append(n_max**2)
    return n[0]+n[1]+n[2]

# print(sum(1,5,5))
