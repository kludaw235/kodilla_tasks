rom_to_dec_dict = \
    {'I': 1,
     'V': 5,
     'X': 10,
     'L': 50,
     'C': 100,
     'D': 500,
     'M': 1000,
     }


def get_value_by_key(searched):
    return [key for key, value in rom_to_dec_dict.items() if value == searched]


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

        def check_counter(c):
            if c > 1:
                raise ValueError()

        def order_validation(leading_numeral, invalid_next_numerals):
            rom_number_list = list(self.number)
            counter = 0
            prev = None
            flag = False

            for i in rom_number_list:
                if i == leading_numeral:
                    counter += 1
                    prev = i
                    flag = True
                    continue
                if flag:
                    if prev == 'C':
                        for letter in invalid_next_numerals:
                            if i == letter:
                                check_counter(counter)
                    elif prev == 'X':
                        for letter in invalid_next_numerals:
                            if i == letter:
                                raise ValueError()
                        if i != 'I' and i != 'V':
                            check_counter(counter)
                    else:
                        for letter in invalid_next_numerals:
                            if i == letter:
                                raise ValueError()
                        else:
                            check_counter(counter)

        if self.number.count('D') > 1 or self.number.count('L') > 1 or self.number.count('V') > 1:
            raise ValueError()
        if self.number.count('C') >= 10 or self.number.count('X') >= 10 or self.number.count('I') >= 10:
            raise ValueError()

        order_validation('I', 'MDCL')
        order_validation('X', 'MD')
        order_validation('C', 'MD')
        order_validation('V', 'MDCLX')
        order_validation('L', 'MDC')
        order_validation('D', 'M')

    def rom_to_dec(self):
        number_list = list(self.number)
        self.target_number = rom_to_dec_dict[number_list[-1]]
        previous_number = rom_to_dec_dict[number_list[-1]]
        for i in reversed(number_list[:-1]):
            if previous_number <= rom_to_dec_dict[i]:
                self.target_number += rom_to_dec_dict[i]
            else:
                self.target_number -= rom_to_dec_dict[i]
            previous_number = rom_to_dec_dict[i]

    def check_dec_if_valid(self):
        if not (isinstance(self.number, int) or isinstance(self.number, str)):
            raise ValueError()
        if int(self.number) < 1:
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
                self.target_number += times * get_value_by_key(multiplier)[0]
            elif times == 4:
                self.target_number += get_value_by_key(multiplier)[0] + get_value_by_key(multiplier * 5)[0]
            elif times == 9:
                self.target_number += get_value_by_key(multiplier)[0] + get_value_by_key(multiplier * 10)[0]
            else:
                self.target_number += get_value_by_key(multiplier * 5)[0] + (times - 5) * \
                                      get_value_by_key(multiplier)[0]
