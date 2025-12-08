# Language: R
# Script: Vectorize2.R
# Des: Compare loop-based and vectorised implementations of the stochastic Ricker model
# Usage: Rscript Vectorize2.R
# Date: Oct, 2025
# Author: Ximan Ding (x.ding25@imperial.ac.uk)

rm(list = ls())

# FUNCTION 1
# This function runs the stochastic Ricker model with Gaussian noise (non-vetorized)
# using nested for-loops over populations and years.
#
# ARGUMENTS:
# p0        : Initial population sizes (vector)
# r         : Intrinsic growth rate
# K         : Carrying capacity
# sigma     : Standard deviation of environmental noise
# numyears  : Number of years (time steps) to simulate
#
# OUTPUT:
# A matrix N of dimension numyears x length(p0), where each column
# represents one population time series.

stochrick <- function(p0 = runif(1000, 0.5, 1.5),
                      r = 1.2,
                      K = 1,
                      sigma = 0.2,
                      numyears = 100) {
  
  # Initialise an empty matrix to store population sizes
  N <- matrix(NA, nrow = numyears, ncol = length(p0))
  
  # Set the first year to the initial population sizes
  N[1, ] <- p0
  
  # Loop through populations
  for (pop in 1:length(p0)) {
    
    # Loop through years for each population
    for (yr in 2:numyears) {
      
      # Ricker update with one random fluctuation from a normal distribution
      N[yr, pop] <- N[yr - 1, pop] *
        exp(r * (1 - N[yr - 1, pop] / K) + rnorm(1, mean = 0, sd = sigma))
    }
  }
  
  return(N)
}

# FUNCTION 2
# This function runs the same stochastic Ricker model, but vectorises (VECTORIZED)
# over populations. It removes the inner loop over populations and
# updates all populations for a given year at once.
#
# The model equation is:
# N[t+1, ] = N[t, ] * exp(r * (1 - N[t, ] / K) + epsilon_t)
# where epsilon_t ~ Normal(0, sigma) independently for each population.

stochrickvect <- function(p0 = runif(1000, 0.5, 1.5),
                          r = 1.2,
                          K = 1,
                          sigma = 0.2,
                          numyears = 100) {
  
  # Initialise an empty matrix to store population sizes
  N <- matrix(NA, nrow = numyears, ncol = length(p0))
  
  # Set the first year to the initial population sizes
  N[1, ] <- p0
  
  # Loop only over years; populations are updated in a vectorised way
  for (yr in 2:numyears) {
    
    # Generate one random fluctuation for each population
    eps_t <- rnorm(length(p0), mean = 0, sd = sigma)
    
    # Vectorised Ricker update for all populations at once
    N[yr, ] <- N[yr - 1, ] *
      exp(r * (1 - N[yr - 1, ] / K) + eps_t)
  }
  
  return(N)
}


# PERFORMANCE COMPARISON
# Here we time the non-vectorised and vectorised implementations
# using the same parameter values to compare their performance.
# Time the loop-based version
print("Non-vectorised stochastic Ricker takes:")
print(system.time(res1 <- stochrick()))

# Time the vectorised version
print("Vectorised stochastic Ricker takes:")
print(system.time(res2 <- stochrickvect()))