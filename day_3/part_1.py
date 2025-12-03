filename = 'input.txt'

def fileread(filename: str):
    with open(filename, 'r') as f:
        content = [line.rstrip('\n') for line in f]
    return content


def extract_two_highest_nums(line: str):
    first_idx = line.index(max(line))

    if first_idx < len(line) - 1:
        second = max(line[first_idx + 1:])
        return int(line[first_idx] + second)
    else:
        
        sorted_digits = sorted(set(line), reverse=True)
        if len(sorted_digits) >= 2:
            second_max = sorted_digits[1]
            max_digit = sorted_digits[0]
            return int(second_max + max_digit)
        else:
            return int(line[0] + line[1])

def main():
    content = fileread(filename)

    total = 0
    for line in content:
        result = extract_two_highest_nums(line)
        total += result
    total
    return total

if __name__ == '__main__':
	print(main())
