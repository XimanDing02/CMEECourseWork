# Language: R
# Script: apply2.R
# Des: Demonstrate the use of apply() with a user-defined function
# Usage: Rscript apply2.R
# Date: Oct, 2025
# Author: Ximan Ding (x.ding25@imperial.ac.uk)

# USER-DEFINED FUNCTION TO BE USED WITH apply()
# This function takes a numeric vector v as input.
# If the sum of the elements of v is greater than 0,
# it multiplies every element of v by 100.
# Otherwise, it simply returns the original vector.
SomeOperation <- function(v) {
  
  # Check whether the sum of the vector is positive
  if (sum(v) > 0) {
    
    # If positive, scale the vector by a factor of 100
    return(v * 100)
    
  } else {
    
    # Otherwise, return the original vector unchanged
    return(v)
  }
}

# CREATE A RANDOM MATRIX
# Generate a 10 x 10 matrix with random values from a normal distribution
M <- matrix(rnorm(100), 10, 10)

# APPLY THE FUNCTION TO EACH ROW OF THE MATRIX
# Use apply() to run SomeOperation on each row (margin = 1)
Result <- apply(M, 1, SomeOperation)

# Print the result
print("Result of applying SomeOperation to each row:")
print(Result)