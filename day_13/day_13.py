import re


f = open("input.txt", "r").read()




def hatemath(ax, ay, bx, by, px, py, part2):
    timesa = (px * by - py * bx) / (ax * by - ay * bx)
    timesb = (px - timesa * ax) / bx

    if timesa % 1 == timesb % 1 == 0: 
        if part2:
            return int( 3*timesa + timesb) 
        else: 
            if (timesa <= 100 and timesb <= 100):
                return int( 3*timesa + timesb)  
    
    return 0

#  px = timesa * ax + timesb * bx,     <-> timesa = (px - timesb * bx) / (ax) , timesb = (py - timesa * ay) / by
#  py = timesa * ay + timesb * by      <->  timesa = (px * by - py * bx) / (ax * by - ay * bx)

def solve(): 
    total = 0
    total2 = 0
    for block in f.split("\n\n"):
        ax, ay, bx, by, px, py = map(int, re.findall(r'\d+', block))
        total += hatemath(ax, ay, bx, by, px, py, False)
        total2 += hatemath(ax, ay, bx, by, px+10000000000000, py+10000000000000, True)


    print("Result for part1 is: ", total)
    print("Result for part2 is: ", total2)



if __name__ == "__main__":
    solve() 