import math
import pylab as plt #For plotting

globalMD = 1.61554262658 #Calculated for a square of side 2000

def main():
    L = percentage_list(list_of_MD()) #Generates a list of the percentages
    #-- Plotting routine --#
    plt.plot(L[2:len(L)]) 
    plt.ylabel('Percentage deviation from precise Madelung constant (%)')
    plt.xlabel('Length of side of square')
    plt.show()
    #----------------------#

def dist( x,y,z ): #Calculates the distance of (x,y,z) from (0,0,0)
    return math.sqrt((x*x)+(y*y)+(z*z))

def ML(n): #Calculates the madelung constant for a square lattice of side 2*n
    mdlung = 0
    for i in range(-n,n): #Loops through x values
        for j in range(-n,n): #Loops through y values
            for k in range(-n,n): #Loops through z values
                if i != 0 or j != 0 or k != 0: #Ignores the center point
                    mdlung += pow(-1,1+i+j+k)/dist(i,j,k) #Adds contribution from each point
    return mdlung

def list_of_MD(): #Returns a list of Madelung constants for a range of n 
    L = []
    for n in range(2,50):
        L.append(ML(n/2))
    return L

def percentage_list(L): #Uses list of constants to return a list of percentage deviations
    P = []
    for i in L:
        P.append(100*(globalMD-i)/globalMD)
    return P

if __name__ == "__main__":
    main()
