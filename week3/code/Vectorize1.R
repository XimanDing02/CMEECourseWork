# Language: R
# Script: Vectorize1.R
# Des: Demonstrate the efficiency difference between loop-based and vectorised operations
# Usage: Rscript Vectorize1.R
# Date: Oct, 2025
# Author: Ximan Ding (x.ding25@imperial.ac.uk)

# 1. GENERATE A LARGE RANDOM MATRIX
# Create a 1000 x 1000 matrix filled with random numbers
M <- matrix(runif(1000000), 1000, 1000)

# 2. DEFINE A FUNCTION TO SUM ALL ELEMENTS USING LOOPS
# This function sums all elements in a matrix using nested for loops
SumAllElements <- function(M) {
  
  # Get the dimensions of the matrix
  Dimensions <- dim(M)
  
  # Initialise the total sum
  Tot <- 0
  
  # Loop over rows
  for (i in 1:Dimensions[1]) {
    
    # Loop over columns
    for (j in 1:Dimensions[2]) {
      
      # Add each matrix element to the total
      Tot <- Tot + M[i, j]
    }
  }
  
  # Return the total sum
  return(Tot)
}

# 3. TIME THE LOOP-BASED SUM
print("Using loops, the time taken is:")
print(system.time(SumAllElements(M)))

# 4. TIME THE VECTORISED SUM
print("Using the in-built vectorised function, the time taken is:")
print(system.time(sum(M)))