def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(3, int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

T = int(input())

for i in range(T):
    x = int(input())
    a = x // 2
    b = a
    
    while True:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        a -= 1
        b += 1

    
    


        