# Raster-dataset-search
Description

This script should be used with ArcGIS when you are working with raster and mosaic datasets (currently only raster datasets are implemented). This tool helps to search rasters by choosing a field with a custom value from a selected feature class (polygon). First the location of the images has to be defined. Multiple folders can be selected. Then the script iterates through these images and checks if the selected rasters extents' intersect the feature's extent. If yes, those files are added to the current data frame. This also works with different projections (on-the-fly transformation). One of the small disadvantages of the tool, that it works with extents, so sometimes there are no real intersections between the features. However, it still provides a better solution than checking a folder full of images manually.


How to use it:

1. Simply run it from the provided toolbox inside ArcGIS.


Feel free to develop and use this script, also please don't forget to refer to my GitHub page :)
