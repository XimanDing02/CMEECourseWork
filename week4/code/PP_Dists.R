# Language: R
# Script: PP_Dists.R
# Des: Draw and save predator/prey/body-size-ratio distributions and compute summary stats
# Usage: Rscript PP_Dists.R
# Date: Nov, 2025
# Author: Ximan Ding (x.ding25@imperial.ac.uk)

rm(list = ls())            # Clear workspace
graphics.off()             # Close any open graphic devices

# Use relative paths as required in the practical
data_dir    <- "../data"
results_dir <- "../results"

# Create results directory if it does not exist
if (!dir.exists(results_dir)) {
  dir.create(results_dir, recursive = TRUE)
}

data_file   <- file.path(data_dir, "EcolArchives-E089-51-D1.csv")

# Read predator–prey body mass dataset
MyDF <- read.csv(data_file, header = TRUE)

# Convert some columns to factors (we will group by feeding interaction type)
MyDF$Type.of.feeding.interaction <- as.factor(MyDF$Type.of.feeding.interaction)
MyDF$Location                    <- as.factor(MyDF$Location)

# Ensure prey masses are in grams
# The column Prey.mass.unit can contain "g" and "mg"
# Convert mg to g and update the unit to "g"
mg_idx <- MyDF$Prey.mass.unit == "mg"
MyDF$Prey.mass[mg_idx]       <- MyDF$Prey.mass[mg_idx] / 1000
MyDF$Prey.mass.unit[mg_idx]  <- "g"

# Remove rows with missing key values (defensive)
MyDF <- MyDF[!is.na(MyDF$Predator.mass) &
               !is.na(MyDF$Prey.mass) &
               !is.na(MyDF$Type.of.feeding.interaction), ]

# Log10 predator mass (g)
MyDF$log10PredMass  <- log10(MyDF$Predator.mass)

# Log10 prey mass (g)
MyDF$log10PreyMass  <- log10(MyDF$Prey.mass)

# Predator–prey body-mass ratio: prey / predator
MyDF$SizeRatio      <- MyDF$Prey.mass / MyDF$Predator.mass
MyDF$log10SizeRatio <- log10(MyDF$SizeRatio)

# Given a number of groups, choose a roughly square layout (nrow, ncol)
get_layout <- function(n) {
  ncol <- ceiling(sqrt(n))
  nrow <- ceiling(n / ncol)
  return(list(nrow = nrow, ncol = ncol))
}


feeding_types <- levels(MyDF$Type.of.feeding.interaction)
n_types       <- length(feeding_types)
layout_info   <- get_layout(n_types)

pdf(file.path(results_dir, "Pred_Subplots.pdf"),
    width = 11.7, height = 8.3)   # A4 landscape-ish

par(mfrow = c(layout_info$nrow, layout_info$ncol),
    mar = c(4, 4, 3, 1),          # margins: bottom, left, top, right
    oma = c(0, 0, 4, 0))          # outer margins (for overall title)

for (ft in feeding_types) {
  subset_df <- MyDF[MyDF$Type.of.feeding.interaction == ft, ]
  hist(subset_df$log10PredMass,
       main = ft,
       xlab = "log10(Predator mass (g))",
       ylab = "Frequency")
}

mtext("Predator mass distributions by feeding interaction type",
      outer = TRUE, cex = 1.2, font = 2)

dev.off()

pdf(file.path(results_dir, "Prey_Subplots.pdf"),
    width = 11.7, height = 8.3)

par(mfrow = c(layout_info$nrow, layout_info$ncol),
    mar = c(4, 4, 3, 1),
    oma = c(0, 0, 4, 0))

for (ft in feeding_types) {
  subset_df <- MyDF[MyDF$Type.of.feeding.interaction == ft, ]
  hist(subset_df$log10PreyMass,
       main = ft,
       xlab = "log10(Prey mass (g))",
       ylab = "Frequency")
}

mtext("Prey mass distributions by feeding interaction type",
      outer = TRUE, cex = 1.2, font = 2)

dev.off()

pdf(file.path(results_dir, "SizeRatio_Subplots.pdf"),
    width = 11.7, height = 8.3)

par(mfrow = c(layout_info$nrow, layout_info$ncol),
    mar = c(4, 4, 3, 1),
    oma = c(0, 0, 4, 0))

for (ft in feeding_types) {
  subset_df <- MyDF[MyDF$Type.of.feeding.interaction == ft, ]
  hist(subset_df$log10SizeRatio,
       main = ft,
       xlab = "log10(Prey mass / Predator mass)",
       ylab = "Frequency")
}

mtext("Prey–predator size-ratio distributions by feeding interaction type",
      outer = TRUE, cex = 1.2, font = 2)

dev.off()

# We will compute log10 mean and median for:
# - Predator mass
# - Prey mass
# - Prey/Predator size ratio
# for each feeding interaction type.

vars       <- c("log10PredMass", "log10PreyMass", "log10SizeRatio")
var_labels <- c("log10PredatorMass", "log10PreyMass", "log10PreyPredSizeRatio")

results_list <- list()

for (ft in feeding_types) {
  subset_df <- MyDF[MyDF$Type.of.feeding.interaction == ft, ]
  
  for (i in seq_along(vars)) {
    vname <- vars[i]
    vlab  <- var_labels[i]
    vvals <- subset_df[[vname]]
    
    # Compute mean and median, ignoring any NA/Inf
    vvals <- vvals[is.finite(vvals)]
    
    res_row <- data.frame(
      Feeding.type = ft,
      Variable     = vlab,
      LogMean      = mean(vvals, na.rm = TRUE),
      LogMedian    = median(vvals, na.rm = TRUE),
      stringsAsFactors = FALSE
    )
    
    results_list[[length(results_list) + 1]] <- res_row
  }
}

PP_Results <- do.call(rbind, results_list)

# Save results to CSV
write.csv(PP_Results,
          file = file.path(results_dir, "PP_Results.csv"),
          row.names = FALSE)

