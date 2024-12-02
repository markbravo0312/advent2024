

FILENAME = "input.txt"


def isSafe(lst) : 
    stricly_inc_or_dec = (lst == sorted(lst)) or (lst == sorted(lst, reverse=True))
            
    acceptable = True
    for i in range(len(lst) - 1) : 
        diff = abs(lst[i] - lst[i + 1])
        if not 1 <= diff <= 3 : 
            acceptable = False 
                    
                
    if acceptable and stricly_inc_or_dec:
        return True
    


def solution():
    safe = 0
    tolerate = 0
    
    with open(FILENAME, 'r') as f: 
        lines = f.read().split('\n')
        for line in lines:
            t = list(map(int, line.split() ))  #cast to int
            
            if isSafe(t):
                safe += 1
                tolerate += 1
            else: 
                tolerable = False
                for temp in [t[:i] + t[i+1:] for i in range(len(t))]:
                    if isSafe(temp):
                        tolerable = True
                if tolerable: 
                    tolerate += 1
                        
                   
    print("Part 1: ", safe)
    print("Part 2: ", tolerate)



    
        
            
        
        
    
                
                
if __name__ == '__main__':
    solution()
     
    