from collections import deque
import scipy
lines = open("input.txt", "r").read().split("\n")

rows = len(lines)
cols = len(lines[0])

grid = { (r,c):lines[r][c] for r in range(rows) for c in range(cols) }

union_find = scipy.cluster.hierarchy.DisjointSet( grid )
for ( r, c ), val in grid.items():
    for n in ( ( r - 1, c ), ( r + 1,  c),
               ( r, c - 1 ), ( r, c + 1 ) ):
        if grid.get( n, None ) == val:
            union_find.merge( ( r, c ), n )

def solve():
    total1 = 0
    total2 = 0


    for le_set in union_find.subsets():
        le_set = set(le_set)
        area = len(le_set)
        perimeter = 0
        sides = 0

        for r1,c1 in le_set:
            for r2,c2 in [(r1 + 1, c1), (r1 - 1, c1), (r1, c1 + 1), (r1, c1-1)]:
                perimeter += (r2,c2) not in le_set

            sides += ( r1 - 1, c1 ) not in le_set and ( r1, c1 - 1 ) not in le_set
            sides += ( r1 + 1, c1 ) not in le_set and ( r1, c1 - 1 ) not in le_set
            sides += ( r1 - 1, c1 ) not in le_set and ( r1, c1 + 1 ) not in le_set
            sides += ( r1 + 1, c1 ) not in le_set and ( r1, c1 + 1 ) not in le_set
            sides += (r1 - 1, c1) in le_set and (r1, c1 - 1) in le_set and (r1 - 1, c1 - 1) not in le_set
            sides += (r1 + 1, c1) in le_set and (r1, c1 - 1) in le_set and (r1 + 1, c1 - 1) not in le_set
            sides += (r1 - 1, c1) in le_set and (r1, c1 + 1) in le_set and (r1 - 1, c1 + 1) not in le_set
            sides += (r1 + 1, c1) in le_set and (r1, c1 + 1) in le_set and (r1 + 1, c1 + 1) not in le_set

        total1 += area * perimeter
        total2 += area * sides


    print("Result for part1:", total1)
    print("Result for part2:", total2)
                            


if __name__ == "__main__" :
    solve()




