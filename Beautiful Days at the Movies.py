def beautiful_days(i, j, k):
    beautiful_days_count = 0
    for day in range(i, j + 1):
        reversed_day = int(str(day)[::-1])
        if abs(day - reversed_day) % k == 0:
            beautiful_days_count += 1
    return beautiful_days_count

if __name__ == "__main__":
    i, j, k = 20, 23, 6
    print(beautiful_days(i, j, k))
