import math

def userinputs():
    global A
    global B
    global C
    A = int(input("Input your A coefficient (If your equation doesn't have one, just type 1): "))
    B = int(input("Input your B coefficient: "))
    C = int(input("Input your C coefficient: "))
    numerator()

def numerator():
    global numpos
    global numneg
    numrootone = B*B-4*A*C 
    if numrootone < 0:                                               
        print("--------------------------------------------------") 
        print("ERROR: Invalid coefficients")                        
        restarter() 
    else:
        numroottwo = math.sqrt(numrootone) 
        numpos = B*-1 + numroottwo
        numneg = B*-1 - numroottwo
        denominator()

def denominator():
    global denom
    denom = 2*A
    solver()

def solver():
    global restarter
    def restarter(): 
        print("--------------------------------------------------")
        retry = input("Would you like to solve another equation? (Y/N) ")
        if retry == "Y" or retry == "y":
            print("--------------------------------------------------")
            userinputs()
        elif retry == "N" or retry == "n":
            print("--------------------------------------------------")
        else:
            restarter()
    possol = numpos/denom
    negsol = numneg/denom
    print("--------------------------------------------------")
    print("X is either", possol,"or", negsol)
    restarter()

userinputs()