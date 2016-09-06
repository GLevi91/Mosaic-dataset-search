import os, sys, arcpy
import arcpy.mapping

reload (sys)
sys.setdefaultencoding('utf-8')

inputRaster = sys.argv[1] # Select raster
landtext = sys.argv[2] # Select "land"

scriptPath = sys.path[0]
toolSharePath = os.path.dirname(scriptPath)
toolDataPath = os.path.join(toolSharePath)
landfeatureEOV = os.path.join(toolDataPath,"dummy.SHP") #EOV projection
landfeatureUTM = os.path.join(toolDataPath,"dummy_UTM.SHP") #UTM projection
arcpy.env.overwriteOutput = True


inputs = arcpy.GetParameterAsText(0) # Getting input mosaic dataset parameters as text


for row in arcpy.SearchCursor(landfeatureEOV, fields="NAME"):
   namevalue=row.getValue("NAME")
   if namevalue == landtext:
      break

query = """ "NAME" = '%s'"""%namevalue

	  
for dataset in inputs.split(';'):
   rasterdesc=arcpy.Describe(dataset)
   wkid = rasterdesc.spatialReference.factoryCode
   
   lstFields = arcpy.ListFields(dataset)
   for field in lstFields:
      if field.name == "Path":
         arcpy.DeleteField_management(dataset,"Path")
   
   if wkid == 23700:
      arcpy.MakeFeatureLayer_management(landfeatureEOV,"landfeature_lyr_EOV",query)
      arcpy.CopyFeatures_management("landfeature_lyr_EOV","C:\landlayer_EOV.SHP")
      EOV = os.path.join("C:\landlayer_EOV.SHP")
      Desc_EOV = arcpy.Describe(EOV)
      Ext = Desc_EOV.extent
   
   if wkid == 32633:
      arcpy.MakeFeatureLayer_management(landfeatureUTM,"landfeature_lyr_UTM",query)
      arcpy.CopyFeatures_management("landfeature_lyr_UTM","C:\kulhatlayer_UTM.SHP")
      UTM = os.path.join("C:\kulhatlayer_UTM.SHP")
      Desc_UTM = arcpy.Describe(UTM)
      Ext = Desc_UTM.extent

   joinfield_mosaic = "OBJECTID"
   joinfield_table = "OID"
   jointable = str(dataset)+"_Paths"
   pathfield = "Path"

   arcpy.JoinField_management(dataset,joinfield_mosaic,jointable,joinfield_table,pathfield)

   for row in arcpy.SearchCursor(dataset, fields="Path"):
      pathvalue = row.getValue("Path")
      rasterDesc = arcpy.Describe(pathvalue) # Define raster extent
      rasterExt  = rasterDesc.extent
	   
      if Ext.disjoint(rasterExt):
         pass
      else: 
         arcpy.AddMessage(str(pathvalue) + " added to the layer.")
		 
         mxd = arcpy.mapping.MapDocument("CURRENT")
         df = arcpy.mapping.ListDataFrames(mxd,"*")[0]
		 
         newlayer = arcpy.mapping.Layer(pathvalue)
         
         arcpy.mapping.AddLayer(df,newlayer,"TOP")
         arcpy.RefreshTOC()
         del mxd, df, newlayer

arcpy.RefreshActiveView()
