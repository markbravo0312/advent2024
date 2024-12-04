

FILENAME = "input.txt"



def solve(): 
    with open(FILENAME, "r") as f:
        golden = "XMAS"
        s = f.read().split("\n")
        
        
        counter = 0
        counter2 = 0
        rows = len(s)
        cols = len(s[0])
        
        def matches(row, col, dir_row, dir_col) :
            try: 
                result = "X"
                for i in range(1,len(golden)):
                    new_row = row + dir_row * i
                    new_col = col + dir_col * i
                    if (new_row < 0 or new_col < 0):
                        return False
                    result += s[new_row][new_col]
                return result == golden
            except IndexError:
                return False
            
        def matches2(row, col):
            if row == 0 or col == 0 or row == rows-1 or col == cols-1:
                return False
            try:
                if (
                    (s[row + 1][col + 1] == 'M' and s[row - 1][col - 1] == 'S' and s[row + 1][col - 1] == 'M' and s[row - 1][col + 1] == 'S') or
                    (s[row + 1][col + 1] == 'M' and s[row - 1][col - 1] == 'S' and s[row + 1][col - 1] == 'S' and s[row - 1][col + 1] == 'M') or
                    (s[row + 1][col + 1] == 'S' and s[row - 1][col - 1] == 'M' and s[row + 1][col - 1] == 'M' and s[row - 1][col + 1] == 'S') or  
                    (s[row + 1][col + 1] == 'S' and s[row - 1][col - 1] == 'M' and s[row + 1][col - 1] == 'S' and s[row - 1][col + 1] == 'M')
                ): 
                    return True
            except IndexError:
                    return False
                
            
        
                 
        
        for row in range(rows):
            for col in range(cols) :
                if s[row][col] == "X" : 
                    counter += matches(row, col, 0, 1) 
                    counter += matches(row, col, 0, -1) 
                    counter += matches(row, col, 1, 0) 
                    counter += matches(row, col, -1, 0)
                    counter += matches(row, col, 1, 1) 
                    counter += matches(row, col, -1, -1) 
                    counter += matches(row, col, -1, 1)
                    counter += matches(row, col, 1, -1)
                if (s[row][col] == "A"):
                    if (matches2(row, col)):
                        counter2 += 1
            
        print("Result for part1: ", counter)
        print("Result for part2: ", counter2)              
                            
        return counter


                
if __name__ == "__main__" :
    solve()
        
        