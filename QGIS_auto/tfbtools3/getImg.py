# -*- coding: utf-8 -*-

"""
/***************************************************************************
 TFB-Tool
                                 A QGIS plugin
 Initializer of the plugin.
                             -------------------
        begin                : 2017-11-30
        author               : kuma
        email                : kumahl@gmail.com
 ***************************************************************************/
/***************************************************************************
 *       
 *   This plugin is free softwart,                                                                   *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 3 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qgis.core import *
from qgis.gui import *
import urllib.request
import qgis.utils
import io
import os
import os.path
import sys 
import csv
import glob
from osgeo import ogr
from osgeo import osr, gdal
# from gdalconst import *
import getpass



#global var
global rootPath
# rootPath = 'C:/Users/' + getpass.getuser() + '/.qgis2/python/plugins/TFB-Tools/'
# rootPath = 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\QGIS\\QGIS3\\profiles\\default\\python\\plugins\\TFB-Tools3\\'
rootPath = os.path.dirname(__file__)+'\\'



class getImgFromFrame: 

  def __init__(self, iface):
    # save reference to the QGIS interface
    self.iface = iface
    self.canvas = iface.mapCanvas()    


  def load_25000_img(self, defaultPath):
    
    #######################################################
    #                                                     #
    # Read file path & get 1/25000 frame file name        #
    # if exist, load it and put it on top                 #
    #                                                     #
    # filePathList[12][2]: 1_25000圖幅接合圖0882.shp      #
    #                                                     #
    #######################################################

    filePath = rootPath + 'filePath.csv'
    filePathfile = open(filePath, 'r')
    csvCursor = csv.reader(filePathfile)

    global filePathList
    filePathList = []
    for row in csvCursor:
      filePathList.append(row)

    global defaultDir
    defaultDir = defaultPath
    global filePathName
    filePathName = defaultDir + filePathList[12][2]
    global styleFilePath    
    styleFilePath = rootPath + 'style/noFillRedLine.qml'

    if os.path.isfile(filePathName) :     
      if len(QgsProject.instance().mapLayersByName(filePathList[12][1])) == 0:
        i=0
        self.iface.addVectorLayer(filePathName, "", "ogr")
        self.iface.activeLayer().loadNamedStyle(styleFilePath)


      #######################################################
      #                                                     #
      # setMapTool: click to get layer attribute            #
      #                                                     #
      #######################################################
    
      self.pointEmitter = QgsMapToolEmitPoint(self.iface.mapCanvas())
      # QObject.connect( self.pointEmitter, SIGNAL("canvasClicked(const QgsPoint, Qt::MouseButton)"), self.clickNow)
      self.pointEmitter.canvasClicked.connect(self.clickNow)
      self.iface.mapCanvas().setMapTool( self.pointEmitter ) 
      #mouseIconPath = rootPath + 'icon/25000.png'
      #QgsApplication.instance().setOverrideCursor(QCursor(QPixmap(mouseIconPath)))
      # QtCore.QObject.connect(self.actionChangeFeedbackController, QtCore.SIGNAL("triggered()"), self.changeFeedbackController)
      # self.actionChangeFeedbackController.triggered.connect(self.changeFeedbackController)

    else:
      msg = "找不到\" " + filePathName + " \"圖層" + "\n請確認路徑" 
      QMessageBox.information(self.iface.mainWindow(), "錯誤", msg)       


  
  def clickNow(self, event):

    #######################################################
    #                                                     #
    # 1. let 1/25000 lyr be active layer                  #
    # 2. get the X, Y when mouse click                    #
    # 3. select the feature mouse click                   #
    # 4. add raster img                                   #
    # 5. change the layer order(frame lyr always on top)  #
    #                                                     #
    #######################################################

    #1#
    layers = self.canvas.layers()  
    for each_layer in layers:
      if each_layer.source() == filePathName:        
        parish_layer = each_layer
        break

    #2#
    rect = QgsRectangle(event.x() - 0.000001,
                      event.y() - 0.000001,
                      event.x() + 0.000001,
                      event.y() + 0.000001)
    # rect = self.iface.mapCanvas().mapRenderer().mapToLayerCoordinates(parish_layer, rect)
    rect = self.iface.mapCanvas().mapSettings().mapToLayerCoordinates(parish_layer, rect)    
    #3#
    parish_layer.selectByRect(rect)
    selected_features = parish_layer.selectedFeatures()    

    if (selected_features != []):
      selected_features_item = selected_features[0]
      rasterfilePathName = defaultDir + filePathList[13][2]
      rasterName = rasterfilePathName + selected_features_item["FileNAME"] + ".jpg"

    #4#
      if os.path.isfile(rasterName) : 
        fileInfo = QFileInfo(rasterName)
        baseName = fileInfo.baseName()
        rlayer = QgsRasterLayer(rasterName, baseName)
        rlayer.setCrs( QgsCoordinateReferenceSystem(3826, QgsCoordinateReferenceSystem.EpsgCrsId) )
        self.iface.setActiveLayer(parish_layer)
        QgsProject.instance().addMapLayer(rlayer)  
  
    #5#
        root = QgsProject.instance().layerTreeRoot()

        myalayer = root.findLayer(parish_layer.id())
        myClone = myalayer.clone()
        parent = myalayer.parent()
        parent.insertChildNode(0, myClone)
        parent.removeChildNode(myalayer)     
        #self.iface.legendInterface().moveLayer(parish_layer, 0)
        #self.canvas.refresh()

      else:
        msg = "找不到\" " + rasterName + "\n請確認路徑" + "\""
        QMessageBox.information(self.iface.mainWindow(), "錯誤", msg)

    
  def load_5000_img(self, defaultPath):
    
    #######################################################
    #                                                     #
    # Read file path & get 1/5000 frame file name        #
    # if exist, load it and put it on top                 #
    #                                                     #
    # filePathList[11][2]: 1_5000圖幅接合圖0931.shp      #
    #                                                     #
    #######################################################

    filePath = rootPath + 'filePath.csv'
    filePathfile = open(filePath, 'r')
    csvCursor = csv.reader(filePathfile)

    global filePathList_5000
    filePathList_5000 = []
    for row in csvCursor:
      filePathList_5000.append(row)

    global defaultDir_5000
    defaultDir_5000 = defaultPath
    global filePathName_5000
    filePathName_5000 = defaultDir_5000 + filePathList_5000[11][2]
    global styleFilePath_5000    
    styleFilePath_5000 = rootPath + 'style/noFillBlueLine.qml'

    if os.path.isfile(filePathName_5000) :     
      if len(QgsProject.instance().mapLayersByName(filePathList_5000[11][1])) == 0:
        i=0
        self.iface.addVectorLayer(filePathName_5000, "", "ogr")
        self.iface.activeLayer().loadNamedStyle(styleFilePath_5000)

 



      #######################################################
      #                                                     #
      # setMapTool: click to get layer attribute            #
      #                                                     #
      #######################################################
    
      self.pointEmitter = QgsMapToolEmitPoint(self.iface.mapCanvas())
      # QObject.connect( self.pointEmitter, SIGNAL("canvasClicked(const QgsPoint, Qt::MouseButton)"), self.clickNow_2)
      self.pointEmitter.canvasClicked.connect(self.clickNow_2)
      self.iface.mapCanvas().setMapTool( self.pointEmitter ) 
      #mouseIconPath = rootPath + 'icon/25000.png'
      #QgsApplication.instance().setOverrideCursor(QCursor(QPixmap(mouseIconPath)))      

    else:
      msg = "找不到\" " + filePathName_5000 + " \"圖層" + "\n請確認路徑" 
      QMessageBox.information(self.iface.mainWindow(), "錯誤", msg)  
    
    # self.iface.activeLayer().removeSelection()
  
  def clickNow_2(self, event):

    #######################################################
    #                                                     #
    # 1. let 1/5000 lyr be active layer                   #
    # 2. get the X, Y when mouse click                    #
    # 3. select the feature mouse click                   #
    # 4. add raster img                                   #
    # 5. change the layer order(frame lyr always on top)  #
    #                                                     #
    #######################################################

    #1#
    layers = self.canvas.layers()  
    for each_layer in layers:
      if each_layer.source() == filePathName_5000:        
        parish_layer = each_layer
        break

    #2#
    rect = QgsRectangle(event.x() - 0.000001,
                      event.y() - 0.000001,
                      event.x() + 0.000001,
                      event.y() + 0.000001)
    rect = self.iface.mapCanvas().mapSettings().mapToLayerCoordinates(parish_layer, rect)
    
    #3#
    parish_layer.selectByRect(rect)
    selected_features = parish_layer.selectedFeatures()

    if (selected_features != []):
      selected_features_item = selected_features[0]
      rasterfilePathName = defaultDir_5000 + filePathList_5000[14][2]

      if str(selected_features_item["ID5000"])[0]+str(selected_features_item["ID5000"])[1] == '92':
        detailDir = '92xxxxx'
      elif str(selected_features_item["ID5000"])[0]+str(selected_features_item["ID5000"])[1] == '93':
        detailDir = '93xxxxx'
      elif str(selected_features_item["ID5000"])[0]+str(selected_features_item["ID5000"])[1] == '94':
        detailDir = '94xxxxx'
      elif str(selected_features_item["ID5000"])[0]+str(selected_features_item["ID5000"])[1]+str(selected_features_item["ID5000"])[2] == '951':
        detailDir = '951xxxxx'        
      elif str(selected_features_item["ID5000"])[0]+str(selected_features_item["ID5000"])[1]+str(selected_features_item["ID5000"])[2] == '952':
        detailDir = '952xxxxx'                
      elif str(selected_features_item["ID5000"])[0]+str(selected_features_item["ID5000"])[1]+str(selected_features_item["ID5000"])[2] == '961':
        detailDir = '961xxxxx'        
      elif str(selected_features_item["ID5000"])[0]+str(selected_features_item["ID5000"])[1]+str(selected_features_item["ID5000"])[2] == '962':
        detailDir = '962xxxxx'                        
      elif str(selected_features_item["ID5000"])[0]+str(selected_features_item["ID5000"])[1] == '97':
        detailDir = '97xxxxx'        

      rasterName = rasterfilePathName + detailDir + "\\" + str(selected_features_item["ID5000"]) + "*.jpg"
      fullrasterName = glob.glob(rasterName)      

      #QMessageBox.information(self.iface.mainWindow(), "rasterName".decode('utf-8'), fullrasterName[0]) 

    #4#
      if fullrasterName!=[]:
        if os.path.isfile(fullrasterName[0]) : 
          fileInfo = QFileInfo(fullrasterName[0])
          baseName = fileInfo.baseName()
          rlayer = QgsRasterLayer(fullrasterName[0], baseName)
          rlayer.setCrs( QgsCoordinateReferenceSystem(3826, QgsCoordinateReferenceSystem.EpsgCrsId) )
          self.iface.setActiveLayer(parish_layer)
          QgsProject.instance().addMapLayer(rlayer)  

    #5#
          root = QgsProject.instance().layerTreeRoot()

          myalayer = root.findLayer(parish_layer.id())
          myClone = myalayer.clone()
          parent = myalayer.parent()
          parent.insertChildNode(0, myClone)
          parent.removeChildNode(myalayer)     
          #self.iface.legendInterface().moveLayer(parish_layer, 0)
          #self.canvas.refresh()

        else:
          msg = "找不到\" " + rasterName + "\n請確認路徑" + "\""
          QMessageBox.information(self.iface.mainWindow(), "錯誤", msg)

      else:
          msg = "找不到\" " + rasterName + "\n請確認路徑" + "\""
          QMessageBox.information(self.iface.mainWindow(), "錯誤", msg)        

#######################################################
#                                                     #
# overload  PointTool                                 #
#                                                     #
# when mouse release: return current X, Y             #
#                                                     #
#######################################################

class PointTool(QgsMapTool):   
    def __init__(self, canvas):
      QgsMapTool.__init__(self, canvas)
      self.canvas = canvas    

    def canvasPressEvent(self, event):
      pass

    def canvasMoveEvent(self, event):
      pass

    def canvasReleaseEvent(self, event):
      x = event.pos().x()
      y = event.pos().y()
      point = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
        
    def activate(self):
      pass

    def deactivate(self):
      pass

    def isZoomTool(self):
      return False

    def isTransient(self):
      return False

    def isEditTool(self):
      return True


