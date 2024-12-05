
FILENAME = "input.txt"


predecessors = {}
outdegree = {}



def topo_sort(nums) :
    
   
    
    for x in range(0, len(nums)): 
        for y in range(x+1, len(nums)) :
            if nums[x] in predecessors and nums[y] in predecessors[nums[x]]:
                nums[x], nums[y] = nums[y], nums[x]
    
    
    return nums[len(nums)//2]
    
    

def solve() : 
    lines = open(FILENAME).read().split('\n')
    flag = False
    
    
    
    total = 0
    total2 = 0
    
    for line in lines:
        if line == "":
            flag = True
            continue
        
        if not flag:
            num1, num2 = map(int, line.split('|'))        #num1 has to come before num2 so
            if num2 not in predecessors:
                predecessors[num2] = [num1]
            else:
                predecessors[num2].append(num1)
                
        
        if flag:
            nums = list(map(int, line.split(',')))
            curr = []
            valid = True
            newlist = []
            for x in nums: 
                for y in range(len(curr)):
                    if curr[y] in predecessors:
                        if x in predecessors[curr[y]]:
                            valid = False
                            break
                
                if not valid:
                    total2 += topo_sort(nums)
                    break
                       
                curr.append(x)
            
            if valid :
                total += nums[len(nums)//2]
                
    print("result part 1 : ", total)
    print("result part 2 : ", total2)                
                            
                

                
            
            
    
    

if __name__ == "__main__" :
    solve()