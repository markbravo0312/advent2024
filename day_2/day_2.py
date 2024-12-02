

FILENAME = "input.txt"


def part1():
    safe = 0
    tolerate = 0
    
    with open(FILENAME, 'r') as f: 
        lines = f.read().split('\n')
        for line in lines:
            t = list(map(int, line.split() ))  #cast to int
            stricly_inc_or_dec = (t == sorted(t) or t == sorted(t, reverse=True))
            acceptable = True
            for i in range(len(t) - 1) : 
                diff = abs(t[i] - t[i + 1])
                if not 1 <= diff <= 3 : 
                    acceptable = False 
            if acceptable and stricly_inc_or_dec:
                safe += 1
    print("Part 1: ", safe)
    return safe


def part2(): 
    with open(FILENAME, 'r') as f: 
        lines = f.read().split('\n')
        for line in lines : 
            t = list(map(int, line.split() ))
            
        
        
    
                
                
if __name__ == '__main__':
    part1()
    part2() 
    