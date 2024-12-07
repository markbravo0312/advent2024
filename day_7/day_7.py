
FILENAME = "input.txt"

def rec_op_part1(result, op, running, j, nums):
    if j == len(nums):
        return running == result

    match op:
        case '*':
            temp = running * nums[j]
        case '+':
            temp = running + nums[j]

    if temp > result:
        return False
    else:
        return (rec_op_part1(result, '*', temp, j + 1, nums) or
                rec_op_part1(result, '+', temp, j + 1, nums))

def rec_op_part2(result, op, running, j, nums):
    if j == len(nums):
        return running == result

    match op:
        case '*':
            temp = running * nums[j]
        case '+':
            temp = running + nums[j]
        case '||':
            temp = int(str(running) + str(nums[j]))

    if temp > result:
        return False
    else:
        return (rec_op_part2(result, '*', temp, j + 1, nums) or
                rec_op_part2(result, '+', temp, j + 1, nums) or
                rec_op_part2(result, '||', temp, j + 1, nums))

def process_lines(rec_op_func):
    lines = open(FILENAME, "r").read().split("\n")
    total = 0

    for line in lines:
        vals = line.split(" ")
        vals[0] = vals[0][:-1]
        nums = list(map(int, vals))

        if (rec_op_func(nums[0], '*', nums[1], 2, nums) or
            rec_op_func(nums[0], '+', nums[1], 2, nums) or
            (rec_op_func == rec_op_part2 and 
             rec_op_func(nums[0], '||', nums[1], 2, nums))):
            total += nums[0]

    return total

def part1():
    result = process_lines(rec_op_part1)
    print("Result for part1:", result)

def part2():
    result = process_lines(rec_op_part2)
    print("Result for part2:", result)

if __name__ == "__main__":
    part1()
    part2()
