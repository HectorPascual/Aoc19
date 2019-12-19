def calc_final_state(input):
    """
    Iterates length/4 times through the array, taking the first position of the group of 4 as the
    op code, the second and third position values as the index for the parameters of the operation
    and the last position shows the index where the result will be stored.
    :param input:
    :return: the final state of the input array
    """
    for i in range(0,int(len(input)/4)+1):
        if input[0+i*4] == 1:
            input[input[3+i*4]] = input[input[1+i*4]] + input[input[2+i*4]]
        elif input[0+i*4] == 2:
            input[input[3+i*4]] = input[input[1+i*4]] * input[input[2+i*4]]
        elif input[0+i*4] == 99:
            break
    return input


with open('input.txt') as f:
    input = list(map(int, f.readline().replace('\n','').split(',')))

input[1]=12
input[2]=2

print(calc_final_state(input)[0])
