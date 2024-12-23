S = 70
og_grid = [['.'] * (S+1) for _ in range(S+1)]
from copy import deepcopy


f = open("input.txt", "r")
pairs = f.read().split("\n")




def solve(n): 
    grid = deepcopy(og_grid)
    for i in range(n) : 
        p=pairs[i]
        x,y = map(int, p.split(","))
        grid[y][x] = '#'
    
    q = []       #weight, r, c
    q.append( (0, 0 ))
    visited = set() 
    

    while len(q) > 0 :
        r, c = q.pop(0) 

        if r ==  c == S: 
            #print("Result to part1: ", weight)
            return True

        if (r,c) in visited: 
            continue

        visited.add((r,c))

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]: 
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r <= S and 0 <= new_c <= S and grid[new_r][new_c] != "#":
                q.append(  (new_r, new_c)  ) 

    return False



def solve2() : 
    left = 1024
    right = len(pairs) - 1

    while left < right : 
        mid = (left + right) // 2
        if solve(mid): 
            left = mid + 1
        else: 
            right = mid - 1

    print("Result to part2: ", pairs[left])


    


if __name__ == "__main__" : 
    solve(1024)     
    
    solve2()

    


