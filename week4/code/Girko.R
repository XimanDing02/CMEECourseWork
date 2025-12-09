# Language: R
# Script: Girko.R
# Des: Plot eigenvalues of a random matrix and overlay Girko's circular law ellipse
# Usage: Rscript Girko.R
# Date: Nov, 2025
# Author: Ximan Ding (x.ding25@imperial.ac.uk)

# ggplot2 is used for plotting. The script will stop with a clear
# error message if ggplot2 is not installed.
if (!require("ggplot2", quietly = TRUE)) {
  stop("Package 'ggplot2' is required but not installed. Please install it with install.packages('ggplot2').")
}

# build_ellipse:
#   Given horizontal and vertical radii, return a data.frame with
#   the x and y coordinates of an ellipse centred at (0, 0).
build_ellipse <- function(hradius, vradius) {
  npoints <- 250                      # number of points along the ellipse
  a <- seq(0, 2 * pi, length.out = npoints + 1)  # angles
  x <- hradius * cos(a)               # x coordinates
  y <- vradius * sin(a)               # y coordinates
  
  return(data.frame(x = x, y = y))
}

set.seed(123)   # For reproducibility of the random matrix

N <- 250        # Size of the square matrix (N x N)

# Generate a random matrix with entries from N(0, 1)
M <- matrix(rnorm(N * N), nrow = N, ncol = N)

# Compute eigenvalues of the matrix
eigvals <- eigen(M)$values

# Store real and imaginary parts of eigenvalues in a data.frame for plotting
eigDF <- data.frame(
  Real      = Re(eigvals),
  Imaginary = Im(eigvals)
)

# According to Girko's circular law, eigenvalues lie (approximately)
# inside a circle of radius sqrt(N) in the complex plane.
circle_radius <- sqrt(N)

# Build the ellipse (here a circle) that represents Girko's bound
ellDF <- build_ellipse(circle_radius, circle_radius)
names(ellDF) <- c("Real", "Imaginary")

# Create a ggplot object with eigenvalues
p <- ggplot(eigDF, aes(x = Real, y = Imaginary)) +
  # Plot eigenvalues as points
  geom_point(shape = 3, size = 0.7) +
  # Add horizontal and vertical reference lines through the origin
  geom_hline(yintercept = 0, linetype = "dashed") +
  geom_vline(xintercept = 0, linetype = "dashed") +
  # Add Girko ellipse (circle)
  geom_polygon(
    data   = ellDF,
    aes(x = Real, y = Imaginary),
    fill   = "red",
    alpha  = 0.2,
    colour = NA
  ) +
  # Use equal scaling on both axes so the circle is not distorted
  coord_equal() +
  # Use a clean theme suitable for printing
  theme_bw() +
  theme(
    legend.position = "none",
    panel.grid      = element_blank()
  ) +
  # Add title and axis labels
  labs(
    title = "Girko's Circular Law: Eigenvalues of a Random Matrix",
    x     = "Real part of eigenvalues",
    y     = "Imaginary part of eigenvalues"
  )

# Ensure the results directory exists (create if it does not)
if (!dir.exists("../results")) {
  dir.create("../results", recursive = TRUE)
}

# Save the plot as a PDF in the results directory
pdf("../results/Girko.pdf")
print(p)   # Important: print the ggplot object to the PDF device
dev.off()
