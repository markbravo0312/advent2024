from functools import cache


f = open("input.txt", "r").read().strip()
nums = [int(x) for x in f.split()]

            
@cache 
def count(stone , steps): 
    if (steps == 0): 
        return 1
    
    if (stone == 0) :
        return count(1, steps - 1)
    
    num_as_string = str(stone)
    if (len(num_as_string) % 2 == 0): 
        half = len(num_as_string) // 2
        l, r = int(num_as_string[:half].lstrip('0') or '0'), int(num_as_string[half:].lstrip('0') or '0')
        return count(l, steps - 1) + count(r, steps - 1)
    
    return count(stone * 2024, steps-1)
    
    
        

def solve(): 
    curr = nums
    res1 = sum(count(x, 25) for x in nums)
    print("Result for part1: ", res1)  
    res2 = sum(count(x, 75) for x in nums)
    print("Result for part2: ", res2)
    
        
        
        
            
    
    
    
    
if __name__ == "__main__":
    solve() 
