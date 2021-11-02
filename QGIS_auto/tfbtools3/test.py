

import os
import xml
import xml.dom.minidom as xmini
import json

from PIL import Image
from PIL import ExifTags
from PIL.ExifTags import TAGS, GPSTAGS
import piexif

import exifread
import re
import requests

import time;
import random;
from datetime import datetime,timedelta
import numpy as np

from math import sin, cos, sqrt, atan2, radians
from dateutil.parser import parse

import getpass
import urllib.request
import sys 
import base64
import csv
from os import walk



import xml.etree.ElementTree

# import pyexiv2 as ev


# # 資料
# my_data = {'WS_ID': 'pythontest', 'RE_ID': 'pythontest456'}

# # 將資料加入 POST 請求中
# r = requests.post('http://140.134.48.75/QGIS_vote/api/QGISvote_WebAPI/DW_INSERTT', data = my_data)

# class Math:
#     #求极差
#     @staticmethod
#     def range(l):
#         return max(l)-min(l);
#     #求平均数
#     @staticmethod
#     def avg(l):
#         return float(sum(l))/len(l);
#     #求中位数
#     @staticmethod
#     def median(l):
#         l=sorted(l);#先排序
#         if len(l)%2==1:
#             return l[len(l)/2];
#         else:
#             return (l[len(l)/2-1]+l[len(l)/2])/2.0;
#     #求众数
#     @staticmethod
#     def mode(l):
#         #统计list中各个数值出现的次数
#         count_dict={};
#         for i in l:
#             if count_dict.has_key(i):
#                 count_dict[i]+=1;
#             else:
#                 count_dict[i]=1;
#         #求出现次数的最大值
#         max_appear=0
#         for v in count_dict.values():
#             if v>max_appear:
#                 max_appear=v;
#         if max_appear==1:
#             return;
#         mode_list=[];
#         for k,v in count_dict.items():
#             if v==max_appear:
#                 mode_list.append(k);
#         return mode_list;
#     #求方差
#     @staticmethod
#     def variance(l):#平方的期望-期望的平方
#         s1=0;
#         s2=0;
#         for i in l:
#             s1+=i**2;
#             s2+=i;
#         return float(s1)/len(l)-(float(s2)/len(l))**2;
    
#     #求方差2
#     @staticmethod    
#     def variance2(l):#平方-期望的平方的期望
#         ex=float(sum(l))/len(l);
#         s=0;
#         for i in l:
#             s+=(i-ex)**2;
#         return float(s)/len(l);    


# #主函数，测试
# arr=[1,2,3,2,3,1,4];
# print("极差为：{0}".format(Math.range(arr)))
# print("平均数为：{0:.2f}".format(Math.avg(arr)));
# # print("中位数为：{0}".format(Math.median(arr)));
# # print( "众数为：{0}".format(Math.mode(arr)));
# # print( "方差为：{0:.2f}".format(Math.variance(arr)));
# # print( "方差为：{0:.2f}".format(Math.variance2(arr)));


# #計算GPX檔點到點的距離
# def main(point_1_lat, point_1_lon, point_2_lat, point_2_lon, unit='m'):
#     # approximate radius of earth in km
#     R = 6373.0

#     lat1 = radians(float(point_1_lat))
#     lon1 = radians(float(point_1_lon))
#     lat2 = radians(float(point_2_lat))
#     lon2 = radians(float(point_2_lon))

#     dlon = lon2 - lon1
#     dlat = lat2 - lat1

#     a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
#     c = 2 * atan2(sqrt(a), sqrt(1 - a))

#     distance = R * c * 1000
#    #  print("Distance: " + str(distance) + "m")
# #計算GPX檔點到點的距離


# #擷取GPX檔XML轉為json
# dom = xmini.parse(r"C:\Users\vincentlu\Desktop\QGIS3上課用教學資料+外掛程式\測試用資料\GPX檔\gpx_test01.gpx")

# testlist=[]


# for i in dom.getElementsByTagName("trkpt"):            
#     _getL=i.getAttribute("lat")
#     _getLo=i.getAttribute("lon")
#     _getEle=i.getElementsByTagName("ele").item(0).childNodes.item(0).nodeValue
#     _gett=i.getElementsByTagName("time").item(0).childNodes.item(0).nodeValue    
#     # print("Lat={0} | Lon={1} | elev.={2} | time={3}".format(_getL,_getLo,_getEle,_gett) )
#     # testlist.append("Lat={0} | Lon={1} | elev.={2} | time={3}".format(_getL,_getLo,_getEle,_gett))
#     # Lat.append(_getL)
#     # Lon.append(_getLo)
#     # elev.append(_getEle)
#     testlist.append({"Lat":_getL,"Lon":_getLo,"elev":_getEle,"time":_gett,"rate":0,"type":0})    
    

#print(testlist)

#print((testlist[3]["time"]-testlist[0]["time"]).total_seconds())  計算時間差


############


# testtime = []

# for x in range(0,len(testlist)):   
#    #date = datetime.strptime(testlist[x]["time"], '%Y-%m-%dT%H:%M:%S%fZ')
#    #timeStamp = int(time.mktime(date))   
#    testtime = datetime.strptime(testlist[x]["time"], '%Y-%m-%dT%H:%M:%S%fZ')
#    testlist[x]["time"] = testtime

# print(testtime)
# print(testlist[0])

# ########匯入照片EXIF 測試OK
# imgPath = r"D:\Vincent\99_Temp\QGIS_Temp\QGIStest\NoEXIF\20190507_115500.jpg"
# img = Image.open(imgPath)
# exif = img._getexif()
# #print(exif)
# tags = {}
# for tag, value in exif.items():
#     decoded = ExifTags.TAGS.get(tag, tag) #exif.items()傳回的tag只是編號, 利用ExifTags.TAGS.get()來取得tag名稱
#     tags[decoded] = value
#     #print("%s -> %s" % (decoded, value))


# print(tags)
# name = os.path.basename(imgPath)
# print(name)
# geoPhotos = []

# geo_info = {"type": "Feature",
#                             "properties": {'ID': 'test01', 'Name': name, 'Date': testlist[0]['time'], 'Time': testlist[0]['time'],
#                                            'Lon': testlist[0]['Lon'],
#                                            'Lat': testlist[0]['Lat'], 'Altitude': 'altitude', 'North': 'north',
#                                            'Azimuth': 'azimuth',
#                                            'Camera Maker': 'str(maker)', 'Camera Model': 'str(model)', 'Title': 'str(title)',
#                                            'Comment': 'user_comm','Path': imgPath, 'RelPath': 'RelPath',
#                                            'Timestamp': 'timestamp'},
#                             "geometry": {"coordinates": [testlist[0]['Lon'], testlist[0]['Lat']], "type": "Point"}}
# geoPhotos.append(geo_info)



# print(geoPhotos)

#print((testtime[t-1]-testtime[0]).total_seconds())


#print((testtime[t-1]-testtime[0]).total_seconds()/60/60)


# timeee=[]
# for x in range(0,len(testtime)):
#    if x + 1 < len(testlist):
#       timeee.append(((testtime[x+1]-testtime[x]).total_seconds()))
#    else:
#       break

#print(len(timeee))



#print(datetime.strptime(testlist[0]["time"], '%Y-%m-%dT%H:%M:%S%fZ'))
    
#testjson = json.dumps(testlist)
#testjson2 = json.loads(testjson)

# x = 0
# y = 1
# z = []

# while x <= len(testlist):
# #for x in range(len(testlist)):
#    main(testlist[x]["Lat"],testlist[x]["Lon"],testlist[y]["Lat"],testlist[y]["Lon"])
#    x = x+1
#    y = y+1
   


   # approximate radius of earth in km

# #計算GPX座標距離總和
# testdata = []

# for x in range(0,len(testlist)):
   
#    if x + 1 < len(testlist):     

#       R = 6373.0
#       lat1 = radians(float(testlist[x]["Lat"]))
#       lon1 = radians(float(testlist[x]["Lon"]))
#       lat2 = radians(float(testlist[x + 1]["Lat"]))
#       lon2 = radians(float(testlist[x + 1]["Lon"]))      

#       dlon = lon2 - lon1
#       dlat = lat2 - lat1

#       a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
#       c = 2 * atan2(sqrt(a), sqrt(1 - a))

#       distance = R * c *1000
#     #   print("Distance: " + str(distance) + "m")   

#       testdata.append(round(distance,5))
#    else:
#       break
# testdata2 = sum(testdata)
   
# print(testdata2)


# #時間格式轉換與計算點位時間差
# timelist = []
# for x in range(0,len(testlist)): 
#     timelist.append(datetime.strptime(testlist[x]["time"], '%Y-%m-%dT%H:%M:%S%fZ'))

# timelag=[]
# for x in range(0,len(timelist)):
#     if x + 1 < len(timelist):
#         timelag.append((timelist[x+1]-timelist[x]).total_seconds())
#     else:
#         break

# sum_timelag = sum(timelag)

# # print(timelist)
# print(sum_timelag)

      
# ##############

# #print(timeee)

# np.seterr(divide='ignore', invalid='ignore')

# # 計算array相除
# nslist = np.divide(np.array(testdata),np.array(timelag))
# print(nslist)
# test3 = nslist*60/1000*60

# ratelistStd = np.std(test3)

# print(ratelistStd)

# for x in range(0,len(test3)):
#     if test3[x] != 0 :
#         testlist[x]["rate"] = test3[x]
#     else:
#         testlist[x]["rate"] = 0





# out_timeee = [x for x in timeee if x > 1]
#print(out_timeee)

# print(np.mean(np.array(timeee)))

# print(np.mean(np.array(testdata)))

# print(sum(testdata)/sum(timeee))


# anslist.dtype = np.int_

    
# for x in range(0,len(anslist)):
#    if anslist[x] != 0 :
#       testlist[x]["rate"] = anslist[x]
#    else:
#       testlist[x]["rate"] = 0

# testout = []
# #out_testlist = [x for x in testlist[x]["rate"] if x > 1]

# for x in range(0,len(testlist)):
#    if testlist[x]["rate"] > 1 :
#       testout.append(testlist[x])
#    else:
#       break

# print(testout)

# print(out_testlist)


# ##資料匯出產生XML文件
# def creatXML(testlist):
#    #在内存中创建一个空的文档
#    doc = xmini.Document() 
#    #创建一个根节点Managers对象
#    root = doc.createElement('gpx') 
#    #设置根节点的属性
#    root.setAttribute('creator', 'FCU_GIS') 
#    root.setAttribute('version', '1.0') 
#    #将根节点添加到文档对象中
#    doc.appendChild(root) 

#    # managerList = [{'name' : 'joy',  'age' : 27, 'sex' : '女'},
#    #                {'name' : 'tom', 'age' : 30, 'sex' : '男'},
#    #                {'name' : 'ruby', 'age' : 29, 'sex' : '女'}
#    # ]
#    nodeTrk = doc.createElement('trk')
#    nodeName = doc.createElement('name')
#    nodeName.appendChild(doc.createTextNode('test123'))
#    nodetrkseg = doc.createElement('trkseg')
#    for i in range(0,len(testlist)) :
#       nodetrkpt = doc.createElement('trkpt')
#       nodetrkpt.setAttribute('lat',testlist[i]["Lat"])
#       nodetrkpt.setAttribute('lon',testlist[i]["Lon"])
#       nodeEle = doc.createElement('ele')
#       #给叶子节点name设置一个文本节点，用于显示文本内容
#       nodeEle.appendChild(doc.createTextNode(testlist[i]["elev"]))

#       nodeTime = doc.createElement("time")
#       nodeTime.appendChild(doc.createTextNode(str(testlist[i]["time"])))
     

#       #将各叶子节点添加到父节点Manager中，
#       #最后将Manager添加到根节点Managers中
#       nodetrkpt.appendChild(nodeEle)
#       nodetrkpt.appendChild(nodeTime)
#       nodetrkseg.appendChild(nodetrkpt)      
      
   
   
#    nodeTrk.appendChild(nodeName)
#    nodeTrk.appendChild(nodetrkseg)
#    root.appendChild(nodeTrk)

   
#    #开始写xml文档
#    fp = open(r'C:\Users\vincentlu\Desktop\QGIStest\GPX\test123.gpx', 'w')
#    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")

# # #######################################  



# # out_testdata = [x for x in testdata if x > 4]
# #print(out_testdata)
# #print(anslist)
# # output_dict = [x for x in anslist if x < 4]

# # print(len(output_dict))

# # print(np.around(anslist,decimals=1))
# # print(np.mean(np.array(anslist)))
# # anslist.dtype = np.int_

# # print(anslist)

# # print(testlist[0])

# # print(testlist[0]["time"])





# ###array查詢功能測試OK        
# # output_dict = [x for x in testlist if x['Lon'] == '121.589092']
# #####################





# # Transform python object back into json
# #output_json = json.dumps(output_dict)

# # Show json
# #print(output_json)



# f = open(r"D:\Vincent\99_Temp\QGIS_Temp\QGIStest\NoEXIF\20190507_115500.jpg", 'rb')

# # Return Exif tags
# tags2 = exifread.process_file(f) #process_file(f, stop_tag='UNDEF', details=True, strict=False, debug=False)
#     #    Process an image file (expects an open file object).
        
#     #    This is the function that has to deal with all the arbitrary nasty bits
#     #    of the EXIF standard.

# # for tag in tags2.keys():
# #     if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
# #         print ("Key: %s, value %s" % (tag, tags2[tag]))
# print(tags2['Image DateTime'])
# phototime2 = datetime.strptime(str(tags2['Image DateTime']),'%Y:%m:%d %H:%M:%S')

# print(phototime2)

# img = Image.open(r"D:\Vincent\99_Temp\QGIS_Temp\QGIStest\NoEXIF\20190507_115500.jpg") 
# exif_dict = piexif.load(img.info['exif']) 

# altitude = exif_dict['GPS'][piexif.GPSIFD.GPSLatitude] 
# #print(altitude)

# ###########################
# phototime = datetime.strptime(tags["DateTimeDigitized"],'%Y:%m:%d %H:%M:%S')
# timedelta(days=2,hours=2,minutes=0,seconds=0)
# print(phototime)
# print(phototime-timedelta(days=2,hours=2,minutes=0,seconds=0))
# test123=[]
# test456 = []


# def latitude_and_longitude_convert_to_decimal_system(*arg):
#     """
#     經緯度轉為小數, param arg:
#     :return: 十進位制小數
#     """
#     return float(arg[0]) + ((float(arg[1]) + (float(arg[2].split('/')[0]) / float(arg[2].split('/')[-1]) / 60)) / 60)



# def find_GPS_image(pic_path):
#     GPS = {}
#     date = ''
#     with open(pic_path, 'rb') as f:
#         tags = exifread.process_file(f)
#         for tag, value in tags.items():
#             if re.match('GPS GPSLatitudeRef', tag):
#                 GPS['GPSLatitudeRef'] = str(value)
#             elif re.match('GPS GPSLongitudeRef', tag):
#                 GPS['GPSLongitudeRef'] = str(value)
#             elif re.match('GPS GPSAltitudeRef', tag):
#                 GPS['GPSAltitudeRef'] = str(value)
#             elif re.match('GPS GPSLatitude', tag):
#                 try:
#                     match_result = re.match('\[(\w*),(\w*),(\w.*)/(\w.*)\]', str(value)).groups()
#                     GPS['GPSLatitude'] = int(match_result[0]), int(match_result[1]), int(match_result[2])
#                 except:
#                     deg, min, sec = [x.replace(' ', '') for x in str(value)[1:-1].split(',')]
#                     GPS['GPSLatitude'] = latitude_and_longitude_convert_to_decimal_system(deg, min, sec)
#             elif re.match('GPS GPSLongitude', tag):
#                 try:
#                     match_result = re.match('\[(\w*),(\w*),(\w.*)/(\w.*)\]', str(value)).groups()
#                     GPS['GPSLongitude'] = int(match_result[0]), int(match_result[1]), int(match_result[2])
#                 except:
#                     deg, min, sec = [x.replace(' ', '') for x in str(value)[1:-1].split(',')]
#                     GPS['GPSLongitude'] = latitude_and_longitude_convert_to_decimal_system(deg, min, sec)
#             elif re.match('GPS GPSAltitude', tag):
#                 GPS['GPSAltitude'] = str(value)
#             elif re.match('.*Date.*', tag):
#                 date = str(value)
#     return {'GPS_information': GPS, 'date_information': date}



# print(find_GPS_image(r"D:\Vincent\99_Temp\QGIS_Temp\QGIStest\NoEXIF\20190507_115500.jpg"))



# def to_deg(value, loc):
#     """convert decimal coordinates into degrees, munutes and seconds tuple
       
#     Keyword arguments: value is float gps-value, loc is direction list ["S", "N"] or ["W", "E"]
#     return: tuple like (25, 13, 48.343 ,'N')
#     """
#     if value < 0:
#         loc_value = loc[0]
#     elif value > 0:
#         loc_value = loc[1]
#     else:
#         loc_value = ""
#     abs_value = abs(value)
#     deg =  int(abs_value)
#     t1 = (abs_value-deg)*60
#     min = int(t1)
#     sec = round((t1 - min)* 60, 5)
#     return (deg, min, sec, loc_value)    


# def set_gps_location(file_name, lat, lng):
#     """Adds GPS position as EXIF metadata

#     Keyword arguments:
#     file_name -- image file 
#     lat -- latitude (as float)
#     lng -- longitude (as float)

#     """
#     lat_deg = to_deg(lat, ["S", "N"])
#     lng_deg = to_deg(lng, ["W", "E"])

#     print(lat_deg)
#     print(lng_deg)

#     # class pyexiv2.utils.Rational(numerator, denominator) => convert decimal coordinates into degrees, munutes and seconds
#     exiv_lat = (ev.Rational(lat_deg[0]*60+lat_deg[1],60),ev.Rational(lat_deg[2]*100,6000), ev.Rational(0, 1))
#     exiv_lng = (ev.Rational(lng_deg[0]*60+lng_deg[1],60),ev.Rational(lng_deg[2]*100,6000), ev.Rational(0, 1))

#     exiv_image = ev.ImageMetadata(file_name)
#     exiv_image.read()

#     # modify GPSInfo of image
#     exiv_image["Exif.GPSInfo.GPSLatitude"] = exiv_lat
#     exiv_image["Exif.GPSInfo.GPSLatitudeRef"] = lat_deg[3]
#     exiv_image["Exif.GPSInfo.GPSLongitude"] = exiv_lng
#     exiv_image["Exif.GPSInfo.GPSLongitudeRef"] = lng_deg[3]
#     exiv_image["Exif.Image.GPSTag"] = 654
#     exiv_image["Exif.GPSInfo.GPSMapDatum"] = "WGS-84"
#     exiv_image["Exif.GPSInfo.GPSVersionID"] = '2 2 0 0'

#     exiv_image.write()



# for x in range(0,len(testlist)):
#    testX = phototime - testlist[x]["time"]
#    testlist[x]["rate"] = testX
#    test123.append(testX)
   
# for x in range(0,len(testlist)):
#    if testlist[x]["rate"] == min(test123):
#       # print(testlist[x])
#       test456.append(testlist[x])


# print(test456)
# creatXML(test456)
# print(min(test123))



# Open image file for reading (binary mode) 
# f = open(r"D:\Vincent\99_Temp\QGIS_Temp\QGIStest\NoEXIF\20190507_115500.jpg", 'rb')
# # Return Exif tags
# tags2 = exifread.process_file(f)
# print(tags2)

# img = Image.open(r"D:\Vincent\99_Temp\QGIS_Temp\QGIStest\NoEXIF\20190507_115500.jpg")
# print(img) #傳回印出該檔案的基本資料，如模式，大小，記憶體所在位置
# info = img._getexif()
# exifdata={}
# for tag, value in info.items():
# 	key = TAGS.get(tag, tag)
# 	print(key + " "+ str(value))
#     exifdata[key] = value

# print(exifdata)

#    import xml.dom.minidom as xdom

#     gpxPath = 'test.gpx'
#     dom_tree = xdom.parse(gpxPath)
#     collection = dom_tree.documentElement
#     trkpts = collection.getElementsByTagName("trkpt")
#     lats, lons = [], []

#     for trkpt in trkpts:
#         lat = trkpt.getAttribute("lat")
#         lon = trkpt.getAttribute("lon")
#         if lat=='0' or lon=='0':
#             continue
#         lats.append(float(lat))
#         lons.append(float(lon))

#     datas = {'lat': lats, 'lon': lons}
# http://gis.forest.gov.tw/arcgis/services/WMS/FHWMS/MapServer/WMSServer?request=GetCapabilities&service=WMS
# https://ecollect.forest.gov.tw/EcologicalOdata/odata/data
url = "https://ecollect.forest.gov.tw/EcologicalOdata/odata/data?$filter=county eq '臺東縣'"
# request = urllib.request.Request(url)

# response = urllib.request.urlopen(url)
# # html = response.read()        
# xmlDoc = xmini.parse(response)
# root = xmlDoc.documentElement
# # layerList =  root.getElementsByTagName('Layer')
# # j = json.loads(html)
# print(root)


# root = xml.etree.ElementTree.parse(response)
# print(root)
# wmtsTitleList = []
# wmtsIdentifierList = []
# wmtsFormatList = []


# for layer in layerList:
    
#     owsTitleList = layer.getElementsByTagName('Title')
#     owsIdentifier = layer.getElementsByTagName('Name')
#     imgformatList = layer.getElementsByTagName('Format')

#     wmtsTitleList.append(owsTitleList[0].childNodes[0].data)
#     wmtsIdentifierList.append(owsIdentifier[0].childNodes[0].data)
#     wmtsFormatList.append(imgformatList[0].childNodes[0].data)
   

# print(wmtsIdentifierList,wmtsTitleList,wmtsFormatList)

# r = requests.get(url)
# testjson = []
# testjson = json.loads(r.text)
# print(testjson['value'][0])


# response=urllib.request.urlopen('https://ictjournal.itri.org.tw/Content/Messagess/contents.aspx?MmmID=654304432070702333&MSID=1002354337501512631')
# html=response.read()
# print(str(html))


# 指定要列出所有檔案的目錄

# mypath = "D:\Vincent\99_Temp\QGIS_Temp\P"

# # 遞迴列出所有子目錄與檔案
# for root, dirs, files in walk(mypath):
# #   print("路徑：", root)
# #   print("  目錄：", dirs)
#   print("  檔案：", files)



# import socket
# import uuid

# # 獲取主機名
# hostname = socket.gethostname()
# #獲取IP
# ip = socket.gethostbyname(hostname)
# # 獲取Mac地址
# def get_mac_address():
#     mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
#     return ":".join([mac[e:e+2] for e in range(0,11,2)])

# # ipList = socket.gethostbyname_ex(hostname)
# # print(ipList)
# print("主機名：",hostname)
# print("IP：",ip)
# print("Mac地址：",get_mac_address())


