#!/usr/bin/env python2

from spiral import Ulam_Spiral
import time

## start_number: Ulam spiral starting number; spiral_size: Ulam spiral ending number
start_number = 1
spiral_size = 81

uspiral = Ulam_Spiral(start_number, spiral_size)

## nested dictionary: Save Numbers as keys; x,y coords and primality test results as nested keys
spiral_dict = uspiral.spiral_gen()  # Solution (1)

##check_x: x coordinates of checked position; check_y: y coordinates of checked position; 
check_x = 2
check_y = -3

##sub_win_size:  Neighborhood size of checked poisition 
sub_win_size = 5


# ##Check  Primality of a given position after spiral construction, search time: O(N) ##
# time_start =time.time()
# number, is_prime = uspiral.check_given_position(check_x, check_y, **spiral_dict) # Solution (3)
# time_end =time.time()
# print 'Number: %s, Prime: %s, Search time %s s' %(number, is_prime, (time_end-time_start))

##Check Primality of a given position using projection formula, search time: O(1) ##
time_start =time.time()
arbitrary_number, prime_result = uspiral.check_any_position(check_x, check_y) # Bonus Solution
time_end =time.time()
print 'Number: %s, Primality test result: %s , Computation time %s s' %(arbitrary_number, prime_result, (time_end-time_start))

## Visualization of the spiral and subset of the spiral ##
uspiral.visualize_spiral(check_x, check_y, sub_win_size, **spiral_dict) # Solution (2) and Bonus Solution
