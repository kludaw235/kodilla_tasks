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
            self.number = self.number.upper()
            self.check_rom_if_valid()
            self.rom_to_dec()
        elif src_system == 'DEC' and target_system == 'ROM':
            self.dec_to_rom()


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


    def check_dec_if_valid(self):
        if self.number > 0:
            raise ValueError()

    def dec_to_rom(self):
        self.check_dec_if_valid()
        number_list = list(str(self.number))
        multiplier = 1
        test_table = []
        for i in reversed(number_list):
            test_table.insert(0, [int(i), multiplier])
            multiplier *= 10

        self.target_number = ''
        for times, multiplier in test_table:
            print(test_table)
            if times <= 3 or multiplier == rom_to_dec_dict['M']:
                self.target_number += times * self.get_value_by_key(multiplier)[0]
            elif times == 4:
                self.target_number += self.get_value_by_key(multiplier)[0] + self.get_value_by_key(multiplier*5)[0]
            elif times == 9:
                self.target_number += self.get_value_by_key(multiplier)[0] + self.get_value_by_key(multiplier*10)[0]
            else:
                self.target_number += self.get_value_by_key(multiplier*5)[0] + (times-5) * self.get_value_by_key(multiplier)[0]


    def get_value_by_key(self, searched):
        return [key for key, value in rom_to_dec_dict.items() if value == searched]

if __name__ == '__main__':
    x = NumericalSystemsConverter('ROM', 'DEC', -1)

    print(x.target_number)
