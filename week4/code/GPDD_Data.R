# Language: R
# Script: GPDD_Data.R
# Des: Plot GPDD (Global Population Dynamics Database) locations on a world map
# Usage: Rscript GPDD_Data.R
# Date: Nov, 2025
# Author: Ximan Ding (x.ding25@imperial.ac.uk)

# This script:
#  1. Loads the filtered GPDD data from ../data/GPDDFiltered.RData
#  2. Extracts latitude and longitude columns
#  3. Plots a world map and overlays all GPDD locations
#  4. Saves the result as a PDF in ../results/GPDD_Map.pdf
#  5. Adds brief comments on potential sampling bias in GPDD

# Assumption:
#  - You run this script from the "code" directory so that
#    "../data" and "../results" are correct relative paths.

# We need the 'maps' package (note the 's' at the end, not 'map').
# If it is not installed, install it into the user library and then load it.
if (!require("maps", quietly = TRUE)) {
  install.packages("maps", repos = "https://cloud.r-project.org")
  library(maps)
}

# Load the filtered GPDD data (the .RData file may contain one or more objects).
gpdd_file <- "../data/GPDDFiltered.RData"

if (!file.exists(gpdd_file)) {
  stop("Cannot find GPDDFiltered.RData in ../data/. Check your working directory and path.")
}

loaded_objects <- load(gpdd_file)  # returns the names of loaded objects

if (length(loaded_objects) == 0) {
  stop("No objects were loaded from GPDDFiltered.RData.")
}

# For simplicity, assume the first loaded object is the main GPDD dataset.
gpdd_raw <- get(loaded_objects[1])

# Basic check that the loaded object is a data frame (or similar).
if (!is.data.frame(gpdd_raw)) {
  stop("Loaded GPDD object is not a data.frame. Check the contents of GPDDFiltered.RData.")
}

# Column names may be "Latitude", "Lat", "lat", etc.
col_names <- names(gpdd_raw)

# Find candidate latitude and longitude columns using pattern matching.
lat_candidates <- grep("lat", col_names, ignore.case = TRUE, value = TRUE)
lon_candidates <- grep("lon|long", col_names, ignore.case = TRUE, value = TRUE)

if (length(lat_candidates) == 0 || length(lon_candidates) == 0) {
  stop("Could not automatically find latitude/longitude columns in GPDD data.\n",
       "Please check the column names in GPDDFiltered.RData.")
}

lat_col <- lat_candidates[1]
lon_col <- lon_candidates[1]

# Extract coordinates and remove rows with missing values.
gpdd_coords <- gpdd_raw[, c(lon_col, lat_col)]
names(gpdd_coords) <- c("Longitude", "Latitude")

gpdd_coords <- gpdd_coords[!is.na(gpdd_coords$Longitude) & !is.na(gpdd_coords$Latitude), ]

if (nrow(gpdd_coords) == 0) {
  stop("After removing NAs, there are no GPDD locations to plot.")
}

# Open a PDF device in the ../results directory.
# Width and height are chosen for a landscape A4-like page.
pdf("../results/GPDD_Map.pdf", width = 11.7, height = 8.3)

# Draw a simple world map.
map("world",
    fill = TRUE,      # fill in country polygons
    col  = "grey85",  # country color
    bg   = "white",   # background (ocean) color
    lty  = 1,
    lwd  = 0.5)

# Add axes (latitude/longitude lines).
map.axes()

# Overlay GPDD locations as red points.
points(gpdd_coords$Longitude,
       gpdd_coords$Latitude,
       pch = 20,      # filled circles
       col = "red",
       cex = 0.6)

# Add a main title to the figure.
title(main = "Global Population Dynamics Database (GPDD) Locations")

# Close the PDF device to write the file to disk.
dev.off()

# From the plotted map, GPDD locations are typically concentrated in
# Europe and North America, with fewer records from tropical regions,
# Africa, South America and parts of Asia.
#
# This indicates geographic sampling bias:
#   - Temperate and economically developed regions are over-represented.
#   - Tropical and less-developed regions are under-represented.
#
# As a result, global analyses based on GPDD may mainly reflect
# species and ecosystems from well-sampled areas and may not
# generalise well to poorly sampled regions.