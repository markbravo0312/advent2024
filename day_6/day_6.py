


FILENAME = "input.txt"
def part1() :
    f = open(FILENAME, "r")
    lines = f.read().split("\n")
    
    pos = [0,0]
    
    for i in range(0, len(lines)) :
        if "^" in lines[i]:
            pos[0] = i
            pos[1] = lines[i].index("^")
            break

    start_r = pos[0]
    start_c = pos[1]
        
    directions = [[-1,0], [0,1], [1,0], [0,-1]]
    curr_dir = 0
    
    
    s = {tuple(pos)}
    
    
    
    
    while True:
        new_r, new_c = pos[0] + directions[curr_dir][0], pos[1] + directions[curr_dir][1]

        if 0 <= new_r < len(lines) and 0 <= new_c < len(lines[0]):
            if lines[new_r][new_c] == '#':
                curr_dir = (curr_dir + 1) % 4  
            else:
                pos = [new_r, new_c]
                s.add(tuple(pos))
        else:
            break
    print("Result for part1: ", len(s))
    
    total2 = 0
        
    for cr  in range(len(lines)): 
        for cc in range(len(lines[0])) : 
            seen = set() 
            curr_row, curr_col = start_r, start_c
            curr_dir = 0
            while True:
                if (curr_row, curr_col, curr_dir) in seen:
                    total2 += 1
                    break
                
                seen.add((curr_row, curr_col, curr_dir))
                new_r, new_c = curr_row + directions[curr_dir][0], curr_col + directions[curr_dir][1]
                
                
                if not (0 <= new_r < len(lines)) or not (0 <= new_c < len(lines[0])): 
                    break
                if lines[new_r][new_c] == "#" or (new_r == cr and new_c == cc):
                    curr_dir = (curr_dir + 1) % 4  
                else:
                    curr_row = new_r
                    curr_col = new_c
                    
    print("result for part2: ", total2)
                    
                    
                    
    
        
    
if __name__ == "__main__" :
    res1 = part1()
    
    
            
        
        
        
        


