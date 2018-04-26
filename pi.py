import random

def estimatePI():
    n = int(input("Number of Random Points: "))
    
    circle_points = 0
    square_points = 0
    
    for i in range(n):
        
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        d = x*x + y*y
        
        if d <= 1:
            circle_points += 1
        square_points += 1

    pi = 4.0 * circle_points * 1.0 / square_points * 1.0
    return pi

        