# ============================================
# Vectorize2.R — Stochastic Ricker: loop vs vectorized
# ============================================

rm(list = ls())
set.seed(123)  # for reproducibility of the timing run

# --------------------------
# Slow baseline: double loop
# --------------------------
stochrick <- function(p0 = runif(1000, 0.5, 1.5),
                      r = 1.2, K = 1, sigma = 0.2,
                      numyears = 100) {

  # Matrix shape: rows = years, cols = populations
  N <- matrix(NA_real_, nrow = numyears, ncol = length(p0))
  N[1, ] <- p0

  if (numyears >= 2) {
    for (pop in 1:length(p0)) {             # loop over populations
      for (yr in 2:numyears) {              # loop over years
        eps <- rnorm(1, mean = 0, sd = sigma)
        Nt1 <- N[yr - 1, pop]
        N[yr, pop] <- Nt1 * exp(r * (1 - Nt1 / K) + eps)
      }
    }
  }
  N
}

# -------------------------------------------
# Vectorized across populations (fast version)
# One loop over time only; update all pops at once
# -------------------------------------------
stochrickvect <- function(p0 = runif(1000, 0.5, 1.5),
                          r = 1.2, K = 1, sigma = 0.2,
                          numyears = 100) {

  N <- matrix(NA_real_, nrow = numyears, ncol = length(p0))
  N[1, ] <- p0

  if (numyears >= 2) {
    for (yr in 2:numyears) {                # only time loop remains
      eps <- rnorm(length(p0), 0, sigma)     # vector of noises, one per population
      Nt1 <- N[yr - 1, ]                     # all populations at t-1
      growth <- r * (1 - Nt1 / K)
      N[yr, ] <- Nt1 * exp(growth + eps)     # vectorized update
    }
  }
  N
}

# --------------------------
# Benchmark & sanity checks
# --------------------------
cat("Stochastic Ricker (double loop) timing:\n")
print(system.time(res_loop <- stochrick()))

cat("Vectorized stochastic Ricker timing:\n")
print(system.time(res_vec  <- stochrickvect()))

# basic checks
stopifnot(all(dim(res_loop) == dim(res_vec)))
# the two runs won't be identical because they drew different random numbers;
# but shapes should match and values should be in reasonable ranges.

# Optional quick plot of a few trajectories (interactive)
# matplot(res_vec[ , 1:20], type = "l", lty = 1, col = 1,
#         xlab = "Year", ylab = "N", main = "20 stochastic Ricker trajectories")

cat("Done.\n")
