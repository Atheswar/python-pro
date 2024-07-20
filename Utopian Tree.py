def utopian_tree(n):
    height = 1
    for i in range(1, n + 1):
        if i % 2 == 0:
            height += 1
        else:
            height *= 2
    return height

if __name__ == "__main__":
    n = 5
    print(utopian_tree(n))
