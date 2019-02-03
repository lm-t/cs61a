def sum_digits(num):
    str_num = str(num)
    total = 0
    for i in range(len(str_num)):
        total += int(str_num[i])
    print(total)
