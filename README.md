# Raster-dataset-search
Description

This script should be used with ArcGIS when you are working with raster and mosaic datasets (currently only raster datasets are implemented). This tool helps to search rasters by choosing a field with a custom value from a selected feature class (polygon). First the location of the images has to be defined. Multiple folders can be selected. Then the script iterates through these images and checks if the selected rasters extents' intersect the feature's extent. If yes, those files are added to the current data frame. One of the small disadvantages of the tool, that it works with extents, so sometimes there are no real intersections between the features. However, it still provides a better solution than checking a folder full of images manually. A more serious drawback is that intersection can only be checked between features with the same projection. An on-the-fly transformation is planned to be implemented in the future to solve this problem.


How to use it:

1. Simply run it from the provided toolbox.


Future plans:

- Mosaic dataset support
- Projection transformation



Feel free to develop and use this script, also please don't forget to refer to my GitHub page :)
