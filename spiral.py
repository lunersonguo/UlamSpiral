#!/usr/bin/env python2 

""" Author: Jinjiang Guo """
import math
import matplotlib.pyplot as plt

_max_size_ = 4294967295  # 2**32-1
class Ulam_Spiral:
    """ Ulam Spiral Class functions:
    Generation of an Ulam spiral of  arbitrary size;
    Visualization of the generated  sipral;
    Check any number Primality of given position in Cartesian coordinate system;
    Visualization of a subset of the spiral near the checked position.
    """

    def __init__(self, start = 0, end = 81):

        # Ensure that the spiral starting and ending number is valid
        if not isinstance(start, int):
            raise TypeError(
                'Spiral starting number must be a non-negative integer; but %s entered' % start
            )
        elif start < 0:
            raise ValueError(
                'Spiral starting number must be a non-negative integer; but %s entered' % start
            )
        elif start > _max_size_:
            raise ValueError(
                'Spiral starting number (%s) exceeds limits (%s)' % (start, _max_size_)
            )


        if not isinstance(end, int):
            raise TypeError(
                'Spiral size must be a positive integer; but %s entered' % end
            )
        elif end < 0:
            raise ValueError(
                'Spiral size must be a positive integer; %s entered' % end
            )
        elif end < start:
            raise ValueError(
                'Ending number (%s) is smaller than starting number (%s)' % (end, start)
            )
        elif end > _max_size_:
            raise ValueError(
                'Ending number (%s) exceeds limits (%s)' % (end, _max_size_)
            )
    
    #initializiton of paras
        self.start = start
        self.end = end
        
        self.x = 0
        self.y = 0
	# Operation: 0 = right; 1 = up; 2 = left; 3 = down;
        self.operation = -1 
    # repetition of each operation
        self.dupli = 1
    #Accumalation of whole repetitions of operations
        self.sumation = 2*self.dupli

    # Return current coordinates
    def _coords_(self):
        return (self.x, self.y)
    
    #function for primality test : Sieve of Eratosthenes
    def _is_prime_(self, n): 
        self.n = n
        if self.n ==2: 
            return True
        # if n can be exactly divided by 2, it is not prime, except 2 
        if self.n % 2 == 0 or self.n < 2:  
            return False
         # try all the odd number betwee 3 and suqare root n, if n can be exactly divided by the odd number, n is not prime
        for i in range(3, int(math.sqrt(self.n)) + 1, 2):
            if self.n % i == 0:
                return False
        return True


    # determine the position of next number
    def _next_step_(self, i = 0):
        self.i = i
        
        if self.i == self.sumation: #this comparison is used for determining repetition of each operation 
            self.dupli += 1
            self.sumation += 2*self.dupli #after each 2 operations, the repetition of each operation increacses

        self.change_index = self.i % self.dupli # this index used for checking whether need to change operation
        
        if self.change_index == 0:  #time to change
            self.operation += 1
        
        if self.operation%4 == 0: self.x += 1
        elif self.operation%4 == 1: self.y += 1
        elif self.operation %4== 2: self.x -= 1
        elif self.operation%4 == 3: self.y -= 1
   
   # generate ulam spiral O(N)
    def spiral_gen(self):

        span = self.end - self.start + 1

        self.spiral_dict ={} # dictionary: Save Numbers as keys; x,y coords and prime check result as values
       
        for i in range(span):
            self.x, self.y = self._coords_()
            
            self.prime = self._is_prime_(self.start+i)

            self.spiral_dict[str(self.start+i)]={'x':self.x, 'y':self.y, 'prime': self.prime} #save to  the nested dictionary

 
            self._next_step_(i)

        return self.spiral_dict
   
    ## generate a subset of the spiral near the checked position
    def sub_spiral(self, x, y, win_size = 5):
        
        if not isinstance(x+y, int):
            raise TypeError(
                'Coordinates of checked position must be integers, but (%s, %s) entered' %(x, y)
            )

        if not isinstance(win_size, int):
            raise TypeError(
                'Sub window size must be an odd integer, but %s entered' % win_size
            )
        elif win_size <= 0 or win_size%2 == 0:
            raise ValueError(
                'Sub window size must be an odd integer; but %s entered' % win_size
            )
        elif win_size > 20:
            raise ValueError(
                'Sub window size is NOT recommended bigger than 20, but %s entered' % win_size
            )
        
        self.sub_spiral ={}
        self.sub_win_size = win_size
        self.half_win = int(math.floor(self.sub_win_size/2))
        self.given_x = x
        self.given_y = y

        for m in range(-self.half_win, self.half_win+1):
            for n in range(-self.half_win, self.half_win+1):
                
                self.check_number, self.check_prime = self.check_any_position(self.given_x+m, self.given_y+n)
                self.sub_spiral[str(self.check_number)] = {'sub_x':m, 'sub_y': n, 'prime': self.check_prime}
        
        return self.sub_spiral 

    ## function to check a given position in generated spiral. O(N)
    def check_given_position(self, x, y, **kw):
        
        if not isinstance(x+y, int):
            raise TypeError(
                'Coordinates of checked position must be integers, but (%s, %s) entered' %(x, y)
            )
        
        self.check_x = x
        self.check_y = y
        inside = False

        for k in kw:
            if kw[k]['x']== self.check_x and kw[k]['y']== self.check_y:
                self.inside = True
                return (k, kw[k]['prime'])
        if inside == False:
            print 'Number is Not in the spiral'
            return (-1, -1)
    
    ## function to check arbitrary given position. O(1)
    def check_any_position(self, x, y): 
        if not isinstance(x+y, int):
            raise TypeError(
                'Coordinates of checked position must be integers, but (%s, %s) entered' %(x, y)
            )

        self.x = x
        self.y = y
        
        # para: n in documentation
        self.layer = 0 
        # pars: b in documentation
        self.weights = -4 
        # para: c in documentation
        self.constant = 0 
        # para: sigma in documentation
        self.sign = 0 
        

        if abs(self.x) > abs(self.y):
            self.layer = abs(self.x)
            self.constant = abs(self.y)
        elif  abs(self.x) <= abs(self.y):
            self.layer = abs(self.y)
            self.constant = abs(self.x)

        # calculate angle of a given position in radians[0, 2*pi)
        self.angle = math.atan2(y,x) 
        if self.angle < 0: self.angle = 2*math.pi + self.angle 


        if self.angle > math.pi/4 and self.angle <= math.pi*3/4: 
            self.weights = -1
            if self.angle <= math.pi/2: self.sign = -1
            else: self.sign = 1
        elif self.angle > math.pi*3/4 and self.angle <= math.pi*5/4: 
            self.weights = 1
            if self.angle <= math.pi: self.sign = -1
            else: self.sign = 1
        elif self.angle > math.pi*5/4 and self.angle <= math.pi*7/4: 
            self.weights = 3
            if self.angle <= math.pi*3/2: self.sign = -1
            else: self.sign = 1
        else: 
            self.weights = -3
            if self.angle > math.pi*7/4 : self.sign = -1
            else: self.sign = 1
        
        #computation of the Number for a given position
        self.final_num = 4 * self.layer**2 + self.weights * self.layer  + self.sign*self.constant + self.start
        self.prime = self._is_prime_(self.final_num)

        return (self.final_num, self.prime)

    ## Function to visualization of the spiral and subset of the spiral
    def visualize_spiral(self, x, y, win_size = 5, **kw1):
        
        if not isinstance(x+y, int):
            raise TypeError(
                'Coordinates of checked position must be integers, but (%s, %s) entered' %(x, y)
            )
        
        self.checked_x = x
        self.checked_y = y
        self.spiral_dict = kw1
        self.sub_win_size = win_size
        self.sub_spiral_dict = self.sub_spiral(self.checked_x, self.checked_y, self.sub_win_size)

        self.any_number, self.prime_result = self.check_any_position(self.checked_x, self.checked_y)

        fig, ax = plt.subplots(figsize=(10, 10))
        side = 20
        for j in self.sub_spiral_dict:
            
            if self.sub_spiral_dict[j]['prime']:
                color ='red'
            else:
                color = 'navy'

            rect = plt.Rectangle(((self.sub_spiral_dict[j]['sub_x']-0.5)*2, (self.sub_spiral_dict[j]['sub_y']-0.5)*2), width=2, height=2, angle=0, ec='black', color=color)
            ax.add_artist(rect)
            ax.text(self.sub_spiral_dict[j]['sub_x']*2, self.sub_spiral_dict[j]['sub_y']*2, s='{}'.format(j), ha='center', va='center', color='white', fontsize=13)
        
        fig.suptitle('Subset of Ulam Spiral: checked position (%s, %s), window size: %s' %(self.checked_x, self.checked_y, self.sub_win_size), fontsize=16)
        plt.xlim(-side/2, side/2+1)
        plt.ylim(-side/2, side/2+1)
        plt.axis('off')
        
        if self.any_number > self.end:
            print 'The checked position is OUT of generated Ulam Spiral. Subset of spiral is drawn near checked position. '

        elif self.any_number <= self.end: # draw the whole spiral when checedk number is less than spiral size
            
            fig, ax = plt.subplots(figsize=(10, 10))
            side = 10
            for k in self.spiral_dict:

                if (self.spiral_dict[k]['prime']):
                    color = 'red'
                else:
                    color = 'gray'
                rect = plt.Rectangle(((self.spiral_dict[k]['x']-0.5)*1, (self.spiral_dict[k]['y']-0.5)*1), width=1, height=1, angle=0, ec='black', color=color)
                ax.add_artist(rect)
                ax.text(self.spiral_dict[k]['x']*1, self.spiral_dict[k]['y']*1, s='{}'.format(k), ha='center', va='center', color='white', fontsize=13)
            
            fig.suptitle('Ulam Spiral size of %s' %(self.end), fontsize=16)
            plt.xlim(-side/2, side/2+1)
            plt.ylim(-side/2, side/2+1)
            # plt.axis('off')

        plt.show()

