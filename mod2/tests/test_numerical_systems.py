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
        assert nsv('ROM', 'DEC', 'MMDCCLXXVIII').target_number == 2778

    def test_5(self):
        assert nsv('ROM', 'DEC', 'CMXCIX').target_number == 999


class TestSingleAppearDLV:
    def test_single_appear_D(self):
        with pytest.raises(ValueError):
            print(nsv('ROM', 'DEC', 'MDDLX').target_number)

    def test_single_appear_L(self):
        with pytest.raises(ValueError):
            print(nsv('ROM', 'DEC', 'MDLLX').target_number)

    def test_single_appear_V(self):
        with pytest.raises(ValueError):
            print(nsv('ROM', 'DEC', 'VVVI').target_number)


class TestSmallerDenominationsAsMCX:
    def test_smaller_equal_M(self):
        with pytest.raises(ValueError):
            print(nsv('ROM', 'DEC', 'CCCCCCCCCC').target_number)

    def test_smaller_exceed_M(self):
        with pytest.raises(ValueError):
            print(nsv('ROM', 'DEC', 'CCCCCCCCCCC').target_number)

    def test_smaller_correct_M(self):
        assert nsv('ROM', 'DEC', 'CCCCCCCCC').target_number == 900

    def test_smaller_equal_C(self):
        with pytest.raises(ValueError):
            print(nsv('ROM', 'DEC', 'XXXXXXXXXX').target_number)

    def test_smaller_exceed_C(self):
        with pytest.raises(ValueError):
            print(nsv('ROM', 'DEC', 'XXXXXXXXXXX').target_number)

    def test_smaller_correct_C(self):
        assert nsv('ROM', 'DEC', 'XXXXXXXXX').target_number == 90

    def test_smaller_equal_X(self):
        with pytest.raises(ValueError):
            print(nsv('ROM', 'DEC', 'IIIIIIIIII').target_number)

    def test_smaller_exceed_X(self):
        with pytest.raises(ValueError):
            print(nsv('ROM', 'DEC', 'IIIIIIIIIII').target_number)

    def test_smaller_correct_X(self):
        assert nsv('ROM', 'DEC', 'IIIIIIIII').target_number == 9


class TestSubLeadingNumsIXC:
    inputs = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

    @staticmethod
    def check_result(test_value, result):
        if not result:
            with pytest.raises(ValueError):
                print(nsv('ROM', 'DEC', test_value).target_number)
        else:
            assert nsv('ROM', 'DEC', test_value).target_number == result

    def test_sub_leading_I(self):
        expected_results = [False, False, False, False, 9, 4, 2]
        for i in range(len(self.inputs)):
            self.check_result('I' + self.inputs[i], expected_results[i])

    def test_sub_leading_X(self):
        expected_results = [False, False, 90, 40, 20, 15, 11]
        for i in range(len(self.inputs)):
            self.check_result('X' + self.inputs[i], expected_results[i])

    def test_sub_leading_C(self):
        expected_results = [900, 400, 200, 150, 110, 105, 101]
        for i in range(len(self.inputs)):
            self.check_result('C' + self.inputs[i], expected_results[i])

    def test_single_sub_leading_I(self):
        for i in range(len(self.inputs) - 1):
            with pytest.raises(ValueError):
                print(nsv('ROM', 'DEC', 'II' + self.inputs[i]).target_number)

    def test_single_sub_leading_X(self):
        for i in range(len(self.inputs) - 3):
            with pytest.raises(ValueError):
                print(nsv('ROM', 'DEC', 'XX' + self.inputs[i]).target_number)

    def test_single_sub_leading_C(self):
        for i in range(len(self.inputs) - 5):
            with pytest.raises(ValueError):
                print(nsv('ROM', 'DEC', 'CC' + self.inputs[i]).target_number)

    class TestDescendingOrder:
        def test_1(self):
            with pytest.raises(ValueError):
                print(nsv('ROM', 'DEC', 'IVX').target_number)

        def test_2(self):
            with pytest.raises(ValueError):
                print(nsv('ROM', 'DEC', 'XLC').target_number)

        def test_3(self):
            with pytest.raises(ValueError):
                print(nsv('ROM', 'DEC', 'CDM').target_number)

        def test_4(self):
            with pytest.raises(ValueError):
                print(nsv('ROM', 'DEC', 'IVXLCDM').target_number)

    def test_small_letters(self):
        assert nsv('ROM', 'DEC', 'mdclxvi').target_number == 1666

    def test_dec_to_rom_target_str(self):
        assert isinstance(nsv('DEC', 'ROM', 4).target_number, str)

    class TestDecToRomSrcValid:
        def test_src_float(self):
            with pytest.raises(ValueError):
                print(nsv('DEC', 'ROM', 2.5).target_number)

        def test_src_list(self):
            with pytest.raises(ValueError):
                print(nsv('DEC', 'ROM', [2, 5]).target_number)

        def test_src_tuple(self):
            with pytest.raises(ValueError):
                print(nsv('DEC', 'ROM', (2, 5)).target_number)

        def test_src_str(self):
            assert nsv('DEC', 'ROM', '4').target_number == 'IV'

        def test_negative(self):
            with pytest.raises(ValueError):
                print(nsv('DEC', 'ROM', -1).target_number)

        def test_zero(self):
            with pytest.raises(ValueError):
                print(nsv('DEC', 'ROM', 0).target_number)

    class TestDecToRomSmallNums:
        def test_1(self):
            assert nsv('DEC', 'ROM', 33).target_number == 'XXXIII'

        def test_2(self):
            assert nsv('DEC', 'ROM', 79).target_number == 'LXXIX'

        def test_3(self):
            assert nsv('DEC', 'ROM', 44).target_number == 'XLIV'

        def test_4(self):
            assert nsv('DEC', 'ROM', 66).target_number == 'LXVI'

        def test_5(self):
            assert nsv('DEC', 'ROM', 1).target_number == 'I'

    class TestDecToRomGreatNums:
        def test_1(self):
            assert nsv('DEC', 'ROM', 1665).target_number == 'MDCLXV'

        def test_2(self):
            assert nsv('DEC', 'ROM', 4444).target_number == 'MMMMCDXLIV'

        def test_3(self):
            assert nsv('DEC', 'ROM', 3888).target_number == 'MMMDCCCLXXXVIII'

        def test_4(self):
            assert nsv('DEC', 'ROM', 2778).target_number == 'MMDCCLXXVIII'

        def test_5(self):
            assert nsv('DEC', 'ROM', 4999).target_number == 'MMMMCMXCIX'
