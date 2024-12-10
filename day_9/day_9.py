from collections import deque
FILENAME = "input.txt"


f = open(FILENAME, "r").read() 


def part1() : 
    
    
    files = list(map(int, f[::2]))
    free_blocks = list(map(int, f[1::2]))    
    file_head = 0
    file_tail = len(files) - 1
    blockptr = 0
    total = 0
    i = 0
    res = []
    
    while file_head <= file_tail or blockptr < len(free_blocks):

       
        if file_head <= file_tail:
            curr_file_size = files[file_head]
            if curr_file_size > 0:
                res.extend([file_head] * curr_file_size)
                files[file_head] = 0  
            file_head += 1

        
        if blockptr < len(free_blocks):
            curr_block_size = free_blocks[blockptr]
            while curr_block_size > 0 and file_tail >= file_head:
                last_file_size = files[file_tail]
                if last_file_size > 0:
                    to_fill = min(curr_block_size, last_file_size)
                    res.extend([file_tail] * to_fill)
                    files[file_tail] -= to_fill
                    curr_block_size -= to_fill

                
                if files[file_tail] == 0:
                    file_tail -= 1

           
            blockptr += 1


    for r in range(len(res) ) :
        total += r * res[r]
    
    print("Result for Part1: ", total )
        
    
def part2() : 
    files, free_blocks = [], []
    pointer = 0

    for i, c in enumerate(f):
        if i % 2 == 0:
            files.append(list(range(pointer, pointer + int(c))))
            pointer += int(c)
        else:
            free_blocks.append(list(range(pointer, pointer + int(c))))
            pointer += int(c)

    for y in reversed(range(len(files))):
        for x in range(len(free_blocks)):
            if len(free_blocks[x]) >= len(files[y]) and files[y][0] > free_blocks[x][0]:
                files[y] = free_blocks[x][:len(files[y])]
                free_blocks[x] = free_blocks[x][len(files[y]):]

    print("Result for part2: ", sum(i * j for i, f in enumerate(files) for j in f))



    



     

                 
                
            

    




        
        

        



    





if __name__ == "__main__" : 
    part1() 
    part2() 