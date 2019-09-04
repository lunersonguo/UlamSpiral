# Ulam Spiral
Ulam spiral is constructed by placing sequential positive integers in a counterclockwise square spiral. In Cartesian coordinate system, an Ulam Spiral can be constructed and shown in Figure 1 below:
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

There are many methods to check whether a number is a prime or not, I referred to Sieve of Eratosthenes, and implemented it as my primality test function in my codes. The method is described in Wikipedia link below:
[link to Wiki](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
## Data Structure
For data structure, I used Nested Dictionary in Python, a collection of dictionaries into a single dictionary, and can be described as follows:
```python
nested_dict = {‘keyA’: {‘nested_keyA1’: ‘valueA1’, ‘nested_keyA2’: ‘valueA2’ }
‘keyB’: {‘nested_keyB1’: ‘valueB1’, ‘nested_keyB2’: ‘valueB2’ }}
```
The nested dictionary is very convenient for saving our data, since for each number in Ulam Spiral, its information like number position (x, y) and primality test result (True or False) should be recorded. 
Take a ‘number’ as a ‘Key’ and its ‘x coordinate’, ‘y coordinate’, ‘primality test result’ as ‘Nested_Keys’, and all the data can be saved appropriately during spiral construction.
