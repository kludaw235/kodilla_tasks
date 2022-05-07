def prime_factors(number):
    factors = []
    for i in range(2, number+1):
        while True:
            if number % i == 0:
                if i == number:
                    break
                else:
                    number = number // i
                    factors.append(i)
                    continue
            else:
                break


    factors.append(number)

    return factors

