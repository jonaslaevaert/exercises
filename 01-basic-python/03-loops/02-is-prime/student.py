def is_prime(n):
    if n == 1 or n == 0:
        return False
    delers = 0
    for i in range(n - 1, 1, -1):
        if(n % i == 0):
            delers += 1
    return delers == 0
        
        

