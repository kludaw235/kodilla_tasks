
class NumericalSystemsConverter:
    def __init__(self, src_system, target_system, number):
        self.number = number
        self.target_number = None

        if src_system == 'ROM' and target_system == 'DEC':
           self.rom_to_dec()

    def rom_to_dec(self):
        self.target_number = 4
