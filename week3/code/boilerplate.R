# Language: R
# Script: boilerplate.R
# Des: Boilerplate template for R scripts used in coursework and projects
# Usage: Rscript boilerplate.R
# Date: Oct, 2025
# Author: Ximan Ding (x.ding25@imperial.ac.uk)

# This script serves as a general template (boilerplate) for all future
# R scripts. It includes a standard header, section structure, and
# placeholders for inputs, processing, and outputs.

# 1. CLEAN WORKSPACE
# Remove all objects from the current R workspace
rm(list = ls())

# Clear R console (works in most environments)
cat("\014")

# 2. SET SEED FOR REPRODUCIBILITY (OPTIONAL)
# Set a random seed to ensure reproducible results
set.seed(123)

# 3. LOAD REQUIRED LIBRARIES
# Example: Uncomment when packages are needed
# library(ggplot2)
# library(dplyr)

# 4. INPUT DATA
# Example of reading a CSV file using a relative path
# data <- read.csv("../data/example.csv", header = TRUE)

# 5. DATA PROCESSING
# Placeholder for data cleaning, transformation, and analysis
# Example:
# summary(data)

# 6. OUTPUT RESULTS
# Example of writing results to a CSV file
# write.csv(data, "../results/output.csv")

# 7. VISUALISATION (OPTIONAL)
# Example plotting section
# plot(data$x, data$y)

# END OF SCRIPT
print("Boilerplate R script executed successfully!")
