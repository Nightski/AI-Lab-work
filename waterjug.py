def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

def solver(a,b,target):
    gcd_val = gcd(a,b)
    if target%gcd_val != 0:
        print("Solution doesn't exist")
        return
    x,y = 0,0
    steps = 0
    while x!= target and y!=target:
        if x==0:
            x = a
            print("Fill jug 1")
            steps+=1
        elif y == b:
            y = 0
            print("Empty jug 2")
            steps+= 1
        else:
            pour = min(x, b-y)
            x-=pour
            y+=pour
            print(f"Pour {pour}L from jug 1 to jug 2")
            steps += 1
    print(f"Solution found in {steps} steps")

a = 3
b = 5
target = 4
solver(a,b,target)