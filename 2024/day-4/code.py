def array_column(arr, i):
    return [row[i] for row in arr]


data = []

with open('input.txt', 'r') as input:
    line = input.readline()
    while line:
        data.append(line.strip())
        line = input.readline()

xmas_count = 0

# XMAS horizontal search
xmas_count += sum([line.count('XMAS') for line in data])
xmas_count += sum([line.count('SAMX') for line in data])

# XMAS vertical search
xmas_count += sum([''.join(array_column(data, i)).count('XMAS')
                  for i in range(len(data[0]))])
xmas_count += sum([''.join(array_column(data, i)).count('SAMX')
                  for i in range(len(data[0]))])

# XMAS diagonal & reverse diagonal search
diagonal_length = 4

for i in range(len(data)-diagonal_length+1):
    for j in range(len(data[0])-diagonal_length+1):
        diagonal_value = ''
        reverse_diagonal_value = ''

        for k in range(diagonal_length):
            diagonal_value += data[i+k][j+k]
            reverse_diagonal_value += data[i+diagonal_length-k-1][j+k]

        xmas_count += 1 if diagonal_value == 'XMAS' else 0
        xmas_count += 1 if diagonal_value == 'SAMX' else 0
        xmas_count += 1 if reverse_diagonal_value == 'XMAS' else 0
        xmas_count += 1 if reverse_diagonal_value == 'SAMX' else 0

cross_xmas_count = 0

# cross X-MAS search
diagonal_length = 3

for i in range(len(data)-diagonal_length+1):
    for j in range(len(data[0])-diagonal_length+1):
        diagonal_value = ''
        reverse_diagonal_value = ''

        for k in range(diagonal_length):
            diagonal_value += data[i+k][j+k]
            reverse_diagonal_value += data[i+diagonal_length-k-1][j+k]

        cross_xmas_count += 1 if diagonal_value == 'MAS' and reverse_diagonal_value == 'MAS' else 0
        cross_xmas_count += 1 if diagonal_value == 'MAS' and reverse_diagonal_value == 'SAM' else 0
        cross_xmas_count += 1 if diagonal_value == 'SAM' and reverse_diagonal_value == 'MAS' else 0
        cross_xmas_count += 1 if diagonal_value == 'SAM' and reverse_diagonal_value == 'SAM' else 0

print('Part 1:', xmas_count)
print('Part 2:', cross_xmas_count)
