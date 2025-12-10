# Biological Computing in R

This week talked about the R. This section talked about the introduction of **vectorization**, and **apply family of functions** in R.

Also, we learned how to improve computational method between loops and vectorized appproaches, and practice debugging using R.

## Table of Contents
- [Biological Computing in R](#biological-computing-in-r)
  - [Table of Contents](#table-of-contents)
  - [Project Structure](#project-structure)
  - [Brief Description](#brief-description)
  - [Languages](#languages)
  - [Installation](#installation)
  - [Dependencies](#dependencies)
  - [Scripts List](#scripts-list)
  - [Basic Script Usage](#basic-script-usage)
  - [Expected Output](#expected-output)
  - [What I found challenge](#what-i-found-challenge)
  - [Author and Contact](#author-and-contact)

## Project Structure
This week3 structure is:

```plaintext

./week3/
│
├── code/
│   ├── Florida.R
│   ├── R_conditionals.R
│   ├── Ricker.R
│   ├── TreeHeight.R
│   ├── Vectorize1.R
│   ├── Vectorize2.R
│   ├── apply1.R
│   ├── apply2.R
│   ├── basic_io.R
│   ├── boilerplate.R
│   ├── break.R
│   ├── browse.R
│   ├── control_flow.R
│   ├── next.R
│   ├── preallocate.R
│   └── sample.R
│
├── data/
│   ├── KeyWestAnnualMeanTemperature.RData
│   └── trees.csv
│
├── results/
│   └── (currently empty — ignored by .gitignore)
│
└── readme.md
```

## Brief Description
In this week, we focus on intermediate R programming skills for biological computing. The main learning contents include:

1. Basic R syntax and script structure
2. Conditional statements in R (if, else, ifelse)
3. Control flow in R (for loops, while loops, break, next)
4. Vectorization in R and performance comparison
5. Apply-family functions for efficient data processing
6. Preallocation for improving computational efficienc
7. Basic file input/output in R
8. Debugging and code inspection using
9. Sampling and random number generation
10. These works are based on the Notebook and Data from https://github.com/mhasoba/TheMulQuaBio.git.

## Languages
```
R
```

## **Installation**
```
Ensure that you are using a UNIX-based environment.

git clone https://github.com/XimanDing02/CMEECourseWork.git
```

## **Dependencies** 
Most of the scripts only require base R and can be run directly in the terminal using Rscript.

Installation: `sudo apt install r-base` (Run in the terminal)

## Scripts List
| Script Name        | Description                                                         | Arguments |
| ------------------ | ------------------------------------------------------------------- | --------- |
| Florida.R          | Analyse annual mean temperature in Florida over time               | None      |
| R_conditionals.R   | Demonstrate conditional statements (if / else / ifelse) in R       | None      |
| Ricker.R           | Implement and explore the Ricker population dynamics model         | None      |
| TreeHeight.R       | Calculate tree heights from distance and angle using trigonometry  | None      |
| Vectorize1.R       | Compare loop-based and vectorised implementations (part 1)         | None      |
| Vectorize2.R       | Further illustration of R vectorisation (part 2)                   | None      |
| apply1.R           | Introduce apply-family functions for matrices and data frames      | None      |
| apply2.R           | More advanced apply-family usage on lists and complex data         | None      |
| basic_io.R         | Basic file input/output operations in R                            | None      |
| boilerplate.R      | Template script with standard R script structure                   | None      |
| break.R            | Demonstrate use of `break` in loops                                | None      |
| browse.R           | Demonstrate debugging with `browser()` in R                        | None      |
| control_flow.R     | Overview of control flow structures in R                           | None      |
| next.R             | Demonstrate use of `next` to skip loop iterations                  | None      |
| preallocate.R      | Show performance benefits of preallocating vectors                 | None      |
| sample.R           | Demonstrate random sampling and generation of random numbers       | None      |

# Basic Script Usage
| Script Name        | Basic Usage |
| ------------------ | ----------- |
| Florida.R          | Rscript Florida.R |
| R_conditionals.R   | Rscript R_conditionals.R |
| Ricker.R           | Rscript Ricker.R |
| TreeHeight.R       | Rscript TreeHeight.R |
| Vectorize1.R       | Rscript Vectorize1.R |
| Vectorize2.R       | Rscript Vectorize2.R |
| apply1.R           | Rscript apply1.R |
| apply2.R           | Rscript apply2.R |
| basic_io.R         | Rscript basic_io.R |
| boilerplate.R      | Rscript boilerplate.R |
| break.R            | Rscript break.R |
| browse.R           | Rscript browse.R |
| control_flow.R     | Rscript control_flow.R |
| next.R             | Rscript next.R |
| preallocate.R      | Rscript preallocate.R |
| sample.R           | Rscript sample.R |

## Expected Output
| Script Name        | Expected Output |
| ------------------ | --------------- |
| Florida.R          | Prints analysis results or plots showing Florida annual mean temperature trends |
| R_conditionals.R   | Prints results of conditional statements to the console |
| Ricker.R           | Outputs simulated population dynamics values over time |
| TreeHeight.R       | Prints calculated tree heights in the terminal |
| Vectorize1.R       | Prints runtime comparison between loop-based and vectorised code |
| Vectorize2.R       | Prints further performance comparison results for vectorisation |
| apply1.R           | Prints results of apply functions on matrices/data frames |
| apply2.R           | Prints outputs of apply-family functions on lists or complex objects |
| basic_io.R         | Reads input file and prints processed data to console |
| boilerplate.R      | Prints placeholder output demonstrating standard script structure |
| break.R            | Demonstrates early loop termination via printed output |
| browse.R           | Enters debugging mode and shows variable inspection in console |
| control_flow.R     | Prints outputs from control flow examples |
| next.R             | Demonstrates skipped loop iterations via printed output |
| preallocate.R      | Prints runtime comparison between preallocated and non-preallocated vectors |
| sample.R           | Prints randomly generated samples or vectors |

## What I found challenge
The most challenging part in this week was understanding the performance differences between loops and vectorised operations in R. Although I know that vectorisation makes the code run much faster, it was not always intuitive to translate loop thinking into vectorised form, especially when I working with conditional logic and matrix operations.

Another difficulty was learning to use the apply family of functions properly. It is hard to choose the correct function (apply, lapply, sapply) and understanding their return types required careful attention.

## Author and Contact

Name: Ximan Ding

Email: x.ding25@imperial.ac.uk

Institution: Imperial College London