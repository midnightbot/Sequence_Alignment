*********************************************************************************************************************************
How to run
Running from command prompt
	a. "python3 time_efficient.py input.txt" for running basic version (Time Efficient)
	b. "python3 space_efficient.py input.txt" for running efficient version (Space Efficient)

Running from Shell Script
	a. time_efficient.sh for running basic version
	b. space_efficient.sh for running efficient version

Note : Commands may change depending on Python version and operating system
*********************************************************************************************************************************
Import requirements
1. time
2. timeit
3. os
4. psutil
5. sys
**********************************************************************************************************************************
Python Version : 3+
**********************************************************************************************************************************
Output file format
Line 1 - > word1[0:50]   word1[len(word1)-50:len(word1)]
Line 2 - > word2[0:50]   word2[len(word2)-50:len(word2)]
Line 3 - > Alignment Cost
Line 4 - > Time Taken in seconds
Line 5 - > Memory utilization in KB
***********************************************************************************************************************************
Notation
Basic version - > Time Efficient
Efficient version - > Memory Efficient
***********************************************************************************************************************************
Note : please make sure input.txt is in the same folder as that of the python files
**********************************************************************************************************************************