import argparse
import contextlib
import os
import re
import sys
import time
import urllib.request
from typing import Generator


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

@contextlib.contextmanager
def timing(name: str = '') -> Generator[None, None, None]:
    before = time.time()
    try:
        yield
    finally:
        after = time.time()
        t = (after - before) * 1000
        unit = 'ms'
        if t < 100:
            t *= 1000
            unit = 'μs'
        if name:
            name = f' ({name})'
        print(f'> {int(t)} {unit}{name}', file=sys.stderr, flush=True)

def _get_cookie_headers() -> str:
    with open(f"{CURRENT_DIR}/../.env") as f:
        content = f.read().strip()
    
    return {"Cookie": content, "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}

def get_input(year: int, day: int) -> str:
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    req = urllib.request.Request(url, headers=_get_cookie_headers())
    return urllib.request.urlopen(req).read().decode()

def get_year_day() -> tuple[int, int]:
    cwd = os.getcwd()
    day_s = os.path.basename(cwd)
    year_s = os.path.basename(os.path.dirname(cwd))

    if not day_s.startswith('day') or not year_s.startswith('aoc'):
        raise AssertionError(f'unexpected working dir: {cwd}')

    return int(year_s[len('aoc'):]), int(day_s[len('day'):])

def download_input() -> int:
    parser = argparse.ArgumentParser()
    parser.parse_args()

    year, day = get_year_day()


    for i in range(5):
        try:
            s = get_input(year, day)
        except urllib.error.URLError as e:
            print(f'zzz: not ready yet: {e}')
            time.sleep(1)
        else:
            break
    else:
        raise SystemExit('timed out after attempting many times')

    with open('input.txt', 'w') as f:
        f.write(s)
    os.chmod('input.txt', 0o400)

TOO_QUICK = re.compile('You gave an answer too recently.*to wait.')
WRONG = re.compile(r"That's not the right answer.*?\.")
RIGHT = "That's the right answer!"
ALREADY_DONE = re.compile(r"You don't seem to be solving.*\?")

def _post_answer(year: int, day: int, part: int, answer: int) -> str:
    params = urllib.parse.urlencode({'level': part, 'answer': answer})
    req = urllib.request.Request(
        f'https://adventofcode.com/{year}/day/{day}/answer',
        method='POST',
        data=params.encode(),
        headers=_get_cookie_headers(),
    )
    resp = urllib.request.urlopen(req)

    return resp.read().decode()

def submit_solution() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("year", type=int, help="year of the challenge")
    parser.add_argument("day", type=int, help="day of the challenge")
    parser.add_argument('--part', type=int, required=True)
    args = parser.parse_args()

    answer = int(sys.stdin.read())

    print(f'answer: {answer}')

    contents = _post_answer(args.year, args.day, args.part, answer)

    for error_regex in (WRONG, TOO_QUICK, ALREADY_DONE):
        error_match = error_regex.search(contents)
        if error_match:
            print(f'\033[41m{error_match[0]}\033[m')
            return 1

    if RIGHT in contents:
        print(f'\033[42m{RIGHT}\033[m')
        return 0
    else:
        # unexpected output?
        print(contents)
        return 1
