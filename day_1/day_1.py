from numpy import loadtxt, sort

FILENAME = "input.txt"



def parse_input(filename) :
    data = loadtxt(filename, int)
    list1, list2 = sort(data.T)
    return list1, list2


def part1() :
    list1, list2 = parse_input(FILENAME)
    return sum(abs(list1 - list2))


def part2 () :
    list1, list2 = parse_input(FILENAME)
    freq = {}
    for item in list2: 
        freq[item] = freq.get(item, 0) + 1
    acc = sum(freq.get(elem, 0) * elem for elem in list1)
    return acc

if __name__ == "__main__":
    res1 = part1()
    res2 = part2()
    print("Result of part1 is: ", res1)
    print("Result of part2 is: ", res2)
    
        