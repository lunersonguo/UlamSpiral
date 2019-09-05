# Ulam Spiral
Ulam spiral is constructed by placing sequential positive integers in a counterclockwise square spiral. In Cartesian coordinate system, an Ulam Spiral can be constructed and shown in Figure 1 :
In the grid, each number locates in corresponding position, such like 
1: (0,0),  2: (1,0),  3: (1,1),  4: (0,1),  5: (-1, 1), etc.

## Spiral Constrcutin

To construct an Ulam Spiral of arbitrary size N, and accomplish it in O(N) times. It is necessary to find some patterns:
During spiral construction, at each iteration, the next number’s position should be calculated based on current number status. There are 4 next-step operations for next number’s position: right (x coordinate value +1), up (y coordinate value +1), left (x coordinate value -1), down ( y coordinate -1). Let’s label these 4 operations as 0, 1, 2 and 3 respectively. 
From the origin (0,0), the Ulam Spiral can be constructed following the operation sequence (0, 1, 2, 2, 3, 3, 0, 0, 0, 1, 1, 1, …). The sequence obeys the patterns below:
1. The operations change from 0 to 3 sequentially and circularly;
2. The repetitions of each operation increase after every two operations.
The patterns of operations can be specifically observed in Figure 2. And the computation time complexity is O(N).

## Primality test

There are many methods to check whether a number is a prime or not, I referred to Sieve of Eratosthenes, and implemented it as my primality test function in my codes. The method is described in Wikipedia link :
[link to Wiki](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
## Data Structure
For data structure, I used Nested Dictionary in Python, a collection of dictionaries into a single dictionary, and can be described as follows:
```python
nested_dict = {‘keyA’: {‘nested_keyA1’: ‘valueA1’, ‘nested_keyA2’: ‘valueA2’ }
‘keyB’: {‘nested_keyB1’: ‘valueB1’, ‘nested_keyB2’: ‘valueB2’ }}
```
The nested dictionary is very convenient for saving our data, since for each number in Ulam Spiral, its information like number position (x, y) and primality test result (True or False) should be recorded. 
Take a ‘number’ as a ‘Key’ and its ‘x coordinate’, ‘y coordinate’, ‘primality test result’ as ‘Nested_Keys’, and all the data can be saved appropriately during spiral construction.

## Whole Spiral visualization
For visualization, I used Matplotlib as my 2D plotting library for drawing Ulam Spiral with size of N =81. Specifically, each number is placed in the center of small square. When the number is prime, its background square will be in red color, otherwise the square will be in gray. The result is shown in Figure 3 :

## Data Searching
Once all the data are saved in a nested dictionary. It is very efficient for data searching, retrieval and visualization. Each number in N (spiral size) is visited once, and target data is obtained by checking the values associated with its Nested_Keys. Therefore, the time complexity is O(N).
In this project, for a given grid coordinate (x, y) in a spiral size of N. To determine whether that position contains a prime number or not, traverse the nested dictionary from beginning key (number ‘1’ in this case) , at each step for each key (number n ), compare its recorded coordinates with checked coordinates (x, y), if the coordinates equal then return its recorded ‘primality test result’, if the coordinates do not equal then continue search till the end key ( number ‘N’ in this case). Thus, the search function time complexity is O(N).

## Improvement
As noticed, the checking method in above works after the construction of an Ulam Spiral. However, when the spiral size is extremely large (e.g., N =100 Trillion), it will be very consuming to firstly construct the spiral and then check the number of a given position. 
To check ANY given position in a spiral of arbitrarily large size efficiently, it is critical to find the patterns of number distributions over Ulam Spiral, and establish the projection (function) between each position in the grid and its corresponding number of the spiral. Once the projection is established, any given position can be checked directly without constructing the spiral, and hence the time complexity is O(1).
Thanks to precedent study on Ulam Spiral by pioneers, I got much useful information for establishing such projection. The information and patterns I got through the links and references [link to reference 1](http://primorial-sieve.com/_Ulam%20spiral%20unraveled.pdf)[link to reference 2](https://web.archive.org/web/20141202041502/https://danpearcymaths.wordpress.com/2012/09/30/infinity-programming-in-geogebra-and-failing-miserably/)
The patterns can be described in Figure 4 below:

Based on the information in Figure 4, I generalized the projection formula as follows: 
Starting with number s: (0, 0) ( s=1 in this project), any number in a spiral corresponds to polynomials of the form, as follows: 

For a given position (x, y), all the parameters can be determined by:

Substitute equations (2), (3), (4) and (5) into formula (1), the corresponding number of the given position (x, y) can be computed. And naturally whether it is a prime or not can be also determined. 
Table 1 shows some time comparison results between the method in question (3) and the projection function over different checked positions and spiral sizes. The performance is measured by PC with single processing unit: 2.7 GHz Intel Core i7.
