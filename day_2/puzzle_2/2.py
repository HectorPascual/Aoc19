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


def find_noun_verb(input):
    """
    Iterate noun and verb from 0 to 99 trying to calc the state for each pair, resetting the input
    vector each time, when the correct pair is found it prints the values.
    :param input:
    :return:
    """
    for noun in range(0, 99+1):
        for verb in range(0, 99+1):
            input_clean = input.copy()
            input_clean[1] = noun
            input_clean[2] = verb
            if calc_final_state(input_clean)[0] == 19690720:
                print(f'Noun : {noun} | Verb : {verb} -> 100*noun + verb = {100*noun+verb}')

with open('input.txt') as f:
    input = list(map(int, f.readline().replace('\n','').split(',')))

find_noun_verb(input)
