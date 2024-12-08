FILENAME = "input.txt" 

# each frequency staellitle has an antinode, with same delta as that
# satellite to other satellites.



def part1() : 
    antennas = {}
    
    
    lines = open(FILENAME, 'r').read().split("\n")
    numRows = len(lines)
    numCols = len(lines[0])
    
    
    
    antinodes = set()
    more_antinodes = set() 
    
    
    for i in range(0, numRows):
        for j in range(0, numCols):
            if lines[i][j].isalnum():
                if lines[i][j] not in antennas:
                    antennas[lines[i][j]] = []
            
                antennas[lines[i][j]].append((i,j))
            
    for _, value in antennas.items():
        for (r1, c1) in value:
            for (r2, c2) in value: 
                if (r1,c1) == (r2,c2):
                    continue 
            
                delta_r, delta_c = abs(r1 - r2), abs(c1 - c2)

                for fr, fc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    for (r3, c3) in [(r1, c1), (r2, c2)]:
                        r4, c4 = r3 + fr * delta_r, c3 + fc * delta_c
                        d1 = abs(r4 - r1) + abs(c4 - c1)
                        d2 = abs(r4 - r2) + abs(c4 - c2)
                        if (
                            (d1 == 2 * d2 or d1 * 2 == d2)
                            and 0 <= r4 < numRows
                            and 0 <= c4 < numCols
                            and (r4 - r1) * (c4 - c2) == (r4 - r2) * (c4 - c1)
                        ):
                            antinodes.add((r4, c4))
                            
    for row in range(numRows):
        for col in range(numCols):
            for _, value in antennas.items():
                for (r1, c1) in value:
                    for (r2, c2) in value: 
                        if (r1,c1) == (r2,c2):
                            continue 
                    
                        d1 = abs(row - r1) + abs(col - c1)
                        d2 = abs(row - r2) + abs(col - c2)
                         
                        delta_row_1 = row - r1
                        delta_row_2 = row - r2
                        delta_col_1 = col - c1
                        delta_col_2 = col - c2
                        
                        if (delta_row_1 * delta_col_2 == delta_row_2 * delta_col_1):
                            more_antinodes.add((row, col))
                        
                            
                        
            
                    
    p1 = len(antinodes)
    p2 = len(more_antinodes)
                    
    print("Result for part 1: ", p1)
    print("Result for part 2: ", p2)
    
    
if __name__ == "__main__" :
    part1() 
                
            
        
            
                    
            
        
    


