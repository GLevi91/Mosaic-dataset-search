# Mosaic-dataset-search
Description

This script should be used with ArcGIS when you are working with mosaic datasets. A mosaic dataset is literally a collection of raster datasets, which only contains reference to them. If you have a huge collection of datasets, it might happen, that you only need those which are located at a certain area. With this script you can select the area you are interested in (polygon) by setting a pre-defined shapefile in the script, and then you can search for its features by a column which uniquely identifies them. After that only those rasters will appear which are overlapping the features. Currently an extra feature is in the code (because it was required for the customer): the script checks if the projetion of the rasters is Hungarian Datum 1972 (EOV) or UTM, and after that it uses the proper shapefiles to work with. The script works with extents, so there might be no real intersection between the datasets, but it still reduces the number images to be rendered and viewed.


How to use it:

1. Create a toolbox (or use an existing one)
2. Add a script to the toolbox
3. Set the following parameters:
   - Mosaic Dataset (you can select multiple values)
   - Text (used for searching in the shapefile defined by the script)
4. Run the script.


Future plans:

- Filtering raster datasets located in folders
- Allow polygon selection in the tool window



Feel free to develop and use this script, also please don't forget to refer to my GitHub page :)
