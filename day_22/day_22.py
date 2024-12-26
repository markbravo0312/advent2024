from functools import cache
from collections import defaultdict

f = open("input.txt", "r").read().split("\n")

nums = list(map(int, f))




@cache
def transform(sec): 
    res = sec * 64
    sec = sec ^ res
    sec = sec % 16777216  

    temp = sec // 32
    sec = sec ^ temp
    sec = sec % 16777216  

    
    temp = sec * 2048
    sec = sec ^ temp
    sec = sec % 16777216  

    return sec



def solve() :
    total = 0
    for x in nums: 
        temp = x
        for _ in range(2000):
            temp = transform(temp)
        total += temp

    print("Result for part1: ", total)

    
    seq_to_total = {}
    for x in nums: 
        temp = x
        buyer = [temp % 10]
        for _ in range(2000): 
            temp = transform(temp)
            buyer.append(temp % 10 )

        visited = set() 
        

        for i in range((len(buyer) - 4)) : 
            x1, x2, x3, x4, x5 = buyer[i:i+5]

            seq =  (x2-x1, x3-x2, x4-x3, x5-x4) 
            if seq in visited : continue
            visited.add(seq)
            

            if seq in seq_to_total: 
                seq_to_total[seq] += x5
            else: 
                seq_to_total[seq] = x5

    print("Result for part2: ", max(seq_to_total.values()) ) 




if __name__ == "__main__":
    solve() 