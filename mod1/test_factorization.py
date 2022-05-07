from mod1.factorization import prime_factors

def test_import_factorization():
    try:
        from factorization import prime_factors
        assert callable(prime_factors), 'prime_factors is not callable'
    except ImportError as error:
        assert False, error

def test_result_is_a_list():
    result = prime_factors(2)
    assert type(result) is list, 'Result is not a list'

def test_number_is_a_prime():
    result = prime_factors(11)
    assert result == [11], f'Expected [11], got {result}'

def test_number_is_not_a_prime():
    result = prime_factors(12)
    assert result != [12], f'Expected not [12], got {result}'

def test_number_with_same_factors():
    result = prime_factors(32)
    assert result == [2, 2, 2, 2, 2], f'Expected [2, 2, 2, 2, 2], got {result}'

def test_number_with_different_factors():
    result = prime_factors(36)
    assert result == [2, 2, 3, 3], f'Expected [2, 2, 3, 3], got {result}'

def test_big_number():
    result = prime_factors(3958159172)
    assert result == [2, 2, 11, 2347, 38329], f'Expected [2, 2, 11, 2347, 38329], got {result}'

def test_negative_number():
    try:
        result = prime_factors(-100)
        assert False, f'Expected ValueError, got {result}'
    except ValueError:
        pass

def test_zero():
    try:
        result = prime_factors(0)
        assert False, f'Expected ValueError, got {result}'
    except ValueError:
        pass

def test_one():
    try:
        result = prime_factors(1)
        assert False, f'Expected ValueError, got {result}'
    except ValueError:
        pass

if __name__ == '__main__':
    for test in (test_import_factorization, test_result_is_a_list, test_number_is_a_prime, test_number_is_not_a_prime,
                 test_number_with_same_factors, test_number_with_different_factors, test_big_number, test_negative_number,
                 test_zero, test_one):
        print(f'{test.__name__}: ', end=' ')
        try:
            test()
            print("OK")
        except AssertionError as error:
            print(error)