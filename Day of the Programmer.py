def day_of_programmer(year):
    if year == 1918:
        return "26.09.1918"
    elif (year < 1918 and year % 4 == 0) or (year > 1918 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))):
        return f"12.09.{year}"
    else:
        return f"13.09.{year}"

if __name__ == "__main__":
    year = 2017
    print(day_of_programmer(year))
