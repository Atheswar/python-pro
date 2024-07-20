def bon_appetit(bill, k, b):
    anna_share = (sum(bill) - bill[k]) // 2
    if b == anna_share:
        print("Bon Appetit")
    else:
        print(b - anna_share)

if __name__ == "__main__":
    bill = [3, 10, 2, 9]
    k = 1
    b = 12
    bon_appetit(bill, k, b)
