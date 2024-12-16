import re

# this pattern catch number groups inside non catching group
MULTIPLY_STATEMENT_REGEX_PATTERN = r'(?:mul\(([0-9]{1,3}),([0-9]{1,3})\))'

# for part 2, also catch do() and don't(), and later be processed on loop
MULTIPLY_STATEMENT_WITH_FLAG_REGEX_PATTERN = \
    r'(?:(do\(\))|(don\'t\(\))|mul\(([0-9]{1,3}),([0-9]{1,3})\))'

multiply_result = 0
multiply_with_flag_result = 0

with open('input.txt', 'r') as input:
    data = input.read()  # "memory" is contiguous, so no need to read each line

    multiply_statements = re.findall(
        MULTIPLY_STATEMENT_REGEX_PATTERN, data)
    multiply_result += sum([int(num[0])*int(num[1])
                            for num in multiply_statements])

    multiply_with_flag_statements = re.findall(
        MULTIPLY_STATEMENT_WITH_FLAG_REGEX_PATTERN, data
    )

    enabled_flag = True

    for statement in multiply_with_flag_statements:
        if statement[1] == 'don\'t()':
            enabled_flag = False
        elif statement[0] == 'do()':
            enabled_flag = True
        elif enabled_flag:
            multiply_with_flag_result += int(
                statement[2])*int(statement[3])

print('Part 1:', multiply_result)
print('Part 2:', multiply_with_flag_result)
