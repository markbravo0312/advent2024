import re
f = open("input.txt", "r" ).read()




registerA, registerB, registerC, *instructions = map(int, re.findall(r"\d+", f)) 



def solve(registerA , registerB, registerC, i=0, outputbuffer=[]):
    while i in range(len(instructions)):
        C = {0:0,1:1,2:2,3:3,4:registerA,5:registerB,6:registerC}

        match instructions[i:i+2]:
            case 0, op: registerA = registerA >> C[op]
            case 1, op: registerB = registerB ^ op
            case 2, op: registerB = 7 & C[op]
            case 3, op: i = op-2 if registerA else i
            case 4, op: registerB = registerB ^ registerC
            case 5, op: outputbuffer = outputbuffer + [C[op] & 7]
            case 6, op: registerB = registerA >> C[op]
            case 7, op: registerC = registerA >> C[op]
        i += 2
    return outputbuffer

def solve2(registerA, n) : 
    if solve(registerA, registerB, registerC) == instructions : print(registerA)
    if solve(registerA, registerB, registerC) == instructions[-n:] or not n:
        for x in range(8): solve2(registerA*8+x, n+1)







if __name__ == "__main__": 
    print("Result to part1: ")
    print(*solve(registerA,registerB,registerC), sep=',')
    print("Result to part2: ")
    solve2(0,0)


