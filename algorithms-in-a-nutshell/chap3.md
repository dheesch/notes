# Algorithm Building Blocks

## Algorithm Template Format 
- name - preferably a descriptive one 
- input/output - the expected format of input data to the algorithm and the resulting values computed 
- context - description of a problem that illustrates when an algorithm is useful and when it will perform at its best 
- solution - the algorithm description using real working code w/ documentation 
- analysis - synopsis of the analysis of the algorithm, including performance data 
- variations 

## Pseudocode Template Format 
- normal pseudocode 

## Floating-Point Computation
- computers perform basic computations on values stored in registers by a CPU
- cpus support basic operations - add, sub, mult, divide over integer values stored in these registers 
  - Floating-point units - FPUS can efficiently process floating-point computations according to IEEE binary floating-point arithmetic
- math on ints have traditionally been the most efficient cpu computations
- floating point numbers will always be a little slower than integers
- any floating-point computation might introduce rounding errors 
- be weary of comparing floats 

## Dynamic Programming 
- variation on divide and conquer 
- subdivide problem into a number of simpler subproblems that are solved in a specific order 
- 