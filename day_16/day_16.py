from collections import defaultdict
from queue import PriorityQueue

f = open("input.txt", "r").read()
grid = f.split("\n")
ROWS = len(grid)
COLS = len(grid[0])
grid = [[grid[r][c] for c in range(COLS)] for r in range(ROWS)]

def solve() :
    directions = [(0,1), (1,0), (0,-1), (-1,0)]    # right, down, left, up 
    dist = {}
    seen = set() 
    solution = None
    sr, sc = [(r,c) for r, row in enumerate(grid) for c, val in enumerate(row) if val == 'S'][0]
    end_pos = [(r,c) for r, row in enumerate(grid) for c, val in enumerate(row) if val == 'E'][0]
    q = PriorityQueue() 
    q.put( (0, sr, sc, 0) )

    while not q.empty() :  
        cost, r, c, curr_dir = q.get()

        if r == end_pos[0] and c == end_pos[1] and solution is None: 
            solution = cost

        if (r,c, curr_dir) not in dist : 
            dist[(r,c,curr_dir)] = cost

        if (r,c,curr_dir) in seen: 
            continue

        seen.add((r,c,curr_dir))
        dr,dc = directions[curr_dir]    
        new_r, new_c = r + dr, c + dc


        if 0 <= new_r <  ROWS and 0 <= new_c < COLS and grid[new_r][new_c] != '#': 
            q.put( (cost + 1, new_r, new_c , curr_dir ) ) 

        q.put( (cost + 1000, r, c, (curr_dir+1)%4) ) 
        q.put( (cost + 1000, r, c, (curr_dir+3)%4 ) )

    

    
    q2 = PriorityQueue() 
    seen2 = set()
    for d in range(4) : 
        q2.put( (0, end_pos[0], end_pos[1] , d) ) 
    dist2 = {}
    while not q2.empty() :
        
        cost, r, c, direction = q2.get() 
        if (r, c, (2+direction) % 4) not in dist2: 
            dist2[(r,c,(2+direction)%4 )] = cost

        if (r, c,direction) in seen2: 
            continue
        seen2.add((r,c,direction))
        dr, dc = directions[direction]
        new_r, new_c = r+dr, c+dc
        if 0 <= new_c < COLS and 0 <= new_r < ROWS and grid[new_r][new_c] != "#": 
            q2.put((cost + 1, new_r, new_c, direction))

        q2.put((cost + 1000, r, c, (direction+1) %4))
        q2.put((cost + 1000, r, c, (direction+3) %4))

    matching = set() 

    for r in range(ROWS) : 
         for c in range(COLS) : 
            for direction in range(4) : 
                if (r, c, direction) in dist and (r,c, direction) in dist2 and dist[(r,c,direction)] + dist2[(r,c,direction)] == solution:
                    matching.add((r,c))
        

    print("Result to part1: ", solution)
    print("Result to part2: ", len(matching))



        


if __name__ == "__main__": 
    solve() 