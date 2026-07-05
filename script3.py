import math
def is_prime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False

    for i in range(5,math.isqrt(n)+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True

n=9999999967
if is_prime(n):
    print(f"{n} is prime number")
else:
    print(f"{n} not prime number")