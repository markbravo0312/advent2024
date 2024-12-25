from functools import cache

f = open("input.txt", "r").read().split("\n")

nums = map(int, f)



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



if __name__ == "__main__":
    solve() 