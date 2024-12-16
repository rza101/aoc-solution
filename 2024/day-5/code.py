import copy

succeeding_pages_rule = {}
update_list = []

with open('input.txt', 'r') as input:
    # rules
    line = input.readline()

    while line != '\n':
        splitted_line = line.split('|')

        first_number = int(splitted_line[0])
        second_number = int(splitted_line[1])

        new_rule = succeeding_pages_rule.get(first_number, set())
        new_rule.add(second_number)

        succeeding_pages_rule[first_number] = new_rule

        line = input.readline()

    # updated pages
    line = input.readline()

    while line:
        splitted_line = line.split(',')
        update_list.append([int(x) for x in splitted_line])

        line = input.readline()

middle_page_sum = 0
middle_page_corrected_sum = 0

for update in update_list:
    is_valid = True

    for i in range(len(update)):
        rule = succeeding_pages_rule.get(update[i], set())
        succeeding_pages = update[i+1:]

        # if succeeding pages for a number is missing any number from the rule
        # then this update is not valid
        if len(list(set(succeeding_pages) - rule)) != 0:
            is_valid = False
            break

    if is_valid:
        middle_page_sum += update[len(update) // 2]
    else:
        corrected_update = copy.deepcopy(update)

        # the logic is to reorder page update from the last index
        # so it have all rules that is on the update
        #
        # every number that has a rule must have succeeding pages
        # so if the succeeding pages for the page is on the lower index (or preceeding the page)
        # it is moved to the index before the first index of rules that is found
        #
        # after doing this for a index until the index is valid, the index is moved -1 and so on
        # until all index is processed
        for i in reversed(range(len(corrected_update))):
            while True:
                preceeding_pages = set(corrected_update[:i])
                rule = succeeding_pages_rule.get(corrected_update[i], set())
                rule_pages_on_preceeding_pages = preceeding_pages.intersection(
                    rule)

                if len(list(rule_pages_on_preceeding_pages)) == 0:
                    break
                else:
                    first_matching_index = min([index for index, page in enumerate(
                        rule_pages_on_preceeding_pages) if page in rule])
                    corrected_update.insert(
                        first_matching_index, corrected_update.pop(i))

        middle_page_corrected_sum += corrected_update[len(
            corrected_update) // 2]

print('Part 1:', middle_page_sum)
print('Part 2:', middle_page_corrected_sum)
