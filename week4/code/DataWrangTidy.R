# Language: R
# Script: DataWrangTidy.R
# Des: Wrangle the Pound Hill dataset using tidyverse (dplyr, tidyr)
# Usage: Rscript DataWrangTidy.R
# Date: Nov, 2025
# Author: Ximan Ding (x.ding25@imperial.ac.uk)
install.packages(c("dplyr", "tidyr"))

library(dplyr)
library(tidyr)

# header = FALSE because the raw data don't have real headers
# We read as a matrix so that we keep everything as character initially
MyData <- as.matrix(read.csv("../data/PoundHillData.csv", header = FALSE))

# header = TRUE because we do have metadata headers
# sep = ";" because the description field contains commas
MyMetaData <- read.csv("../data/PoundHillMetaData.csv", header = TRUE, sep = ";")

# Quick look at the raw data
head(MyData)
dim(MyData)
str(MyData)

# You can also inspect them interactively in RStudio:
# View(MyData)
# View(MyMetaData)

# Put species into columns and treatments (Cultivation/Block/Plot/Quadrat)
# into rows by transposing the matrix
MyData <- t(MyData)
head(MyData)
dim(MyData)

# Empty strings ("") in the raw data represent true absences
# Replace them with "0" BEFORE converting to data frame
MyData[MyData == ""] <- "0"

# Drop the first row (it contains the column names, not data)
# stringsAsFactors = FALSE to keep character columns as characters
TempData <- as.data.frame(MyData[-1, ], stringsAsFactors = FALSE)

# Assign column names from the first row of the transposed matrix
colnames(TempData) <- MyData[1, ]

# Convert to a tibble for nicer printing and tidyverse workflows
TempData <- as_tibble(TempData)

# Check the structure after this step
glimpse(TempData)

# The first four columns are identifiers (Cultivation, Block, Plot, Quadrat)
# All remaining columns are species and should be gathered into key–value pairs
MyWrangledData <- TempData %>%
  gather(
    key   = "Species",           # New column for species names
    value = "Count",             # New column for counts
    -Cultivation, -Block, -Plot, -Quadrat  # All other columns become Species/Count
  )

# Convert categorical variables to factors and Count to integer
MyWrangledData <- MyWrangledData %>%
  mutate(
    Cultivation = factor(Cultivation),
    Block       = factor(Block),
    Plot        = factor(Plot),
    Quadrat     = factor(Quadrat),
    Count       = as.integer(Count)
  )

str(MyWrangledData)
head(MyWrangledData)
dim(MyWrangledData)
glimpse(MyWrangledData)

# Here you can add your own exploration using dplyr and ggplot2, e.g.:
# MyWrangledData %>%
#   group_by(Species) %>%
#   summarise(mean_count = mean(Count)) %>%
#   arrange(desc(mean_count))
#
# Or simple plots, e.g.:
# ggplot(MyWrangledData, aes(x = Count)) +
#   geom_histogram() +
#   theme_minimal()
