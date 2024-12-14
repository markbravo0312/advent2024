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
    
    safety_factor = float('inf')
    iteration = None
        

    for i in range(ROWS * COLS):
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        
        for rob in robs: 
            x = rob[0]
            y = rob[1]
            vx = rob[2]
            vy = rob[3]
            
            next_x = (x + vx) % COLS
            next_y = (y + vy) % ROWS
            
            rob[0] = next_x
            rob[1] = next_y
            
            if next_x == COLS//2 or next_y == ROWS//2 : continue
            if 0 <= next_x <= (COLS//2)-1 :
                if 0 <= next_y <= (ROWS//2)-1:
                    q1 += 1
                else :
                    q3 += 1
            else:
                if 0 <= next_y <= (ROWS//2)-1:
                    q2 += 1
                else: 
                    q4 += 1
                    
        sf = q1 * q2 * q3 * q4
        if sf < safety_factor:
            safety_factor = sf
            iteration = i + 1
            
    print("result for part2: ", iteration)

    

    

            





        





if __name__ == "__main__" : 
    solve() 
    solve2()

