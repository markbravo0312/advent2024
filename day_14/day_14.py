import re


ROWS = 103
COLS = 101


robots = open("input.txt", "r").read().split("\n")



def solve(): 
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for r in robots:
        x,y,vx,vy = map(int, re.findall(r'-?\d+', r))
        end_x = (vx * 100 + x) % COLS
        end_y = (vy * 100 + y) % ROWS
        
        #print("for:", x, ",", y, "velocity: ", vx, ",", vy, "got:", end_x, ",", end_y )
        
        if end_x == COLS//2 or end_y == ROWS//2 : continue
        if 0 <= end_x <= (COLS//2)-1 :
            if 0 <= end_y <= (ROWS//2)-1:
                q1 += 1
            else :
                q3 += 1
        else:
            if 0 <= end_y <= (ROWS//2)-1:
                q2 += 1
            else: 
                q4 += 1

    print("Result for part1: ", q1 * q2 * q3 * q4 )


def solve2() :
    robs = []
    for r in robots: 
        x,y,vx,vy = map(int, re.findall(r'-?\d+', r))

        robs.append( [x,y,vx,vy] )

    for i in range(100):
        grid = [[' '] * 101 for _ in range(103)]
        for rob in robs: 
            x = rob[0]
            y = rob[1]
            vx = rob[2]
            vy = rob[3]
            if grid[y][x] == ' ':
                grid[y][x] = '1'
            else : 
                grid[y][x] = str(int(grid[y][x]) + 1)
            
            rob[0] = (x + vx) % COLS
            rob[1] = (y + vy) % ROWS

        print("for second:", i)
        print('\n'.join(map(''.join, grid)))

            





        





if __name__ == "__main__" : 
    solve() 
    solve2()

