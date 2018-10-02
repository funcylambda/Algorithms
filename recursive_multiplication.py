

def multiply(x, y):

    if x == 0 or y == 0:
        return 0
    if x == 1:
        return y
    if y == 1:
        return x

    return multiply(x - 1, y - 1) + x + y - 1


print(multiply(7, 5))
