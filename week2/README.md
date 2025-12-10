# Week 2 – Biological Computing in Python

## Table of Contents

- [**Week 2 – Biological Computing in Python**](#week-2--biological-computing-in-python)
  - [Table of Contents](#table-of-contents)
  - [**Brief Description**](#brief-description)
  - [**Languages**](#languages)
  - [**Installation**](#installation)
  - [**Dependencies**](#dependencies)
  - [**Project Structure**](#project-structure)
  - [**Scripts List**](#scripts-list)
  - [**Basic Script Usage**](#basic-script-usage)
  - [**What I found challenge**](#what-i-found-challenge)
  - [**Author and Contact**](#author-and-contact)

## Project Structure
This whole week2 structure is:
```plaintext
./week2/
│
├── code/
│   ├── MyExampleScript.py
│   ├── align_seqs.py
│   ├── basic_csv.py
│   ├── basic_io1.py
│   ├── basic_io2.py
│   ├── basic_io3.py
│   ├── boilerplate.py
│   ├── cfexercises1.py
│   ├── cfexercises2.py
│   ├── control_flow.py
│   ├── debugme.py
│   ├── dictionary.py
│   ├── imeitme.py
│   ├── lc1.py
│   ├── lc2.py
│   ├── loops.py
│   ├── oaks.py
│   ├── oaks_debugme.py
│   ├── scope.py
│   ├── sysargv.py
│   ├── test_control_flow.py
│   ├── tuple.py
│   └── using_name.py
│
├── data/
│   ├── JustOaksData.csv
│   ├── TestOaksData.csv
│   ├── align_seqs.csv
│   ├── bodymass.csv
│   └── testcsv.csv
│
├── results/
│   └── (currently empty — will store output from scripts)
│
└── readme.md
```

## Brief Description
In this week, we fucusing on fundamental Python skills. The overall learning process is from simple to complex, so it is quite comfortable for us to learn. Topics 
including:

1. Basic Python syntax and variables
2. Data structures (lists, tuples, sets, dictionaries)
3. Control flow (loops and conditionals)
3. Functions and script execution
4. File input/output
5. List comprehensions and basic workflow automation
6. These works are based on the Notebook and Data from https://github.com/mhasoba/TheMulQuaBio.git.

## Languages
```
Python
```

## **Installation**
```
Ensure that you are using a UNIX-based environment.

git clone https://github.com/XimanDing02/CMEECourseWork.git
```

## **Dependencies** 
Most of the scripts in Week 2 only require Python 3 and the standard library, and can be run directly in the terminal.

Installation: `sudo apt install python3` (Run in the terminal)

## Scripts List
| Script Name |Description | Arguments |
| ------ | ------ | ------ |
| MyExampleScript.py | A simple example script demonstrating basic Python syntax | None |
| basic_csv.py | Demonstrates how to read and write CSV files in Python | None |
| basic_io1.py | Basic file input example | 1 -> input text file |
| basic_io2.py | Writing output to a file | None |
| basic_io3.py | Reading and processing numerical data from a file | None |
| boilerplate.py | Standard Python script template | None |
| cfexercises1.py | Practice of basic control flow (if / for) | None |
| cfexercises2.py | More advanced control flow exercises | None |
| control_flow.py | Demonstration of Python control flow statements | None |
| debugme.py | Debugging practice script | None |
| dictionary.py | Demonstrates the usage of Python dictionaries | None |
| imeitme.py | Measures execution time of code blocks | None |
| lc1.py | List comprehension practice 1 | None |
| lc2.py | List comprehension practice 2 | None |
| loops.py | Demonstrates for-loops and while-loops | None |
| scope.py | Demonstrates variable scope in Python | None |
| sysargv.py | Demonstrates command-line arguments using sys.argv | Multiple command-line inputs |
| test_control_flow.py | Unit testing for control flow exercises | None |
| tuple.py | Demonstrates tuple usage in Python | None |
| using_name.py | Demonstrates the use of `__name__ == "__main__"` | None |
| align_seqs.py | Align two DNA sequences and calculate alignment score | None |
| oaks.py | Classify oak species based on leaf trait dataset | 1 -> oak dataset CSV file |
| oaks_debugme.py | Debugging version of oak species classification script | 1 -> oak dataset CSV file |

# Basic Script Usage
| Script Name | Basic Usage in terminal |
| ------ | ------ |
| MyExampleScript.py | python3 MyExampleScript.py |
| align_seqs.py | python3 align_seqs.py |
| basic_csv.py | python3 basic_csv.py |
| basic_io1.py | python3 basic_io1.py input.txt |
| basic_io2.py | python3 basic_io2.py |
| basic_io3.py | python3 basic_io3.py |
| boilerplate.py | python3 boilerplate.py |
| cfexercises1.py | python3 cfexercises1.py |
| cfexercises2.py | python3 cfexercises2.py |
| control_flow.py | python3 control_flow.py |
| debugme.py | python3 debugme.py |
| dictionary.py | python3 dictionary.py |
| imeitme.py | python3 imeitme.py |
| lc1.py | python3 lc1.py |
| lc2.py | python3 lc2.py |
| loops.py | python3 loops.py |
| oaks.py | python3 oaks.py ../data/JustOaksData.csv |
| oaks_debugme.py | python3 oaks_debugme.py ../data/JustOaksData.csv |
| scope.py | python3 scope.py |
| sysargv.py | python3 sysargv.py 1 2 3 |
| test_control_flow.py | python3 test_control_flow.py |
| tuple.py | python3 tuple.py |
| using_name.py | python3 using_name.py |

## What I found challenge
Since I learned Python during my undergraduate studies, the first half of the week was very relaxing and enjoyable, and I enjoyed consolidating my knowledge. The second half of the week was filled with new topics. What I feel challenging is was writing effective doctests for the is_an_oak function. It was tricky to think about all possible cases, including typos like ``Quercuss'' or extra spaces, but it let me learned how testing can reveal hidden bugs that are not obvious during manual debugging. 

## Author and Contact

Name: Ximan Ding

Email: x.ding25@imperial.ac.uk

Institution: Imperial College London