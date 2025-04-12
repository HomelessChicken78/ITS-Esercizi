'''r2. check if the input is correct'''

from B_10_Conquer.Correct_Input.n_2_1_Only_one_character import islongenough
from B_10_Conquer.Correct_Input.n_2_2_hassign import has_sign
from B_10_Conquer.Correct_Input.n_2_3_Non_alphanumeric import isvalid
from B_10_Conquer.Correct_Input.n_2_4_repeated_char import isrepeated

def check_input(num_sys: str) -> bool:
    if islongenough(num_sys) and (not has_sign(num_sys)) and isvalid(num_sys) and (not isrepeated(num_sys)):
        return True
    else:
        return False


if __name__ == "__main__":
    print(check_input(input("Insert something:\n>\t")))