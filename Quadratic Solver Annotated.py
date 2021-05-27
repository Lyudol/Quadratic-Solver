#This script solves quadratic equations by getting the user to input coefficients, and then putting these coefficients through the Quadratic Formula

import math

def userinputs(): #This function prompts the user to input the equation's A, B and C coefficients and stores them as their respective variables
    global A
    global B
    global C
    A = float(input("Input your A coefficient (If your equation doesn't have one, just type 1): "))
    B = float(input("Input your B coefficient: "))
    C = float(input("Input your C coefficient: "))
    numerator()

def numerator():
    global numpos
    global numneg
    numrootone = B*B-4*A*C #This line calculates the simplified values of the coefficients when plugged into the numerator's surd
    if numrootone < 0:                                               
        print("--------------------------------------------------") #This if statement checks whether the numerator surd contains a negative number,
        print("ERROR: Invalid coefficients")                        #which would deem the user's coefficients invalid due to a negative surd being mathematically impossible
        restarter() #Then the function from line 40 is called to allow a new equation to be input
    else:
        numroottwo = math.sqrt(numrootone) #Otherwise, if the surd is positive, the program continues to actually root the number
        numpos = B*-1 + numroottwo #In this line, the positive version of the numerator is calculated
        numneg = B*-1 - numroottwo #In this line, negative version of the numerator is calculated
        denominator()

def denominator():
    global denom
    denom = 2*A #Here, the denominator is calculated via the 2(A) part of the quadratic formula
    solver()

def solver():
    possol = numpos/denom #This line then divides the added numerator with the denominator to produce the first X value and assigns it a variable
    negsol = numneg/denom #This line then divides the subtracted numerator with the denominator to produce the second X value and assigns it a variable
    print("--------------------------------------------------")
    print("X is either", possol,"or", negsol) #Then, the two solution variables are put into a string and output to the user
    restarter()

def restarter(): #This function just asks the user if they want to solve a new equation  
    print("--------------------------------------------------")
    retry = input("Would you like to solve another equation? (Y/N): ")
    if retry == "Y" or retry == "y":
        print("--------------------------------------------------")
        userinputs()
    elif retry == "N" or retry == "n":
        print("--------------------------------------------------")
    else:
        restarter()

userinputs()
