import re

FILENAME = "input.txt"


def read_file():
    with open(FILENAME, 'r') as f: 
        data = f.read().strip()
    return data
        
        
def part1(corrupted_memory: str) -> int:
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, corrupted_memory)
    
    total = sum(int(num1) * int(num2) for num1, num2 in matches)
    
    return total


def part2(corrupted_memory: str) -> int:
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    
    combined_pattern = f"{mul_pattern}|{do_pattern}|{dont_pattern}"
    total = 0
    
    flag = True
    for match in re.finditer(combined_pattern, corrupted_memory):
        if match.group(0) == "do()":
            flag = True
        elif match.group(0) == "don't()":
            flag = False 
        elif match.group(1) and match.group(2) : 
            if flag:
                num1, num2 = int(match.group(1)), int(match.group(2))
                total += num1 * num2  
    return total
                    


if __name__ == '__main__':
    data = read_file()
    res1 = part1(data)
    res2 = part2(data)
    print("Part 1: ", res1)
    print("Part 2: ", res2)
