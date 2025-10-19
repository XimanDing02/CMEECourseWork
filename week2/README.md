# Week 2 – Biological Computing in Python
In this week, we fucusing on Python progeamming skill. The overall learning process is from simple to complex, so it is quite comfortable for us to learn. Topics Contains such as data structure, control flow, loops, modular programming and so on. 

## Assessment 2
### Loops and List Comprehensions
1. lc1.py 

This task is to practice using loops to generate lists and process data iteratively. Understanding the uses of for and while loop to produce or transforming lists. 

foo_5(x) and foo_6(x) can not handle the siuation when x = 0, so I need to modify functions to fix this situation. I add the x == 0 in side the loop.

2. lc2.py 

This task is little bit more complicated than the code inside lc1.py. Let us to handle 2D lists, filter or transform multi-dimensional data.

3. dictionary.py 

This task showed me the Python dictionary structure. Inside this tasks, I created, updated, and deleted dictionary entries, iterating through keys and values, and demonstrating dictionary comprehension.

4. tuple.py

This task taught me about the structure about tuples as immutable ordered data collections and their practical applications in Python.

### Writing a program with control flows
I copy the lc1.py file to control_flow_lc1.py to practice structuring Python programs using control flows. I learned how to take user-provided arguments instead of hardcoded valuesuse, and combine with the conditional statements (like if, elif, else), loops, and return values to control program outputs. 

### Align DAN sequences
In this task, I modified the original align_seqs.py script which download from MQB/code to automatically read two DNA sequences from an external input file ../data/align_seqs.csv and write the best alignment and its corresponding score to an output file ../results/best_alignment.txt.

The program aims to read two DNA sequences, determines which one is longer, and slides the shorter sequence along the longer one to find the alignment with the highest number of matching bases. 

### Missing oaks problem
In the oaks_debugme.py task, the goal was to identify oak species (genus Quercus) from a CSV dataset TestOaksData.csv. In the first beginning when I run this .py document, the script had a bug where no oaks were detected because the function is_an_oak misspelled ``quercus'' as ``quercs''. I fixed this bug, added doctests to verify the function’s correctness, and then improved the function to handle common typos (such as ``Quercuss'') and variations in case or spacing. 

## What I found challenge
Since I learned Python during my undergraduate studies, the first half of the week was very relaxing and enjoyable, and I enjoyed consolidating my knowledge. The second half of the week was filled with new topics. What I feel challenging is was writing effective doctests for the is_an_oak function. It was tricky to think about all possible cases, including typos like ``Quercuss'' or extra spaces, but it let me learned how testing can reveal hidden bugs that are not obvious during manual debugging. 
