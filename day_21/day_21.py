
from collections import deque
from itertools import product
from functools import partial, cache

f = open("input.txt", "r").read()

codes = [c for c in f.split("\n")]



numpad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [None, '0', 'A']
]

dirpad = [
    [None, '^', 'A'],
    ['<', 'v', '>'],
]



def compute_seqs(keypad):
    position_map = {}
    for row in range(len(keypad)):
        for col in range(len(keypad[row])):
            if keypad[row][col] is not None:
                position_map[keypad[row][col]] = (row, col)

    sequences = {}
    for start_key in position_map:
        for end_key in position_map:
            if start_key == end_key:
                sequences[(start_key, end_key)] = ["A"]
                continue

            possibilities = []
            queue = deque([(position_map[start_key], "")])
            optimal_length = float("inf")

            while queue:
                (curr_row, curr_col), moves = queue.popleft()

                for new_row, new_col, move_symbol in [
                    (curr_row - 1, curr_col, "^"),
                    (curr_row + 1, curr_col, "v"),
                    (curr_row, curr_col - 1, "<"),
                    (curr_row, curr_col + 1, ">")
                ]:
                    if (new_row < 0 or new_col < 0 or 
                        new_row >= len(keypad) or 
                        new_col >= len(keypad[0]) or 
                        keypad[new_row][new_col] is None):
                        continue

                    if keypad[new_row][new_col] == end_key:
                        if optimal_length < len(moves) + 1:
                            break
                        optimal_length = len(moves) + 1
                        possibilities.append(moves + move_symbol + "A")
                    else:
                        queue.append(((new_row, new_col), moves + move_symbol))
                else:
                    continue
                break
            
            sequences[(start_key, end_key)] = possibilities

    return sequences

numseqs = compute_seqs(numpad)
dirseqs = compute_seqs(dirpad)
dirlengths = {key: len(value[0]) for key, value in dirseqs.items()}

def getResult(string, seqs): 
    options = [seqs[(x, y)] for x, y in zip("A" + string, string)]
    return ["".join(x) for x in product(*options)]

@cache
def tabularlength(seq, depth): 
    if depth == 1:
        return sum(dirlengths[(x, y)] for x, y in zip("A" + seq, seq))
    return sum(
        min(tabularlength(subseq, depth - 1) for subseq in dirseqs[(x, y)])
        for x, y in zip("A" + seq, seq)
    )

def solve(d): 
    total = 0
    for code in codes: 
        r1 = getResult(code, numseqs)
        length = min(map(partial(tabularlength, depth=d), r1))
        total += length * int(code[:-1])
    print(total)
    
        
    






        
    
    




if __name__ == "__main__": 
    print("result to part1:")
    solve(2)
    print("result to part2:")
    solve(25) 


    

