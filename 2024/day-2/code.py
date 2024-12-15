def sign(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1


safe_count = 0
safe_tolerable_count = 0

with open('input.txt', 'r') as input:
    line = input.readline()

    while line:
        levels = [int(x) for x in line.split()]

        levels_diff = [levels[i] - levels[i-1] for i in range(1, len(levels))]
        levels_diff_abs = [abs(x) for x in levels_diff]
        levels_diff_sign = [sign(x) for x in levels_diff]

        if min(list(set(levels_diff_abs))) >= 1 and max(list(set(levels_diff_abs))) <= 3 and len(set(levels_diff_sign)) == 1:
            safe_count += 1
            safe_tolerable_count += 1
        else:
            # brute force...
            for removed_level_idx in range(len(levels)):
                adjusted_levels = levels.copy()
                adjusted_levels.pop(removed_level_idx)

                adjusted_levels_diff = [adjusted_levels[i] - adjusted_levels[i-1]
                                        for i in range(1, len(adjusted_levels))]
                adjusted_levels_diff_abs = [abs(x)
                                            for x in adjusted_levels_diff]
                adjusted_levels_diff_sign = [
                    sign(x) for x in adjusted_levels_diff]

                if min(list(set(adjusted_levels_diff_abs))) >= 1 and max(list(set(adjusted_levels_diff_abs))) <= 3 and len(set(adjusted_levels_diff_sign)) == 1:
                    safe_tolerable_count += 1
                    break

        line = input.readline()

print('Part 1:', safe_count)
print('Part 2:', safe_tolerable_count)
