from collections import deque

input_str = open("input.txt", "r" ).read().split("\n") 
COLS = len(input_str[0]) 
ROWS = len(input_str)
grid = [[input_str[r][c] for c in range(COLS)] for r in range(ROWS) ] 

sr, sc = 0,0
er, ec = 0,0 

for r, row in enumerate(grid) :
    for c, val in enumerate(row) : 
        if (val == "S"):
            sr, sc = r, c
        if (val == "E") : 
            er, ec = r, c

seconds_from_start = {} 
visited = set() 

q = deque() 
q.append( (sr, sc, 0) ) 
time_to_end = None
while q: 
    r,c, time = q.popleft()



    if (r,c) in visited: 
        continue

    seconds_from_start[(r,c)] = time

    if r == er and c == ec: 
        time_to_end = time
        break

    visited.add((r,c))

    for dr, dc in [(0,1), (0,-1), (-1,0), (1,0)]: 
        new_r, new_c = r + dr, c + dc
        if 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] != "#" and (new_r, new_c) not in visited:
            q.append( (new_r, new_c, time + 1) ) 



def solve() : 
    count = 0
    for r,c in visited: 
        for dr, dc in [(0,1), (0,-1), (-1,0), (1,0)] : 
            new_r, new_c = r + 2*dr, c + 2*dc
            wallr, wallc = r + dr, c + dc
            if 0<= wallr < ROWS and 0 <= wallc < COLS and 0 <= new_r < ROWS and 0 <= new_c < COLS:
                if grid[wallr][wallc] == "#" and grid[new_r][new_c] != "#" and seconds_from_start[(new_r, new_c)] > seconds_from_start[(r,c)]:
                    saved = seconds_from_start[(new_r, new_c)]  - seconds_from_start[(r,c)] - 2
                    if saved >= 100: count += 1

    print("Result to part 1:", count)



def solve2() : 

    count = 0

    for r,c in visited: 
        q = deque() 
        cheat_visited = set() 
        q.append( (0,r,c)  )
        startsec = seconds_from_start[(r,c)]

        while q : 
            
            currsec, curr_r, curr_c = q.popleft()     

            if (curr_r, curr_c) in cheat_visited:
                continue

            if currsec > 20 : 
                continue

            cheat_visited.add( (curr_r, curr_c) )
            
            if grid[curr_r][curr_c] != "#" :
                if seconds_from_start[ (curr_r,curr_c) ] > startsec: 
                    saved = seconds_from_start[(curr_r,curr_c)]  - startsec - currsec
                    if saved >= 100 : count += 1

            for dr, dc in [(0,1), (0,-1), (-1,0), (1,0)] : 
                new_r, new_c = curr_r + dr, curr_c + dc
                if 0 <= new_r < ROWS and 0 <= new_c < COLS and (new_r, new_c) not in cheat_visited:
                    q.append( (currsec + 1, new_r, new_c ) ) 

    print("Result to part2: ", count)







if __name__ == "__main__" : 
    solve() 
    solve2() 
