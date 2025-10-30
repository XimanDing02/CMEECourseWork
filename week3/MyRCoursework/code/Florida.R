## Florida.R — Is Florida getting warmer?
## Following the steps from the Practicals: correlation + permutation test
## Before running: set working directory to code/, and ensure ../data/KeyWestAnnualMeanTemperature.RData exists

rm(list = ls())

## 1) Load and inspect the data (Key West annual mean temperature dataset)
load("../data/KeyWestAnnualMeanTemperature.RData")  # Loads an object named 'ats'
stopifnot(exists("ats"))
# Optional: quick inspection
print(class(ats)); print(head(ats)); plot(ats)  # The book suggests checking structure and trend with ls(), class(), head(), plot(ats)

## 2) Compute the observed correlation coefficient between Year and Temperature (Pearson)
r_obs <- cor(ats$Year, ats$Temp, method = "pearson", use = "complete.obs")

## 3) Permutation test: randomly shuffle the temperature values among years
##    Each time, recompute the correlation and store it
##    Use sample() for randomization, and set.seed() for reproducibility
set.seed(123)           # Ensures reproducible results
B <- 10000              # Number of permutations; increase if needed
r_perm <- numeric(B)

for (b in 1:B) {
  r_perm[b] <- cor(ats$Year,
                   sample(ats$Temp, replace = FALSE),  # Shuffle pairing only, no resampling
                   method = "pearson")
}

## 4) Compute p-values
## One-sided test (warming hypothesis H1: r > 0):
p_one <- mean(r_perm >= r_obs)
## Two-sided test (any trend):
p_two <- mean(abs(r_perm) >= abs(r_obs))

## 5) Visualize the permutation null distribution and the observed correlation
hist(r_perm,
     main = "Permutation null distribution for r(Year, Temp)",
     xlab = "r under H0 (temperatures randomly assigned to years)")
abline(v = r_obs, lwd = 2)
legend("topleft",
       legend = c(paste0("observed r = ", round(r_obs, 3)),
                  paste0("one-sided p = ", signif(p_one, 3)),
                  paste0("two-sided p = ", signif(p_two, 3))),
       bty = "n")

## 6) Print results to console
cat("\nObserved Pearson r:", r_obs,
    "\nOne-sided p (warming):", p_one,
    "\nTwo-sided p:", p_two, "\n")
