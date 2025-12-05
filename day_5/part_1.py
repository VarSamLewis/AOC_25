import numpy as np

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


def merge_ranges(ranges):
    """Merge overlapping ranges efficiently without using arrays."""
    if not ranges:
        return []

    # Sort ranges by their start point
    sorted_ranges = sorted(ranges, key=lambda x: x[0])

    merged = [sorted_ranges[0]]

    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]

        # Check if current range overlaps or is adjacent to the last merged range
        if current_start <= last_end + 1:
            # Merge by extending the end if necessary
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            # No overlap, add as a new range
            merged.append((current_start, current_end))

    return merged


def main():
    ranges = fileread(FILENAME_RNG)
    ids = fileread(FILENAME_IDS)
    
    parsed_ranges = [parserange(r) for r in ranges]    
    fresh_ids = 0
    fresh_ids_set = {
          int(id)
          for id in ids
          if any(lower <= int(id) <= upper for lower, upper in parsed_ranges)
      }

    return len(fresh_ids_set), sorted(fresh_ids_set)


if __name__ == '__main__':
    fresh_ids, fresh_ids_list = main()

    print(fresh_ids)

