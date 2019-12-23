def calc_final_state(input_arr):
    i = 0
    while True:
        op_code = str(input_arr[0 + i]).zfill(5)

        if op_code[4] != '9': # These case requires no params
            if op_code[2] == '1':
                first_param = input_arr[1 + i]  # Inmediate mode
            else:
                first_param = input_arr[input_arr[1 + i]]  # Position mode

        if not op_code[4] in ['3','4','9']: # These two cases require 1 param and 99 case 0 params
            if op_code[1] == '1':
                scnd_param = input_arr[2 + i]  # Inmediate mode
            else:
                scnd_param = input_arr[input_arr[2 + i]]  # Position mode

        if op_code[4] == '1':
            input_arr[input_arr[3 + i]] = first_param + scnd_param
            i += 4
        elif op_code[4] == '2':
            input_arr[input_arr[3 + i]] = first_param * scnd_param
            i += 4
        elif op_code[4] == '3':
            inp = int(input('Input a number for TEST : '))
            input_arr[input_arr[1 + i]] = inp
            i += 2
        elif op_code[4] == '4':
            print(input_arr[input_arr[1 + i]])
            i += 2
        elif op_code[4] == '99':
            break


with open('input.txt') as f:
    input_arr = list(map(int, f.readline().replace('\n', '').split(',')))


calc_final_state(input_arr)
