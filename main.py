class Roter:
    def __init__(self, position1, position2, position3):
        self.position1 = position1
        self.position2 = position2
        self.position3 = position3

    def smena_rotera(self):
        self.position1 += 1
        if self.position1 > 25:
            self.position1 = 0
        if self.position1 == 5 or self.position1 == 17:
            self.position2 += 1
            if self.position2 > 25:
                self.position2 = 0
            if self.position2 == 4 or self.position2 == 16:
                self.position3 += 1
                if self.position3 > 25:
                    self.position3 = 0
        # print(f'The rotors were switched, now the positions of the rotors are as follows: {self.position1 + 1}, {self.position2 + 1}, {self.position3 + 1}')


def travel_through_rotors(symbol_massage):

    r_2_minus_1 = (rotors.position2 - rotors.position1) % 26
    r_3_minus_2 = (rotors.position3 - rotors.position2) % 26

    # jump_on_1_rotor:
    result_1_rotor = rotor1[(alphabet.index(symbol_massage) + rotors.position1) % 26]

    # jump_on_2_rotor:
    result_2_rotor = rotor2[(alphabet.index(result_1_rotor) + r_2_minus_1) % 26]

    # jump_on_3_rotor:
    result_3_rotor = rotor3[(alphabet.index(result_2_rotor) + r_3_minus_2) % 26]

    # jump_on_refractor:
    almost_result_refractor = alphabet[(alphabet.index(result_3_rotor) - rotors.position3) % 26]
    a = refractor_b_input.index(almost_result_refractor)
    result_refractor = refractor_b_output[a]

    # come_in_3_rotor:
    final_result_3_rotor = alphabet[rotor3.index(alphabet[(alphabet.index(result_refractor) + rotors.position3) % 26])]

    # come_in_2_rotor:
    final_result_2_rotor = alphabet[rotor2.index(alphabet[(alphabet.index(final_result_3_rotor) - r_3_minus_2) % 26])]

    # come_in_1_rotor:
    final_result_1_rotor = alphabet[rotor1.index(alphabet[(alphabet.index(final_result_2_rotor) - r_2_minus_1) % 26])]

    # final:
    final_result = alphabet[(alphabet.index(final_result_1_rotor) - rotors.position1) % 26]

    return final_result


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
rotor1 = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']
rotor2 = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E']
rotor3 = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']
refractor_b_input = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K', 'M', 'T', 'V', 'Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'P', 'X', 'N', 'O', 'Z', 'W']
refractor_b_output = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'P', 'X', 'N', 'O', 'Z', 'W', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K', 'M', 'T', 'V']

while True:
    try:
        position_roter1 = int(input('Input rotor 1 position (1-26): ')) - 1
        if position_roter1 < 0 or position_roter1 > 25:
            print('Position must be between 1 and 26.')
        else:
            break
    except ValueError:
        print('Please input an integer.')

while True:
    try:
        position_roter2 = int(input('Inpup roter 2 position (1-26): ')) - 1
        if position_roter2 < 0 or position_roter2 > 25:
            print('Position must be between 1 and 26.')
        else:
            break
    except ValueError:
        print('Please input an integer.')

while True:
    try:
        position_roter3 = int(input('Inpup roter 3 position (1-26): ')) - 1
        if position_roter3 < 0 or position_roter3 > 25:
            print('Position must be between 1 and 26.')
        else:
            break
    except ValueError:
        print('Please input an integer.')

rotors = Roter(position_roter1, position_roter2, position_roter3)

while True:
    try:
        what_do_you_want = input('Encode or Decode (en or de): ')
        if what_do_you_want.upper() == 'ENCODE' or what_do_you_want.upper() == 'EN':
            encode_m = input('Input message: ')
            encode_massage = []

            for symbol in encode_m.upper():
                if symbol == ' ':
                    encode_massage.append(symbol)
                    rotors.smena_rotera()
                else:
                    encode = travel_through_rotors(symbol)
                    encode_massage.append(encode)
                    rotors.smena_rotera()

            print(''.join(encode_massage))
            break

        elif what_do_you_want.upper() == 'DECODE' or what_do_you_want.upper() == 'DE':
            decode_m = input('Decode: ')
            decode_massage = []

            for de_symbol in decode_m.upper():
                if de_symbol == ' ':
                    decode_massage.append(de_symbol)
                    rotors.smena_rotera()
                else:
                    decode = travel_through_rotors(de_symbol)
                    decode_massage.append(decode)
                    rotors.smena_rotera()
            print(''.join(decode_massage))
            break

        else:
            print('You should choose what you want to Encode or Decode')
    except:
        break

exit = input('Press Enter to exit ')
if exit:
    pass