import random

def generate_random_state(width, height):
    grid = []

    #this loop selects one of the elements in the list of lists that is defined by the generate_random_state's function arguments
    for y in range(0, height):
        #creates the empty list in which all the elements sit in
        grid.append([])
        #this loop populates each element in the list of lists with the defined amount of random zeroes and ones, specified by the functions arguments
        for i in range(0,width):
            n = random.randint(0,1)
            grid[y].append(n)
    #formats the grid, placing it into ordered rows
    for row in grid:
       print(row)

generate_random_state(10, 10) 
