import math
import pylab as plt
from random import randint

def randwalk(): #returns a list of displacements with each step
    x = 0
    y = 0
    coord = []
    for i in range(0,100):
        a = randint(1,4)
        if a == 1: #up
            y+=1
        elif a == 2: #down
            y-=1
        elif a == 3: #right
            x+=1
        else: #left
            x-=1
        coord.append(math.sqrt((x*x)+(y*y)))
    return coord        

def main():
    num_of_runs = 5000 #Number of runs to be averaged

    #-- Averaging routine --#
    fin = randwalk()

    for n in range(0,num_of_runs-1):
        p = randwalk()
        for i in range(0,100):
            fin[i] += p[i]

    for i in range(0,100):
        fin[i] /=num_of_runs
    #----------------------#

    fin.insert(0,0) #zero steps -> zero displacement

    #-- Plotting routine --#
    plt.plot(fin) 
    plt.ylabel('Net Displacement')
    plt.xlabel('Steps')
    plt.show()
    #----------------------#

if __name__ == '__main__':
    main()
    
