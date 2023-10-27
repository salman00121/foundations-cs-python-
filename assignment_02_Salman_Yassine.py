def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


num = int(input("Enter an integer: "))
if num >= 0: 
    result = find_divisors(num)
    print(result)





