from typing import List

filename = 'input.txt'
num_reps = 2

def fileread(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        content = f.read().strip()
        return content.split(',')

def is_repeated_pattern(num: int) -> bool:
    s = str(num)
    length = len(s)

    for pattern_len in range(1, length):
        if length % pattern_len == 0:
            reps = length // pattern_len
            if reps == num_reps:
                pattern = s[:pattern_len]
                if pattern * reps == s:
                    return True
    return False

def geninvalidID(start: int, end: int) -> List[int]:
    invalid_IDs = []

    for num in range(start, end + 1):
        if is_repeated_pattern(num):
            invalid_IDs.append(num)

    return invalid_IDs

def splitrange(range_str: str) -> List[int]:
    return list(map(int, range_str.split('-')))

def sumivalidIDs(invalid_IDs: List[int]) -> int:
    return sum(invalid_IDs)

def main():
    ranges = fileread(filename)

    full_invalid_IDs = []
    for range_str in ranges:
        start, end = splitrange(range_str)
        partial_invalid_IDs = geninvalidID(start, end)
        full_invalid_IDs.extend(partial_invalid_IDs)

    return sumivalidIDs(full_invalid_IDs)

if __name__ == '__main__':
    print(main())
