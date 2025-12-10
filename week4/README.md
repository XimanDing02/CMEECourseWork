# Week 4 Data Wrangling, Visualization and Model Profiling

## Table of Contents
- [Week 4: Data Wrangling, Visualization and Model Profiling](#week-4-data-wrangling-visualization-and-model-profiling)
  - [Table of Contents](#table-of-contents)
  - [Project Structure](#project-structure)
  - [Brief Description](#brief-description)
  - [Languages](#languages)
  - [Installation](#installation)
  - [Dependencies](#dependencies)
  - [Scripts List](#scripts-list)
  - [Scripts Basic Usage](#scripts-basic-usage)
  - [What I found challenge](#what-i-found-challenge)
  - [Author and Contact](#author-and-contact)

## Project Structure
This week4 structure is:

```plaintext
./week4/
│
├── code/
│   ├── DataWrang.R
│   ├── DataWrangTidy.R
│   ├── GPDD_Data.R
│   ├── Girko.R
│   ├── LV1.py
│   ├── LV2.py
│   ├── MyBars.R
│   ├── PP_Dists.R
│   ├── PP_Regress.R
│   ├── SQLinR.R
│   ├── Test.sqlite
│   ├── VisualizingRegressionAnalyses.R
│   ├── plotLin.R
│   ├── profileme.py
│   └── profileme2.py
│
├── data/
│   ├── EcolArchives-E089-51-D1.csv
│   ├── GPDDFiltered.RData
│   ├── PoundHillData.csv
│   ├── PoundHillMetaData.csv
│   ├── Resource.csv
│   └── Results.txt
│
├── results/
│   └── (currently empty — ignored by .gitignore)
│
└── readme.md
```

## Brief Description
1. This week focuses on data wrangling and data management using both R and Python.
2. Core skills include data cleaning, reshaping, and transformation with base R and tidyverse-style workflows.
3. Introduction to statistical distributions and regression analysis for biological datasets.
4. Practice in data visualization, including plotting linear relationships and regression results.
5. Use of SQL within R to query and manage relational databases.
6. Application of population and ecological models (e.g. Lotka–Volterra models) using Python.
7. Analysis through code profiling to compare efficiency of different implementations.
8. Emphasis on integrating real ecological datasets into reproducible computational workflows.
9. These works are based on the Notebook and Data from https://github.com/mhasoba/TheMulQuaBio.git.

## Languages
```
R 
# used for data wrangling, statistical analysis, visualization, and SQL integration
Python
# used for ecological modelling
```

## **Installation**
```
Ensure that you are using a UNIX-based environment.

git clone https://github.com/XimanDing02/CMEECourseWork.git
```

## **Dependencies** 
Most of the scripts require both base R and Python 3,and can be run directly in the terminal using Rscript and python3.

Installation R: `sudo apt install r-base` (Run in the terminal)
Installation Python: `sudo apt install python3` (Run in the terminal)
```
# R Packages:
tidyverse
ggplot2
dplyr
tidyr
dbplyr
RSQLite
stats
graphics
```

```
# Python Packages:
numpy
scipy
matplotlib
line_profiler
cProfile
```

## Scripts List
| Script Name        | Description                                                         | Arguments |
|--------------------|----------------------------------------------------------------------|-----------|
| DataWrang.R        | Data wrangling using base R functions on the Pound Hill dataset     | None      |
| DataWrangTidy.R    | Data wrangling using tidyverse tools on the Pound Hill dataset      | None      |
| GPDD_Data.R        | Visualisation and analysis of the GPDD dataset                      | None      |
| Girko.R            | Demonstration of Girko’s circular law using random matrices         | None      |
| LV1.py             | Basic Lotka–Volterra population model                               | None      |
| LV2.py             | Extended Lotka–Volterra population model                            | None      |
| MyBars.R           | Custom bar plot generation in R                                     | None      |
| PP_Dists.R         | Predator–prey distribution analysis                                 | None      |
| PP_Regress.R       | Regression analysis for predator–prey data                          | None      |
| SQLinR.R            | Using SQL queries inside R with SQLite database                     | None      |
| Test.sqlite        | SQLite database used for SQL–R interaction                          | None      |
| VisualizingRegressionAnalyses.R | Visualisation of regression analysis results in R       | None      |
| plotLin.R          | Linear regression plotting in R                                     | None      |
| profileme.py       | Profiling Python code performance                                   | None      |
| profileme2.py      | Advanced profiling and optimisation in Python                       | None      |

## Scripts Basic Usage
| Script Name        | Basic Usage |
|--------------------|-------------|
| DataWrang.R        | Rscript DataWrang.R |
| DataWrangTidy.R    | Rscript DataWrangTidy.R |
| GPDD_Data.R        | Rscript GPDD_Data.R |
| Girko.R            | Rscript Girko.R |
| LV1.py             | python3 LV1.py |
| LV2.py             | python3 LV2.py |
| MyBars.R           | Rscript MyBars.R |
| PP_Dists.R         | Rscript PP_Dists.R |
| PP_Regress.R       | Rscript PP_Regress.R |
| SQLinR.R           | Rscript SQLinR.R |
| Test.sqlite        | Used internally by SQLinR.R |
| VisualizingRegressionAnalyses.R | Rscript VisualizingRegressionAnalyses.R |
| plotLin.R          | Rscript plotLin.R |
| profileme.py      | python3 profileme.py |
| profileme2.py     | python3 profileme2.py |

## Expected Output
| Script Name        | Expected Output |
|--------------------|-----------------|
| DataWrang.R        | Cleaned and transformed Pound Hill dataset printed to console |
| DataWrangTidy.R    | Tidyverse-based cleaned dataset and summary statistics |
| GPDD_Data.R        | Distribution plots and summary statistics of GPDD dataset |
| Girko.R            | Visualization of eigenvalue distribution following Girko’s law |
| LV1.py             | Time-series plot of basic Lotka–Volterra population dynamics |
| LV2.py             | Time-series plot of extended Lotka–Volterra population dynamics |
| MyBars.R           | Custom bar plot displayed in plotting window |
| PP_Dists.R         | Multiple subplots showing predator–prey mass distributions |
| PP_Regress.R       | Subgroup linear regression plots and regression summaries |
| SQLinR.R           | Queried results from SQLite database printed to console |
| Test.sqlite        | SQLite database file accessed by SQLinR.R |
| VisualizingRegressionAnalyses.R | Regression diagnostic plots |
| plotLin.R          | Linear regression line plotted with data points |
| profileme.py      | Runtime profiling report printed to terminal |
| profileme2.py     | Optimized runtime profiling comparison output |

## What I found challenge
The most challenging part of this week for me was combining data wrangling, visualization, and model profiling all together into a complete workflow. Although I was already familiar with basic R and Python in previous weeks, handling real datasets required much more careful than I expected. Especially when using dplyr and tidyverse, small mistakes in column names or grouping logic could easily lead to quite strange results.
Another difficulty was working across both R and Python in the same week. Switching between different programming styles, plotting systems, and data structures took some time to adapt. But this also helped me gain a clearer understanding of the strengths of each language and how they can be used together in data analysis.

## Author and Contact

Name: Ximan Ding

Email: x.ding25@imperial.ac.uk

Institution: Imperial College London