def prime_factors(number):
    factors = []
    i = 2
    while True:
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
        if i == number:
            break
        i += 1


    factors.append(number)

    return factors

