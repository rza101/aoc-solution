import itertools

antennas = {}

antinodes = set()
updated_antinodes = set()

with open('input.txt', 'r') as input:
    line = input.readline()
    i = 0

    width = len(line) - 1  # adjusting linebreak

    while line:
        for j, char in enumerate(line.rstrip()):
            if char != '.':
                antenna_coords = antennas.get(char, [])
                antenna_coords.append((i, j))
                antennas[char] = antenna_coords

        line = input.readline()
        i += 1

height = i  # EOF line index is "real height"

# part 1
for antenna, amtenna_coordinates in antennas.items():
    # coordinate combination are already sorted per row because the insertion is per row
    for coord1, coord2 in itertools.combinations(amtenna_coordinates, 2):
        # following operations assuming first coordinate row is smaller than second coordinate row
        if coord1[0] == coord2[0] and coord1[1] > coord2[1]:
            # horizontal line must have lower first coordinate column
            coord1, coord2 = coord2, coord1

        if coord1[1] == coord2[1] and coord1[0] > coord2[0]:
            # vertical line must have lower first coordinate row
            coord1, coord2 = coord2, coord1

        # dx and dy a bit not appropriate here, so using row and column
        d_row = coord2[0] - coord1[0]
        d_col = coord2[1] - coord1[1]

        antinodes.add((coord1[0] - d_row, coord1[1] - d_col))
        antinodes.add((coord2[0] + d_row, coord2[1] + d_col))

print('Part 1:', len([
    x for x in antinodes if 0 <= x[0] < height and 0 <= x[1] < width
]))

# part 2
for antenna, amtenna_coordinates in antennas.items():
    for coord1, coord2 in itertools.combinations(amtenna_coordinates, 2):
        if coord1[0] == coord2[0] and coord1[1] > coord2[1]:
            coord1, coord2 = coord2, coord1

        if coord1[1] == coord2[1] and coord1[0] > coord2[0]:
            coord1, coord2 = coord2, coord1

        d_row = coord2[0] - coord1[0]
        d_col = coord2[1] - coord1[1]

        # multiplier = 0 is the antenna coordinate itself
        multiplier = 0

        # repeated to the lower row until reaching boundary
        while True:
            new_coordinate = (
                coord1[0] - d_row * multiplier,
                coord1[1] - d_col * multiplier
            )

            if 0 <= new_coordinate[0] < height and 0 <= new_coordinate[1] < width:
                updated_antinodes.add(new_coordinate)
                multiplier += 1
            else:
                break

        multiplier = 0

        # repeated to the higher row until reaching boundary
        while True:
            new_coordinate = (
                coord2[0] + d_row * multiplier,
                coord2[1] + d_col * multiplier
            )

            if 0 <= new_coordinate[0] < height and 0 <= new_coordinate[1] < width:
                updated_antinodes.add(new_coordinate)
                multiplier += 1
            else:
                break

print('Part 2:', len(updated_antinodes))
