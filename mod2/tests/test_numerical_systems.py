

def test_import_NumericalSystemsConverter():
    try:
        from mod2.numerical_systems import NumericalSystemsConverter
        assert callable(NumericalSystemsConverter), 'prime_factors is not callable'
    except ImportError as error:
        assert False, error