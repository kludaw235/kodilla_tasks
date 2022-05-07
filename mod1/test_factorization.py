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

if __name__ == '__main__':
    for test in (test_import_factorization, test_result_is_a_list, test_number_is_a_prime, test_number_is_not_a_prime):
        print(f'{test.__name__}: ', end=' ')
        try:
            test()
            print("OK")
        except AssertionError as error:
            print(error)