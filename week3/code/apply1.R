# Language: R
# Script: apply1.R
# Des: Demonstrate the use of the apply() function on a matrix
# Usage: Rscript apply1.R
# Date: Oct, 2025
# Author: Ximan Ding (x.ding25@imperial.ac.uk)

# 1. BUILD A RANDOM MATRIX
# Create a 10 x 10 matrix with random values from a normal distribution
M <- matrix(rnorm(100), 10, 10)

# 2. APPLY MEAN FUNCTION TO EACH ROW
# Use apply() to calculate the mean of each row
RowMeans <- apply(M, 1, mean)

# Print the row means
print("Row means:")
print(RowMeans)

# 3. APPLY VARIANCE FUNCTION TO EACH ROW
# Use apply() to calculate the variance of each row
RowVars <- apply(M, 1, var)

# Print the row variances
print("Row variances:")
print(RowVars)

# 4. APPLY MEAN FUNCTION TO EACH COLUMN
# Use apply() to calculate the mean of each column
ColMeans <- apply(M, 2, mean)

# Print the column means
print("Column means:")
print(ColMeans)