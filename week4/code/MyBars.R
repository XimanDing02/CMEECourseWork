# Language: R
# Script: MyBars.R
# Des: Create annotated linerange plot and save as PDF
# Usage: Rscript MyBars.R
# Date: Nov, 2025
# Author: Ximan Ding (x.ding25@imperial.ac.uk)

if (!requireNamespace("ggplot2", quietly = TRUE)) {
  stop("Package 'ggplot2' is not installed. Please run install.packages('ggplot2') first.")
}
library(ggplot2)

if (!file.exists("../data/Results.txt")) {
  stop("Could not find ../data/Results.txt. Are you running this from the Code/ directory?")
}

# Clear the workspace (optional but helps avoid conflicts)
rm(list = ls())

# Load required package for plotting
# If ggplot2 is not installed, run: install.packages("ggplot2")
require(ggplot2)

# Read in the results table
# ../data/Results.txt is relative to the Code/ directory
a <- read.table("../data/Results.txt", header = TRUE)

# Add a column of zeros to use as the lower end of the lineranges
# (one zero per row)
a$ymin <- rep(0, nrow(a))

# Start an empty ggplot object with the data frame 'a'
p <- ggplot(a)

# Add three sets of vertical lineranges    #
# (y1, y2, y3) with different colours      #
# First linerange (orange)
p <- p +
  geom_linerange(
    data  = a,
    aes(x = x, ymin = ymin, ymax = y1),
    linewidth = 0.5,          # line width; 'size' is deprecated for lines
    colour    = "#E69F00",    # orange
    alpha     = 0.5,          # transparency
    show.legend = FALSE
  )

# Second linerange (light blue)
p <- p +
  geom_linerange(
    data  = a,
    aes(x = x, ymin = ymin, ymax = y2),
    linewidth = 0.5,
    colour    = "#56B4E9",    # light blue
    alpha     = 0.5,
    show.legend = FALSE
  )

# Third linerange (red)
p <- p +
  geom_linerange(
    data  = a,
    aes(x = x, ymin = ymin, ymax = y3),
    linewidth = 0.5,
    colour    = "#D55E00",    # red
    alpha     = 0.5,
    show.legend = FALSE
  )

p <- p +
  geom_text(
    data  = a,
    aes(x = x, y = -500, label = Label),   # y = -500 puts labels below bars
    size  = 3,
    na.rm = TRUE                           # ignore NA labels
  )

p <- p +
  scale_x_continuous(
    "My x axis",                           # x-axis label
    breaks = seq(3, 5, by = 0.05)          # tick positions
  ) +
  scale_y_continuous("My y axis") +        # y-axis label
  theme_bw() +                             # black-and-white theme
  theme(legend.position = "none")          # no legend

# Open a PDF device in the results/ directory
pdf("../results/MyBars.pdf", width = 11.7, height = 8.3)  # A4-ish in inches

# Draw the plot into the PDF
print(p)

# Close the graphics device
dev.off()
