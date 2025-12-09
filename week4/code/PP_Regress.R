# Language: R
# Script: PP_Regress.R
# Des: Visualizing regression analyses of predator–prey body size relationships
# Usage: Rscript PP_Regress.R
# Date: Nov, 2025
# Author: Ximan Ding (x.ding25@imperial.ac.uk)

rm(list = ls())  # Clear the workspace

# Load ggplot2 for plotting. Stop with an informative message if not installed.
if (!require("ggplot2", quietly = TRUE, character.only = TRUE)) {
  stop("The 'ggplot2' package is required but not installed. Please install it with install.packages('ggplot2').")
}

# Read the predator–prey dataset using a relative path
# Make sure this script is in the 'Code' directory and the data in '../data/'
MyDF <- read.csv("../data/EcolArchives-E089-51-D1.csv", stringsAsFactors = TRUE)

# Ensure that prey masses are all in grams
# The column Prey.mass.unit is either "g" or "mg"
# Convert all "mg" to "g" and then set the units to "g"
if ("Prey.mass.unit" %in% names(MyDF)) {
  mg_idx <- MyDF$Prey.mass.unit == "mg"
  MyDF$Prey.mass[mg_idx] <- MyDF$Prey.mass[mg_idx] / 1000  # mg -> g
  MyDF$Prey.mass.unit[mg_idx] <- "g"
}

# Remove rows with missing predator or prey mass
MyDF <- MyDF[!is.na(MyDF$Prey.mass) & !is.na(MyDF$Predator.mass), ]

# Keep only strictly positive masses (needed for log10)
MyDF <- MyDF[MyDF$Prey.mass > 0 & MyDF$Predator.mass > 0, ]

# Create log10-transformed columns (for convenience)
MyDF$log10PreyMass     <- log10(MyDF$Prey.mass)
MyDF$log10PredatorMass <- log10(MyDF$Predator.mass)

if (!dir.exists("../results")) {
  dir.create("../results", recursive = TRUE)
}

# The figure should show log10 predator vs log10 prey mass,
# with separate regression lines by Predator.lifestage.
# We also facet by Type.of.feeding.interaction to mimic the
# example in the practical “Visualizing Regression analyses”.

# Build the ggplot object
p <- ggplot(
  MyDF,
  aes(
    x     = log10PreyMass,
    y     = log10PredatorMass,
    colour = Predator.lifestage
  )
) +
  geom_point(alpha = 0.6) +  # semi-transparent points
  geom_smooth(method = "lm", se = FALSE, fullrange = TRUE) +  # regression lines
  facet_wrap(~ Type.of.feeding.interaction) +  # one panel per feeding type
  xlab("log10 Prey mass (g)") +
  ylab("log10 Predator mass (g)") +
  labs(colour = "Predator life stage") +
  theme_bw() +
  theme(
    legend.position = "bottom",
    strip.background = element_rect(fill = "grey90"),
    strip.text = element_text(face = "bold")
  )

# Save the plot to a PDF file in the results directory
pdf("../results/PP_Regress.pdf", width = 11.7, height = 8.3)  # A4-ish landscape
print(p)
dev.off()

## We want one linear regression for each combination of:
##   - Type.of.feeding.interaction
##   - Predator.lifestage
## Response   : log10PredatorMass
## Predictor  : log10PreyMass
## We will extract:
##   - intercept
##   - slope
##   - R^2
##   - F-statistic
##   - p-value (overall regression)
##   - n (sample size)
# Get unique levels for grouping
feeding_types <- levels(MyDF$Type.of.feeding.interaction)
life_stages   <- levels(MyDF$Predator.lifestage)

# Initialise an empty results data frame
reg_results <- data.frame(
  FeedingType        = character(),
  Predator.lifestage = character(),
  Intercept          = numeric(),
  Slope              = numeric(),
  R2                 = numeric(),
  Fstat              = numeric(),
  Pvalue             = numeric(),
  N                  = integer(),
  stringsAsFactors   = FALSE
)

# Loop over all combinations of feeding type and life stage
for (ft in feeding_types) {
  for (ls in life_stages) {
    
    # Subset the data for this combination
    sub_df <- subset(
      MyDF,
      Type.of.feeding.interaction == ft &
        Predator.lifestage == ls
    )
    
    # Remove any non-finite log10 values (just in case)
    sub_df <- sub_df[
      is.finite(sub_df$log10PreyMass) &
        is.finite(sub_df$log10PredatorMass),
    ]
    
    # We need at least 3 points to fit a sensible regression
    if (nrow(sub_df) >= 3) {
      
      # Fit the linear model: log10PredatorMass ~ log10PreyMass
      fit  <- lm(log10PredatorMass ~ log10PreyMass, data = sub_df)
      sfit <- summary(fit)
      
      # Extract coefficients
      intercept <- coef(fit)[1]
      slope     <- coef(fit)[2]
      
      # Extract R^2
      r2 <- sfit$r.squared
      
      # Extract F-statistic and compute p-value
      fstat_vals <- sfit$fstatistic  # named numeric vector: value, num df, den df
      fstat      <- as.numeric(fstat_vals[1])
      df1        <- as.numeric(fstat_vals[2])
      df2        <- as.numeric(fstat_vals[3])
      pval       <- pf(fstat, df1, df2, lower.tail = FALSE)
      
      # Append this result as one row
      reg_results <- rbind(
        reg_results,
        data.frame(
          FeedingType        = ft,
          Predator.lifestage = ls,
          Intercept          = intercept,
          Slope              = slope,
          R2                 = r2,
          Fstat              = fstat,
          Pvalue             = pval,
          N                  = nrow(sub_df),
          stringsAsFactors   = FALSE
        )
      )
    }
  }
}

# Write the regression results to a CSV file
write.csv(
  reg_results,
  file      = "../results/PP_Regress_Results.csv",
  row.names = FALSE
)

cat("PP_Regress.R finished successfully.\n")
cat("Figure saved to ../results/PP_Regress.pdf\n")
cat("Regression table saved to ../results/PP_Regress_Results.csv\n")
