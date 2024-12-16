import copy

map_array = []
initial_guard_position = None

with open('input.txt',  'r') as input:
    line = input.readline()
    i = 0

    while line:
        map_array.append(list(line.rstrip()))

        if line.find('^') != -1:
            initial_guard_position = (i, line.find('^'))

        line = input.readline()
        i += 1

# part 1
visited_positions = set()
visited_positions.add(initial_guard_position)  # initial position is accounted

guard_direction = 0  # up, right, down, left
guard_position = initial_guard_position

while True:
    match guard_direction:
        case 0:  # up
            new_guard_position = (guard_position[0] - 1, guard_position[1])
        case 1:  # right
            new_guard_position = (guard_position[0], guard_position[1] + 1)
        case 2:  # down
            new_guard_position = (guard_position[0] + 1, guard_position[1])
        case 3:  # left
            new_guard_position = (guard_position[0], guard_position[1] - 1)

    if new_guard_position[0] < 0 or\
            new_guard_position[0] > len(map_array) - 1 or\
            new_guard_position[1] < 0 or\
            new_guard_position[1] > len(map_array[0]) - 1:
        break
    else:
        if map_array[new_guard_position[0]][new_guard_position[1]] != '#':
            guard_position = new_guard_position
            visited_positions.add(guard_position)
        else:
            guard_direction = (guard_direction+1) % 4

# part 2
modified_visited_position = copy.deepcopy(visited_positions)
modified_visited_position.remove(
    initial_guard_position
)  # guard position cannot be obstacle

obstacle_count = 0

for visited_position in modified_visited_position:
    # now considering direction
    visited_states = set()
    guard_state = (initial_guard_position[0], initial_guard_position[1], 0)

    visited_states.add(guard_state)

    while True:
        match guard_state[2]:
            case 0:  # up
                new_guard_position = (
                    guard_state[0] - 1, guard_state[1])
            case 1:  # right
                new_guard_position = (
                    guard_state[0], guard_state[1] + 1)
            case 2:  # down
                new_guard_position = (
                    guard_state[0] + 1, guard_state[1])
            case 3:  # left
                new_guard_position = (
                    guard_state[0], guard_state[1] - 1)

        if new_guard_position[0] < 0 or\
                new_guard_position[0] > len(map_array) - 1 or\
                new_guard_position[1] < 0 or\
                new_guard_position[1] > len(map_array[0]) - 1:
            break
        else:
            # original obstacle is not changed
            # so the only way to change the path is to put the obstacle in the visited path
            # and "applied" with this condition
            if map_array[new_guard_position[0]][new_guard_position[1]] == '#' or\
                (new_guard_position[0] == visited_position[0] and
                    new_guard_position[1] == visited_position[1]):
                guard_state = (
                    guard_state[0],
                    guard_state[1],
                    (guard_state[2] + 1) % 4
                )
            else:
                guard_state = (
                    new_guard_position[0],
                    new_guard_position[1],
                    guard_state[2]
                )

            previous_length = len(visited_states)

            visited_states.add(guard_state)

            # if visited states count not increasing after adding new state
            # then the guard is looping
            if (previous_length == len(visited_states)):
                obstacle_count += 1
                break

print('Part 1:', len(visited_positions))
print('Part 2:', obstacle_count)
