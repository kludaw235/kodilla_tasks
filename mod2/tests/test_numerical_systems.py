from mod2.numerical_systems import NumericalSystemsConverter as nsv
import pytest



def test_import_NumericalSystemsConverter():
    try:
        from mod2.numerical_systems import NumericalSystemsConverter
        assert callable(NumericalSystemsConverter), 'NumericalSystemsConverter is not callable'
    except ImportError as error:
        assert False, error


def test_rom_to_dec_target_int():
    assert isinstance(nsv('ROM', 'DEC', 'IV').target_number, int)