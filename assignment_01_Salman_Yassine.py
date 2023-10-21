def factor(n):

        factor = 1
        for i in range(1, n + 1):
            factor *= i
        return factor
        
n = int(input("Input: "))

print("Output: "  + str(factor(n)))