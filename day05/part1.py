from utils.input_reader import read_puzzle_input


def parse_input(puzzle_input):
    break_idx = puzzle_input.index("")

    updates = puzzle_input[break_idx+1:]
    updates = [list(map(int, item.split(","))) for item in updates]

    rules = puzzle_input[:break_idx]
    page_rules = {}
    for rule in rules:
        src, dest = map(int, rule.split("|"))
        if src not in page_rules:
            page_rules[src] = []
        page_rules[src].append(dest)

    return page_rules, updates

def sum_middle_pages(valid_updates):
    return sum([v_update[int((len(v_update)-1)/2)] for v_update in valid_updates])

def get_ordered_updates(rules: dict[str, list], updates: list[str]):
    valid_updates = []
    for update in updates:
        for idx, page in enumerate(update):
            try:
                invalid = set(rules[page]).intersection(set(update[:idx]))
            except KeyError:
                invalid = None            
            if invalid:
                print(f"Invalid: {invalid}")
                break
        else:
            valid_updates.append(update)
    
    return valid_updates

def main():
    puzzle_input = read_puzzle_input(sample=False)
    page_rules, updates = parse_input(puzzle_input)
    ordered_updates = get_ordered_updates(page_rules, updates)
    print(sum_middle_pages(ordered_updates))


if __name__ == "__main__":
    main()
