"""
Calculate of factorial of given number.
Find the number of trailing zeros in the factorial.
"""
#Solve
def factorial(n):
    if n==0 or n==1:
        return 1
    elif n<0:
        return "The Factorial is invalid or infinite"
    else:
        return n*factorial(n-1)
def count_trailing_zeros(n):
    if n == 0: return 1  # Edge case: 0 has 1 trailing zero
    count = 0
    while n % 10 == 0:
        count += 1
        n //= 10
    return count
    
if __name__=="__main__":
    n=int(input("Enter the number: "))
    a=factorial(n) 
    print(f"The factorial is {a}")
    print(f"The number of trailing zeros is {count_trailing_zeros(a)}")