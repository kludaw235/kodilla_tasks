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

# def test_rom_to_dec_small_nums():
#     assert nsv('ROM', 'DEC', 'XXIV').target_number == 24

class TestRomToDecSmallNums:
    def test_1(self):
        assert nsv('ROM', 'DEC', 'IV').target_number == 4

    def test_2(self):
        assert nsv('ROM', 'DEC', 'XXIV').target_number == 24

    def test_3(self):
        assert nsv('ROM', 'DEC', 'XXXVI').target_number == 36

    def test_4(self):
        assert nsv('ROM', 'DEC', 'XIIIIII').target_number == 16

    def test_5(self):
        assert nsv('ROM', 'DEC', 'XXXVI').target_number == 36

class TestRomToDecGreatNums:
    def test_1(self):
        assert nsv('ROM', 'DEC', 'MDCLXV').target_number == 1665

    def test_2(self):
        assert nsv('ROM', 'DEC', 'MMMMDCCCXXXIX').target_number == 4839

    def test_3(self):
        assert nsv('ROM', 'DEC', 'MMMDCCCLXXXVIII').target_number == 3888

    def test_4(self):
        assert nsv('ROM', 'DEC', 'MMDMCCLCXXVXIII').target_number == 2778

    def test_5(self):
        assert nsv('ROM', 'DEC', 'CMXCIX').target_number == 999

