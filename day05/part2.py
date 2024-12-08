from utils.input_reader import read_puzzle_input
from day05.part1 import parse_input, sum_middle_pages


def _check_valid(rules, update) -> bool:
    for idx, page in enumerate(update):
        try:
            invalid = set(rules[page]).intersection(set(update[:idx]))
        except KeyError:
            invalid = None            
        if invalid:
            return False
    
    return True

def _get_invalid_params(rules, update):
    invalid_params = []
    for idx, page in enumerate(update):
        try:
            invalid = set(rules[page]).intersection(set(update[:idx]))
        except KeyError:
            invalid = None            
        if invalid:
            invalid_params.append((page, invalid))

    return invalid_params


def get_unordered_updates(rules: dict[str, list], updates: list[str]):
    invalid_updates = {}
    for update in updates:
        for idx, page in enumerate(update):
            try:
                invalid = set(rules[page]).intersection(set(update[:idx]))
            except KeyError:
                invalid = None            
            if invalid:
                if tuple(update) not in invalid_updates:
                    invalid_updates[tuple(update)] = []
                invalid_updates[tuple(update)].append((page, invalid))
        else:
            continue
    
    return invalid_updates

def order_updates(rules, invalid_updates):
    valid_updates = []
    idx = 0
    still_invalid = list(invalid_updates.keys())

    while idx < len(still_invalid) and idx < 5000:
        for page, invalid_set in invalid_updates[still_invalid[idx]]:

            page_idx = tuple(still_invalid[idx]).index(page)
            reordered_update = list(still_invalid[idx][:page_idx] + still_invalid[idx][page_idx+1:])
            reordered_update.insert(tuple(still_invalid[idx]).index(next(iter(invalid_set))), page)
            rr = tuple(reordered_update)

            if _check_valid(rules, rr):
                valid_updates.append(rr)
                print("Valid Update: ", rr)
            else:
                still_invalid.append(rr)
                invalid_updates[tuple(rr)] = _get_invalid_params(rules, rr)
                print("Invalid Update: ", rr)
                idx += 1
                break

            idx += 1
            
    return valid_updates

def main():
    puzzle_input = read_puzzle_input(sample=False)
    page_rules, updates = parse_input(puzzle_input)
    unordered_updates = get_unordered_updates(page_rules, updates)
    ordered_updates = order_updates(page_rules, unordered_updates)
    print(sum_middle_pages(ordered_updates))


if __name__ == "__main__":
    main()
