# Language: R
# Script: preallocate.R
# Des: Compare performance of dynamic vector growth vs pre-allocation in R
# Usage: Rscript preallocate.R
# Date: Oct, 2025
# Author: Ximan Ding (x.ding25@imperial.ac.uk)

# FUNCTION 1
# This function grows a vector dynamically using concatenation
# Memory is repeatedly re-allocated at each iteration
NoPreallocFun <- function(x) {
  
  # Create an empty vector
  a <- vector()
  
  # Loop x times
  for (i in 1:x) {
    
    # Concatenate the new value to the existing vector
    a <- c(a, i)
  }
}

# FUNCTION 2
# This function pre-allocates memory for the vector
# Memory is allocated only once
PreallocFun <- function(x) {
  
  # Pre-allocate a vector of length x with NA values
  a <- rep(NA, x)
  
  # Loop x times
  for (i in 1:x) {
    
    # Assign values directly to pre-allocated memory
    a[i] <- i
  }
}

# PERFORMANCE COMPARISON (1000 ITERATIONS)
print("Time taken without pre-allocation:")
print(system.time(NoPreallocFun(1000)))

print("Time taken with pre-allocation:")
print(system.time(PreallocFun(1000)))