left = []
right = []

with open('input.txt', 'r') as input:
    line = input.readline()

    while line:
        left_num, right_num = line.split()
        left.append(int(left_num))
        right.append(int(right_num))

        line = input.readline()

print('Part 1:', sum([abs(x[0] - x[1])
      for x in zip(sorted(left), sorted(right))]))

right_dict = {}

for element in right:
    right_dict.update({
        element: right_dict.get(element, 0) + 1
    })

print('Part 2:', sum([x*right_dict.get(x, 0) for x in left]))
