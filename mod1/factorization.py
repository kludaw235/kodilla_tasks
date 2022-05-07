def prime_factors(number):
    if number <= 1:
        raise ValueError()
    factors = []
    i = 2
    while i<number:
        while number % i == 0 and i != number:
                number = number // i
                factors.append(i)
        i += 1


    factors.append(number)

    return factors

