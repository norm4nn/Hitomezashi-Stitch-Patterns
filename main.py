import turtle
import Sammy



VOWELS = 'AEIOU'

def string_code_repair(str_code):#making sure code contains only alpha numeric chars
    str_code = str_code.upper()
    result = ''.join(ch for ch in str_code if ch.isalnum())

    return result

def str2binnary(str_code):#VOWELS ARE ONES, AND ODD DIDGITS ARE ONES
    bin_result = []
    for ch in str_code:
        if ord(ch) >= 65: #char is aplhabetic
            if ch in VOWELS: bin_result.append(1) #char is vowel
            else: bin_result.append(0)
        else: bin_result.append(ord(ch)%2) #  char is numeric

    return bin_result

def get_bin_str_codes():
    first_code_box = turtle.textinput(title="Please input first code", prompt="Code:")
    second_code_box = turtle.textinput(title="Please input second code", prompt="Code:")

    str_code1 = string_code_repair(first_code_box)
    str_code2 = string_code_repair(second_code_box)

    code1 = str2binnary(str_code1)
    code2 = str2binnary(str_code2)

    return code1, code2, str_code1, str_code2

if __name__=='__main__':
    bin1, bin2, str1, str2 = get_bin_str_codes()

    sammy = Sammy.Sammy()

    sammy.setting_step(str1,str2)

    sammy.draw_grid(str1, str2, bin1, bin2)

    turtle.done()