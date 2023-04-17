def is_prime(a):
    if a < 2:
        return False
    elif a == 2:
        return True
    for i in range(2,a):
        if(a == i +1):
            return True
        elif(a % i == 0):
            return False



                    
    