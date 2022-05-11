rom_to_dec_dict = \
    {'I' : 1,
    'V' : 5,
    'X' : 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
     }

class NumericalSystemsConverter:
    def __init__(self, src_system, target_system, number):
        self.number = number
        self.target_number = None

        if src_system == 'ROM' and target_system == 'DEC':
            self.check_rom_if_valid()
            self.rom_to_dec()

    def check_rom_if_valid(self):
        if self.number.count('D') > 1 or self.number.count('L') > 1 or self.number.count('V') > 1:
            raise ValueError()
        if self.number.count('C') >= 10 or self.number.count('X') >= 10 or self.number.count('I') >= 10:
            raise ValueError()

        rom_number_list = list(self.number)
        flag = False
        counter = 0
        for i in rom_number_list:
            if i == 'I':
                counter += 1
                flag = True
                continue
            if flag:
                if i != 'V' and i != 'X':
                    raise ValueError()
                else:
                    if counter > 1:
                        raise ValueError()
            flag = False


        flag = False
        counter = 0
        for i in rom_number_list:
            if i == 'X':
                counter += 1
                flag = True
                continue
            if flag:
                if i == 'M' or i == 'D':
                    raise ValueError()
                elif i != 'I' and i != 'V':
                    if counter > 1:
                        raise ValueError()
            flag = False

        flag = False
        counter = 0
        for i in rom_number_list:
            if i == 'C':
                counter += 1
                flag = True
                continue
            if flag:
                if i == 'M' or i == 'D':
                    if counter > 1:
                        raise ValueError()
            flag = False

        flag = False
        for i in rom_number_list:
            if i == 'V':
                flag = True
                continue
            if flag:
                if i != 'I':
                    raise ValueError()
            flag = False

        flag = False
        for i in rom_number_list:
            if i == 'L':
                flag = True
                continue
            if flag:
                if i != 'I' and i != 'V' and i != 'X':
                    raise ValueError()
            flag = False

        flag = False
        for i in rom_number_list:
            if i == 'D':
                flag = True
                continue
            if flag:
                if i == 'M':
                    raise ValueError()
            flag = False



    def rom_to_dec(self):
        number_list = list(self.number)
        self.target_number = rom_to_dec_dict[number_list[-1]]
        self.previous_number = rom_to_dec_dict[number_list[-1]]
        for i in reversed(number_list[:-1]):
            if self.previous_number <= rom_to_dec_dict[i]:
                self.target_number += rom_to_dec_dict[i]
            else:
                self.target_number -= rom_to_dec_dict[i]
            self.previous_number = rom_to_dec_dict[i]


if __name__ == '__main__':
    x = NumericalSystemsConverter('ROM', 'DEC', 'IVXLCDM')

    print(x.target_number)
