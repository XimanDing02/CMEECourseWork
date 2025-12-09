# Language: R
# Script: plotLin.R
# Des: Plot a simple linear relationship and fitted regression line
# Usage: Rscript plotLin.R
# Date: Nov, 2025
# Author: Ximan Ding (x.ding25@imperial.ac.uk)

rm(list = ls())

# Create results directory if it does not exist
if (!dir.exists("../results")) {
  dir.create("../results", recursive = TRUE)
}

# Set a random seed so results are reproducible
set.seed(123)

# Generate an explanatory variable x
# Here we generate 50 evenly spaced points between 0 and 10
x <- seq(from = 0, to = 10, length.out = 50)

# Generate a response variable y that follows a linear relationship
# y = beta0 + beta1 * x + random error
beta0 <- 2          # intercept
beta1 <- 1.5        # slope
sigma <- 2          # standard deviation of the noise

# Add Gaussian noise (rnorm) to create more realistic data
y <- beta0 + beta1 * x + rnorm(n = length(x), mean = 0, sd = sigma)

# Fit a simple linear regression model: y ~ x
lin_model <- lm(y ~ x)

# Print a short summary to the console (useful when running in terminal)
cat("### Linear model summary ###\n")
print(summary(lin_model))

# Open a PDF device to save the plot
# The figure will be saved as ../results/plotLin.pdf
pdf("../results/plotLin.pdf", width = 7, height = 5)

# Plot the raw data as points
plot(
  x, y,
  pch = 16,                      # solid dots
  col = "darkblue",              # point colour
  xlab = "Explanatory variable x",
  ylab = "Response variable y",
  main = "Simple Linear Relationship and Fitted Line"
)

# Add the fitted regression line
abline(lin_model, col = "red", lwd = 2)

# Add a simple legend
legend(
  "topleft",
  legend = c("Data", "Fitted line"),
  pch = c(16, NA),
  lty = c(NA, 1),
  col = c("darkblue", "red"),
  bty = "n"
)

# Close the PDF device
dev.off()

# Extract coefficients (intercept and slope) and save to CSV
coef_df <- data.frame(
  Intercept = coef(lin_model)[1],
  Slope = coef(lin_model)[2]
)

write.csv(
  coef_df,
  "../results/plotLin_coefficients.csv",
  row.names = FALSE
)

cat("Plot saved to ../results/plotLin.pdf\n")
cat("Coefficients saved to ../results/plotLin_coefficients.csv\n")
