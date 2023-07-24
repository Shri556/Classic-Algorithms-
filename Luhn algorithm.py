num = 1234567890123456

def luhn_algo(num):
    def str_to_int(n):
        return [int(n) for n in str(n)]
    
    num = str_to_int(num)
    odd_num = num[-1::-2]
    even_num = num[-2::-2]

    check_sum = 0
    check_sum += sum(odd_num)

    for x in even_num:
        check_sum += sum(str_to_int(x*2) )

    if check_sum % 10 == 0:
        print("VALID")

    else:
        print("INVALID")

luhn_algo(num)