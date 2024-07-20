def migratory_birds(arr):
    from collections import Counter
    bird_counts = Counter(arr)
    return max(bird_counts, key=lambda x: (bird_counts[x], -x))

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 3]
    print(migratory_birds(arr))
