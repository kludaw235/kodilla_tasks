def test_import_factorization():
    try:
        from factorization import prime_factors
        assert callable(prime_factors), 'prime_factors is not callable'
    except ImportError as error:
        assert False, error


if __name__ == '__main__':
    for test in (test_import_factorization, ):
        print(f'{test.__name__}: ', end=' ')
        try:
            test()
            print("OK")
        except AssertionError as error:
            print(error)