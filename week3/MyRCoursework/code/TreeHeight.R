# TreeHeight.R
#
# Reads trees.csv and calculates tree heights for all trees in the data.
# Output into TreeHts.csv in results file 
# TreeHts.csv will contain the calculated tree heights along with the original data in the following format.
# Works with source() and Rscript.

# Original content in TreeHeight.R document 
# height = distance * tan(degrees * pi/180)
TreeHeight <- function(degrees, distance) {
  radians <- degrees * pi / 180
  height <- distance * tan(radians)
  return(height)
}

# Read the data using a relative path (Hint in question)
MyData <- read.csv("../data/trees.csv", header = TRUE)

# Calculate tree heights (in meters) and add as a new column
MyData$Tree.Height.m <- TreeHeight(MyData$Angle.degrees, MyData$Distance.m)

# Write the result to the results directory using a relative path
write.csv(MyData, "../results/TreeHts.csv", row.names = FALSE)

# Optional confirmation message
print("Done! Wrote ../results/TreeHts.csv")
