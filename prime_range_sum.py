def is_prime(num):
    if num < 2:
        return False
    elif num == 2 or num == 3:
        return True
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 :
        return False
    else:
        return True


# print(is_prime(919))

def primeRangeSum(num1, num2):
    prime_nums_array = []
    prime_nums_sum = 0

    if(num1 > num2):
        for i in range(num2, num1+1):
            prime = is_prime(i)
            if (prime):
                prime_nums_array.append(i)
    else:
        for i in range(num1, num2+1):
            prime = is_prime(i)
            if (prime):
                prime_nums_array.append(i)
    #print(prime_nums_array)
    for i in range(len(prime_nums_array)):
        prime_nums_sum += prime_nums_array[i]

    return prime_nums_sum


print(primeRangeSum(10, 20))
print(primeRangeSum(20, 10)) #  => 60
print(primeRangeSum(20, 29)) #;  => 52
print(primeRangeSum(50, 41)) #;  => 131