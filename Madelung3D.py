import math

def main():
    x = raw_input('Enter the side length of the cube: ')
    print('The Madelung constant for your FCC lattice is: ' + str(ML(int(x)/2)))

def dist( x,y,z ): #Calculates the distance of (x,y,z) from (0,0,0)
    return math.sqrt((x*x)+(y*y)+(z*z))

def ML(n): #Calculates the madelung constant for a FCC lattice of side 2*n
    mdlung = 0
    for i in range(-n,n): #Loops through x values
        for j in range(-n,n): #Loops through y values
            for k in range(-n,n): #Loops through z values
                if i != 0 or j != 0 or k != 0: #Ignores the center point
                    mdlung += pow(-1,1+i+j+k)/dist(i,j,k) #Adds contribution from each point
    return mdlung

if __name__ == "__main__":
    main()
