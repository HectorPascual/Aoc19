#wire_1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
#wire_2 = ['U62','R66','U55','R34','D71','R55','D58','R83']
mapped_movements = {'R' : (1,0), 'L' : (-1, 0), 'D' : (0, -1), 'U' : (0, 1)}
central_port = (0,0)

def move(init, step):
    move_trace = []
    pos = (init[0], init[1])
    for i in range(0, int(step[1:])) :
        pos = (pos[0] + mapped_movements[step[0]][0], pos[1] + mapped_movements[step[0]][1])
        move_trace.append(pos)
    return move_trace


def get_wire_trace(wire):
    trace = []
    current_pos = move(central_port, wire[0])
    trace.extend(current_pos)
    for i in range(1, len(wire)):
        current_pos = move(current_pos[-1], wire[i])
        trace.extend(current_pos)
    return trace


def find_intersections(trace_1, trace_2):
    return list((set(trace_1).intersection(set(trace_2))))


def combined_steps(trace_1, trace_2, intersections):
    steps_w1 = [trace_1.index(i)+1 for i in intersections]
    steps_w2 = [trace_2.index(i)+1 for i in intersections]
    return min([s_w1 + s_w2 for s_w1, s_w2 in zip(steps_w1, steps_w2)])


with open('input.txt') as f:
    wire_1 = f.readline().replace('\n','').split(',')
    wire_2 = f.readline().replace('\n','').split(',')

trace_1 = get_wire_trace(wire_1)
trace_2 = get_wire_trace(wire_2)
intersections = find_intersections(trace_1, trace_2)
print(combined_steps(trace_1, trace_2, intersections))