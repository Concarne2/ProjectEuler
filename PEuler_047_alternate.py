def distinct_prime_factors(in_num):
    i = 2
    distinct_factors = set()
    while i * i <= in_num:
        if in_num % i:
            i += 1
        else:
            in_num //= i
            distinct_factors.add(i)
    if in_num > 1:
        distinct_factors.add(in_num)
    return distinct_factors


counter = 0
n = 4
for i in range(2, 1000000):
    if len(distinct_prime_factors(i)) == n:
        counter += 1
        if counter == n:
            print(i - n+1)
            break
    else:
        counter = 0
