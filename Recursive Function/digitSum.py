def digit_sum(n):
    if n < 10:
        return n
    else:
        return n % 10 + digit_sum(n // 10)

n = int(input("Enter a number: "))
print("Digit sum of", n, "is", digit_sum(n))
