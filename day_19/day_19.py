from functools import cache
input_str = open("input.txt", "r").read().split("\n\n")

towels = [x.strip() for x in input_str[0].split(",")]
patterns = input_str[1].split("\n")


@cache
def recSolve(pattern) : 
    if pattern == "" :
        return True
    
    for t in towels: 
        n = len(t)
        if n > len(pattern) : continue

        if  pattern[:n] == t : 
            if recSolve(pattern[n:]) :
                return True
            
    return False

@cache
def recCount(pattern) : 
    if pattern == "":
        return 1
    
    count = 0
    
    for t in towels: 
        n = len(t)
        if n > len(pattern) : continue

        if  pattern[:n] == t : 
            count += recCount(pattern[n:])
            
    return count


    


def solve() : 
    total = 0
    count = 0
    for p in patterns : 
        if recSolve(p) :
            total += 1
        count += recCount(p)

    print("Result to part1: ", total )
    print("Result to part2: ", count)




if __name__ == "__main__" : 
    solve()

            
        
