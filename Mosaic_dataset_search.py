import os, sys, arcpy
import arcpy.mapping

reload (sys)
sys.setdefaultencoding('utf-8')

inputRaster = sys.argv[1] # Select raster
kulhattext = sys.argv[2] # Select "kulhat"

scriptPath = sys.path[0]
toolSharePath = os.path.dirname(scriptPath)
toolDataPath = os.path.join(toolSharePath)
kulhatfeatureEOV = os.path.join(toolDataPath,"KULTHAT.SHP")
kulhatfeatureUTM = os.path.join(toolDataPath,"KULHAT_UTM.SHP")
#arcpy.env.workspace = Balaton_raszteres_adatok.gdb" # Setting default geodatabase
arcpy.env.overwriteOutput = True


inputs = arcpy.GetParameterAsText(0) # Getting input mosaic dataset parameters as text


for row in arcpy.SearchCursor(kulhatfeatureEOV, fields="NEV"):
   nevvalue=row.getValue("NEV")
   if nevvalue == kulhattext:
      break

query = """ "NEV" = '%s'"""%nevvalue

	  
for dataset in inputs.split(';'):
   rasterdesc=arcpy.Describe(dataset)
   wkid = rasterdesc.spatialReference.factoryCode
   
   lstFields = arcpy.ListFields(dataset)
   for field in lstFields:
      if field.name == "Path":
         arcpy.DeleteField_management(dataset,"Path")
   
   if wkid == 23700:
      arcpy.MakeFeatureLayer_management(kulhatfeatureEOV,"kulhatfeature_lyr_EOV",query)
      arcpy.CopyFeatures_management("kulhatfeature_lyr_EOV","R:\Kereso_allomanyai\kulhatlayer_EOV.SHP")
      EOV = os.path.join("R:\Kereso_allomanyai\kulhatlayer_EOV.SHP")
      Desc_EOV = arcpy.Describe(EOV)
      Ext = Desc_EOV.extent
   
   if wkid == 32633:
      arcpy.MakeFeatureLayer_management(kulhatfeatureUTM,"kulhatfeature_lyr_UTM",query)
      arcpy.CopyFeatures_management("kulhatfeature_lyr_UTM","R:\Kereso_allomanyai\kulhatlayer_UTM.SHP")
      UTM = os.path.join("R:\Kereso_allomanyai\kulhatlayer_UTM.SHP")
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
         arcpy.AddMessage(str(pathvalue) + " hozzáadva a réteghez.")
		 
         mxd = arcpy.mapping.MapDocument("CURRENT")
         df = arcpy.mapping.ListDataFrames(mxd,"*")[0]
		 
         newlayer = arcpy.mapping.Layer(pathvalue)
		 
         if rasterDesc.bandCount == 3:
            alaplayer = arcpy.mapping.Layer(r"R:\Kereso_allomanyai\rgb.lyr")
            arcpy.mapping.UpdateLayer(df,newlayer,alaplayer,True)
            del alaplayer
         arcpy.mapping.AddLayer(df,newlayer,"TOP")
         arcpy.RefreshTOC()
         del mxd, df, newlayer

arcpy.RefreshActiveView()