def angry_professor(k, a):
    on_time = sum(1 for time in a if time <= 0)
    return "YES" if on_time < k else "NO"

if __name__ == "__main__":
    k = 3
    a = [-1, -3, 4, 2]
    print(angry_professor(k, a))
