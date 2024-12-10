from collections import deque

f = open("input.txt", "r").read()
grid = [ [int(char) for char in line] for line in f.split("\n") ]
rows = len(grid)
cols = len(grid[0])




def score(r, c): 
    q = deque( [(r,c)] ) 
    visited = set((r,c)) 
    
    total = 0
    
    while len(q) > 0:
        x1, x2 = q.popleft()
        val = grid[x1][x2]
        
        for new_r, new_c in [ (x1 + 1, x2),  (x1 - 1, x2), (x1, x2 + 1), (x1, x2 - 1) ] :
            if new_r < 0 or new_c < 0 or new_r >= rows or new_c >= cols: continue
            if grid[new_r][new_c] != val + 1: continue
            if (new_r, new_c) in visited: continue
            visited.add( (new_r,new_c) )
            if grid[new_r][new_c] == 9 :
                total += 1
            else: 
                q.append( (new_r, new_c))
            
    return total
       

def rating(r,c):
    q = deque( [(r,c)] ) 
   
    
    total = 0
    
    while len(q) > 0:
        x1, x2 = q.popleft()
        val = grid[x1][x2]
        
        for new_r, new_c in [ (x1 + 1, x2),  (x1 - 1, x2), (x1, x2 + 1), (x1, x2 - 1) ] :
            if new_r < 0 or new_c < 0 or new_r >= rows or new_c >= cols: continue
            if grid[new_r][new_c] != val + 1: continue
            if grid[new_r][new_c] == 9 :
                total += 1
            else: 
                q.append( (new_r, new_c))
            
                
                        
    return total
    
                
            
    


def solve() :
    total = 0
    total_2 = 0
    
    trail_starts = [(r,c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]
    for r,c in trail_starts: 
        total += score(r,c)
        total_2 += rating(r,c)
        
    
        
        
    print("Result for part1: ", total)
    print("Result for part2: ", total_2)
    

if __name__ == "__main__":
    solve()