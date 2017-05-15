def length_check(number):
    if len(number) == 11:
        return True
    else:
        return False


def operator_check(number):
    cn_mobile = [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159,
                 182, 183, 184, 187, 188, 147, 178, 1705]
    cn_union = [130, 131, 132, 155, 156, 185, 186, 145, 176, 1709]
    cn_telecom = [133, 153, 180, 181, 189, 177, 1700]
    number_three = int(number[:3])
    number_four = int(number[:4])

    if number_three in cn_mobile or number_four in cn_mobile:
        return "China Mobile"
    elif number_three in cn_union or number_four in cn_union:
        return "China Union"
    elif number_three in cn_telecom or number_four in cn_telecom:
        return "China Telecom"
    else:
        return "No such a operator"

while True:
    number_input = input("Enter your number:")
    length_result = length_check(number_input)
    if length_result:
        operator_result = operator_check(number_input)
        if operator_result == "No such a operator":
            print(operator_result)
        else:
            print("Operator :" + operator_result)
            print("We're sending verification code via text to your phone: {}"
                  .format(number_input))
            break
    else:
        print("Invalid length, your number shoule be in 11 digits")
