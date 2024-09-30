numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes = []
not_primes = []
for num in numbers:
    if num < 2:
        is_prime = False
    else:
        is_prime = True
        razdelitel = 2
        while razdelitel * razdelitel <= num:
            if num % razdelitel ==0:
                is_prime = False
                break
                razdelitel += 1
        if is_prime:
            primes.append(num)
        else:
            not_primes.append(num)
            print ("простые числа: ")
            print("непростые числа: ")