
def create_list(n):
    l = []
    while n != 0:
        l.append(n)
        n = n - 1
        create_list(n)
    return list(reversed(l))


print(create_list(5))




