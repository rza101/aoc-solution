import itertools

data = {}

with open('input.txt', 'r') as input:
    line = input.readline()

    while line:
        splitted = line.split(': ')

        operands = [int(x) for x in splitted[1].split(' ')]
        result = int(splitted[0])

        data[result] = operands

        line = input.readline()

# part 1
valid_result_sum = 0

for result, operands in data.items():
    for operators in itertools.product([0, 1], repeat=len(operands) - 1):
        computed_result = operands[0]

        for index, operator in enumerate(operators):
            match(operator):
                case 0:
                    computed_result += operands[index + 1]
                case 1:
                    computed_result *= operands[index + 1]

        if computed_result == result:
            valid_result_sum += result
            break

print('Part 1:', valid_result_sum)

# part 2
valid_result_sum = 0

for result, operands in data.items():
    for operators in itertools.product([0, 1, 2], repeat=len(operands) - 1):
        computed_result = operands[0]

        for index, operator in enumerate(operators):
            match(operator):
                case 0:
                    computed_result += operands[index + 1]
                case 1:
                    computed_result *= operands[index + 1]
                case 2:
                    computed_result = int(
                        str(computed_result) + str(operands[index + 1])
                    )

        if computed_result == result:
            valid_result_sum += result
            break

print('Part 2:', valid_result_sum)

# backtracking or DP is recommended here
