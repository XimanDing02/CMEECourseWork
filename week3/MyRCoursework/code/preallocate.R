# ====================================
# preallocate.R (clean benchmark for x = 1000)
# Compare timing with and without pre-allocation (no prints inside loops)
# ====================================

NoPreallocFun <- function(x) {
  a <- vector()  # empty vector
  for (i in 1:x) {
    a <- c(a, i) # repeated resize
  }
  a
}

PreallocFun <- function(x) {
  a <- rep(NA, x)  # pre-allocated vector
  for (i in 1:x) {
    a[i] <- i      # in-place assignment
  }
  a
}

x <- 1000

cat("== Timing without pre-allocation ==\n")
print(system.time(NoPreallocFun(x)))

cat("== Timing with pre-allocation ==\n")
print(system.time(PreallocFun(x)))
