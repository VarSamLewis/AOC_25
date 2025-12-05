FILENAME_RNG = "ranges.txt"
FILENAME_IDS = "ids.txt"

def fileread(filename: str):
    with open(filename, 'r') as f:
        content = [line.rstrip('\n') for line in f if line.strip()]
    return content


def parserange(range_input):
    range_str = range_input.strip()
    
    # Skip empty lines
    if not range_str:
        return None
    
    lower, upper = range_str.split('-')
    return int(lower.strip()), int(upper.strip())


def mergeranges(ranges):
    
    ranges_sorted = sorted(ranges, key=lambda x: x[0])

    merged = [ranges_sorted[0]]

    for current_start, current_end in ranges_sorted[1:]:
        last_start, last_end = merged[-1]

        if current_start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            merged.append((current_start, current_end))

    return merged

def main():
    ranges = fileread(FILENAME_RNG)
    ids = fileread(FILENAME_IDS)

    parsed_ranges = [parserange(r) for r in ranges]

    
    merged_ranges = mergeranges(parsed_ranges)

    
    total_len = 0
    for lower, upper in merged_ranges:
        range_len = 1 + (upper - lower)
        total_len += range_len

    return total_len

if __name__ == '__main__':
    count = main()

    print(count)

