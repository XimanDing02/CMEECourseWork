# Language: R
# Script: TreeHeight.R
# Des: Calculate tree heights from distance and angle for all trees in trees.csv
# Usage: Rscript TreeHeight.R
# Date: Oct, 2025
# Author: Ximan Ding (x.ding25@imperial.ac.uk)

# 1. READ INPUT DATA USING RELATIVE PATH
# Load the tree measurement data from the data directory
MyData <- read.csv("../data/trees.csv", header = TRUE)

# Check the structure of the imported data
str(MyData)

# 2. DEFINE TREE HEIGHT FUNCTION
# This function calculates tree height using trigonometry
# height = distance * tan(angle in radians)
TreeHeight <- function(degrees, distance) {
  
  # Convert degrees to radians
  radians <- degrees * pi / 180
  
  # Calculate tree height
  height <- distance * tan(radians)
  
  # Return the calculated height
  return(height)
}

# 3. CALCULATE TREE HEIGHTS FOR ALL TREES
# Apply the TreeHeight function to all rows of the dataset
MyData$Tree.Height.m <- TreeHeight(
  degrees = MyData$Angle.degrees,
  distance = MyData$Distance.m
)

# 4. WRITE OUTPUT DATA TO CSV FILE
# Write the updated data frame (with tree heights) to the results directory
write.csv(MyData,
          file = "../results/TreeHts.csv",
          row.names = FALSE)

# 5. CONFIRM COMPLETION
print("Tree height calculation complete!")
print("Output file saved as ../results/TreeHts.csv")