import os, sys, arcpy
import arcpy.mapping

reload (sys)
sys.setdefaultencoding('utf-8')

inputFolder = sys.argv[1]
inputMosaic = sys.argv[2]
inputPolygon = sys.argv[3]
inputField = sys.argv[4]
inputValue = sys.argv[5]


arcpy.env.overwriteOutput = True


inputFolderParameters = arcpy.GetParameterAsText(0)
inputMosaicParameters = arcpy.GetParameterAsText(1)


desc = arcpy.Describe(inputPolygon).shapeFieldName
query = "%s = '%s'" %(inputField, inputValue)
searchcursor = arcpy.SearchCursor(inputPolygon, query)


for folder in inputFolderParameters.split(";"):
   arcpy.env.workspace = folder
   
   for row in searchcursor:
      rowvalue = row.getValue(desc)
      polygonextent = rowvalue.extent
	  polygonprojection = polygonextent.spatialReference

      for raster in arcpy.ListRasters("*"):
         rasterdescribe = arcpy.Describe(raster)
         rasterextent = rasterdescribe.extent.projectAs(polygonprojection)
		 
         if polygonextent.disjoint(rasterextent):
            pass
         else:
            mxd = arcpy.mapping.MapDocument("CURRENT")
            df = arcpy.mapping.ListDataFrames(mxd, "*")[0]
			
            newlayer = arcpy.mapping.Layer(raster)
			
            arcpy.mapping.AddLayer(df,newlayer,"TOP")
            arcpy.RefreshTOC()
            del mxd, df, newlayer
		
arcpy.RefreshActiveView()
