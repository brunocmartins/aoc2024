from utils.input_reader import read_puzzle_input
from utils.utils import timing


def parse_input(puzzle_input):
    available_towels = [towel for row in puzzle_input[:puzzle_input.index("")] for towel in row.split(", ")]
    patterns = puzzle_input[puzzle_input.index("") + 1:]
    
    return available_towels, patterns

def get_possible_patterns(available_towels, patterns):
    answers = 0
    seen = {}

    def test_words(words, pattern):
        if pattern in seen:
            return seen[pattern]

        ans = 0
        if not pattern:
            ans = 1

        for word in words:
            if pattern.startswith(word):
                ans += test_words(words, pattern[len(word):])

        seen[pattern] = ans

        return ans

    for pattern in patterns:
        answers += test_words(available_towels, pattern)

    return answers

def main():
    with timing():
        puzzle_input = read_puzzle_input()
        available_towels, patterns = parse_input(puzzle_input)
        print(get_possible_patterns(available_towels, patterns))

if __name__ == "__main__":
    main()
