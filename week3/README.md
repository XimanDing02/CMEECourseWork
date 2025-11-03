# Biological Computing in R

This week talked about the R. This section talked about the introduction of **vectorization**, and **apply family of functions** in R.

Also, we learned how to improve computational method between loops and vectorized appproaches, and practice debugging using R.

This week3 structure is:

```plaintext

week3/
├── MyRCoursework/
│   ├── code/
│   │   ├── Florida.R
│   │   ├── MyResults.Rout
│   │   ├── R_conditionals.R
│   │   ├── Ricker.R
│   │   ├── Rplots.pdf
│   │   ├── TreeHeight.R
│   │   ├── Vectorize1.R
│   │   ├── Vectorize2.R
│   │   ├── apply1.R
│   │   ├── apply2.R
│   │   ├── basic_io.R
│   │   ├── boilerplate.R
│   │   ├── break.R
│   │   ├── control_flow.R
│   │   ├── next.R
│   │   ├── preallocate.R
│   │   ├── sample.R
│   │   └── README.md
│   │
│   ├── data/
│   │   └── trees.csv
│   │
│   ├── results/
│   │   ├── MyData.csv
│   │   └── TreeHts.csv
│   │
│   ├── .RData
│   ├── .Rhistory
│
└── README.md

```

## apply1.R
This section illustrate the use of `apply` function on a random matrix.

We want to calculate the `mean` and `variance` of each row and column.

## apply2.R
It defined a function `SomeOperation()` and applies  it row-wise using `appy()`.

If the sum is positive, we ask the R to make the values are multiplied by 100; otherwise return itself.

## sample.R
Compared different ways (`loopy_sample1()`, `loopy_sample2()`, `loopy_sample3()`, `lapply_sample()`, `sapply_sample()`) to perform repeated random sampling and compute sample means.

These ways include the loop without preallocation, loop with preallocation, loop with list preallocation, two vectorized implementations respectively.

## Ricker.R
Use the deterministic Ricker population modelto simulates population growth over a number of generations and plot the trajectory of results.

## Vectorize2.R
Compare two stochastic Ricker model `stochrick()` double loop ()which is slow and `stochrickvect()` vectorized (which is fast). 

## browse.R
This is a question which about debudding in R to show the `brower()` to perse and inspect code.

## Practicals
### TreeHeight.R
This is the first practical this week. We need to download the `trees.csv` first, and calculate the tree height for trees in the data. Finally we need to create a CSV file `TreeHts.csv` in `../esults/` containing species name, distance, angle and calculated height.

### Florida.R
We need to analyse the Florida vegetation dataset in `../data/Florida.csv`. using `apply`, `tapply` and `by` to summarisespecies abundance and environmental variables.

## How to run
In R or in termial with Rscript:
```plaintext
setwd("~/Documents/CMEECourseWork/week3/MyRCoursework/code")

# Example runs:
Rscript apply1.R
Rscript apply2.R
Rscript sample.R
Rscript Ricker.R
Rscript Vectorize2.R
Rscript browse.R
```