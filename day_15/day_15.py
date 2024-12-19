
f = open("input.txt", "r").read() 
input = f.split("\n\n")


grid = [list(row) for row in input[0].split("\n")]
instructions = input[1] 

gridPart2 = []



for row in grid: 
    r = []
    for c in row: 
        match c : 
            case '#': 
                r.extend(['#', '#'])
            case 'O':
                r.extend(['[', ']'])
            case '.':
                r.extend(['.', '.'])
            case '@':
                r.extend(['@', '.'])
            case _: 
                raise Exception("Not recognized character")
    gridPart2.append(r)

for row in gridPart2:
    print("".join(row))



def moveUp(r, c):
    if grid[r-1][c] == 'O':
        moveUp(r-1, c)
    if grid[r-1][c] == '[':
        moveUp(r-1,c)
        moveUp(r-1, c+1)
    elif grid[r-1][c] == ']':
        moveUp(r-1,c)
        moveUp(r-1,c-1)
    grid[r-1][c] = grid[r][c]
    grid[r][c] = '.'
    return (r-1, c)

def moveDown(r, c):
    if grid[r+1][c] == 'O':
        moveDown(r+1, c)
    
    grid[r+1][c] = grid[r][c]
    grid[r][c] = '.'
    return (r+1, c)

def moveRight(r, c):
    if grid[r][c+1] == 'O':
        moveRight(r, c+1)
    grid[r][c+1] = grid[r][c]
    grid[r][c] = '.'
    return (r, c+1)

def moveLeft(r, c):
    if grid[r][c-1] == 'O':
        moveLeft(r, c-1)
    grid[r][c-1] = grid[r][c]
    grid[r][c] = '.'
    return (r, c-1)


def canMoveUp(r, c):
    if r <= 0:
        return False
    if grid[r-1][c] == '#':
        return False
    if grid[r-1][c] == 'O':
        return canMoveUp(r-1, c)
    return True

def canMoveDown(r, c):
    if r >= len(grid) - 1:
        return False
    if grid[r+1][c] == '#':
        return False
    if grid[r+1][c] == 'O':
        return canMoveDown(r+1, c)
    
    return True

def canMoveRight(r, c):
    if c >= len(grid[0]) - 1:
        return False
    if grid[r][c+1] == '#':
        return False
    if grid[r][c+1] == 'O':
        return canMoveRight(r, c+1)
    return True

def canMoveLeft(r, c):
    if c <= 0:
        return False
    if grid[r][c-1] == '#':
        return False
    if grid[r][c-1] == 'O':
        return canMoveLeft(r, c-1)
    return True


check_viable = {"^": canMoveUp, "v": canMoveDown, ">": canMoveRight, "<": canMoveLeft}
move_op = {"^": moveUp, "v": moveDown, ">": moveRight, "<": moveLeft}


def canMoveUpPart2(r,c) :
    if r <= 0 : 
        return False
    if gridPart2[r-1][c] == '#':
        return False 
    if gridPart2[r-1][c] == '[':
        return canMoveUpPart2(r-1,c) and canMoveUpPart2(r-1,c+1) 
    if gridPart2[r-1][c] == ']':
        return canMoveUpPart2(r-1,c) and canMoveUpPart2(r-1,c-1)   
    
    return True

def canMoveDownPart2(r,c) :
    if r >= len(gridPart2) - 1 : 
        return False
    if gridPart2[r+1][c] == '#':
        return False 
    if gridPart2[r+1][c] == '[':
        return canMoveDownPart2(r+1,c) and canMoveDownPart2(r+1,c+1) 
    if gridPart2[r+1][c] == ']':
        return canMoveDownPart2(r+1,c) and canMoveDownPart2(r+1,c-1)  
    
    return True
    
def canMoveLeftPart2(r,c) :
    if c <= 0:
        return False
    
    if gridPart2[r][c-1] == '#':
        return False
    
    if gridPart2[r][c-1] == ']':
        return canMoveLeftPart2(r, c - 2)
    return True

def canMoveRightPart2(r,c) :
    if c >= len(gridPart2[0]) - 1 :
        return False
    
    if gridPart2[r][c + 1] == "#" :
        return False
    
    if gridPart2[r][c+1] == "[" :
        return canMoveRightPart2(r, c+2)
    
    return True 


def moveUpPart2(r, c):
    if gridPart2[r-1][c] == '[':
        moveUpPart2(r-1,c)
        moveUpPart2(r-1, c+1)
    elif gridPart2[r-1][c] == ']':
        moveUpPart2(r-1,c)
        moveUpPart2(r-1,c-1)

    gridPart2[r-1][c] = gridPart2[r][c]
    gridPart2[r][c] = '.'
    return (r-1, c)


def moveDownPart2(r,c) :
    if gridPart2[r+1][c] == '[' : 
        moveDownPart2(r+1,c)
        moveDownPart2(r+1,c+1)
    elif gridPart2[r+1][c] == ']': 
        moveDownPart2(r+1,c)
        moveDownPart2(r+1,c-1)

    gridPart2[r+1][c] = gridPart2[r][c]
    gridPart2[r][c] = '.'
    return (r+1,c)

def moveRightPart2(r,c) : 
    if gridPart2[r][c+1] == '[':
        moveRightPart2(r, c+2)
        moveRightPart2(r, c+1)
    
    gridPart2[r][c+1] = gridPart2[r][c]
    gridPart2[r][c] = '.'
    return (r,c+1)

def moveLeftPart2(r,c): 
    if gridPart2[r][c-1] == ']': 
        moveLeftPart2(r,c-2)
        moveLeftPart2(r, c-1) 

    gridPart2[r][c-1] = gridPart2[r][c]
    gridPart2[r][c] = '.'
    return (r, c-1)


    

check_viable2 = {"^": canMoveUpPart2, "v": canMoveDownPart2, ">": canMoveRightPart2, "<": canMoveLeftPart2}
move_op2 = {"^": moveUpPart2, "v": moveDownPart2, ">": moveRightPart2, "<": moveLeftPart2}


def solve():
    curr_pos = [(r, c) for r, row in enumerate(grid) for c, val in enumerate(row) if val == '@'][0]
    r, c = curr_pos
    curr_pos2 = [(r, c) for r, row in enumerate(gridPart2) for c, val in enumerate(row) if val == '@'][0]
    r2, c2 = curr_pos2
    total = 0
    total2 = 0

    for char in instructions:
        if char == '\n':
            continue
        if check_viable[char](r, c):
            curr_pos = move_op[char](r, c)
            r, c = curr_pos

        if check_viable2[char](r2,c2): 
            curr_pos2 = move_op2[char](r2,c2)
            r2, c2 = curr_pos2
        

    for i, row in enumerate(grid) :
        for j, char in enumerate(row) :
            if char == 'O':
                total += 100*i + j

    for i, row in enumerate(gridPart2) :
        for j, char in enumerate(row) :
            if char == '[': 
                total2 += 100*i + j

    print("Solution for part1: ", total )
    print("Solution for part2: ", total2)







if __name__ == "__main__" : 
    solve() 
    