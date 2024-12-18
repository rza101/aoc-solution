import copy

disk_map = open('input.txt').read().rstrip()
disk = []  # now consists of tuple (id, length, free space)

for i in range(0, len(disk_map), 2):
    disk.append((
        i//2,
        int(disk_map[i]),
        # last block free space is always 0
        0 if i == len(disk_map) - 1 else int(disk_map[i+1])
    ))

# part 1
fragmented_disk = copy.deepcopy(disk)
i = 0

while not all([block[2] == 0 for block in fragmented_disk]):
    # if current block free space is not 0
    if fragmented_disk[i][2] != 0:
        # insert the last block after this block
        # with length equal to minimum of last block length and current block free space
        # and free space equal to maximum of 0 and (last block length - current block free space)
        fragmented_disk.insert(
            i + 1,
            (
                fragmented_disk[-1][0],
                min(fragmented_disk[-1][1], fragmented_disk[i][2]),
                max(0, fragmented_disk[i]
                    [2] - fragmented_disk[-1][1])
            )
        )

        if fragmented_disk[-1][1] <= fragmented_disk[i][2]:
            # if last block length is less than equal the current disk block free space
            # then remove the last block and set the later last block free space to 0
            fragmented_disk.pop()
            fragmented_disk[-1] = (
                fragmented_disk[-1][0],
                fragmented_disk[-1][1],
                0
            )
        else:
            # else decrease the length by the current block free space (allows fragmentation)
            fragmented_disk[-1] = (
                fragmented_disk[-1][0],
                fragmented_disk[-1][1] - fragmented_disk[i][2],
                0
            )

        # set the current block free space to 0
        fragmented_disk[i] = (
            fragmented_disk[i][0],
            fragmented_disk[i][1],
            0
        )

    i += 1

checksum_result = 0
i = 0

for block in fragmented_disk:
    for _ in range(block[1]):
        checksum_result += i * block[0]
        i += 1

print('Part 1:', checksum_result)

# part 2
reordered_disk = copy.deepcopy(disk)

# the logic is to fit the later block to earlier block if the free space is enough
r_index = len(reordered_disk) - 1

while r_index > 0:
    l_index = 0

    while r_index > l_index:
        # if earlier block free space is more than equal the later block length
        if reordered_disk[l_index][2] >= reordered_disk[r_index][1]:
            # remove the later block
            removed_block = reordered_disk.pop(r_index)

            # insert the later block after earlier block with free space equal to
            # (later block length - earlier free space), and this disallows fragmentation
            reordered_disk.insert(
                l_index + 1,
                (
                    removed_block[0],
                    removed_block[1],
                    reordered_disk[l_index][2] - removed_block[1]
                )
            )

            # set the earlier block free space to 0
            reordered_disk[l_index] = (
                reordered_disk[l_index][0],
                reordered_disk[l_index][1],
                0
            )

            # add the "current" later block free space with total length of removed block
            reordered_disk[r_index] = (
                reordered_disk[r_index][0],
                reordered_disk[r_index][1],
                reordered_disk[r_index][2] +
                removed_block[1] + removed_block[2]
            )

        l_index += 1

    r_index -= 1

checksum_result = 0
i = 0

for block in reordered_disk:
    for _ in range(block[1]):
        checksum_result += i * block[0]
        i += 1

    i += block[2]  # because disk is not fragmented

print('Part 2:', checksum_result)  # answer still wrong
