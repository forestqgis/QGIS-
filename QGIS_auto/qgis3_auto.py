import os
import sys
import configparser
import shutil
import getpass

    
rootPath = 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\QGIS\\QGIS3\\profiles\\default\\'
    

#生成資源文件目錄訪問路徑
def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# 安裝外掛程式
def copyTFB_Tools3():

    global TFBTools3msg  

    # 複製外掛程式到QGIS3安裝資料夾
    try:
        #訪問tfbtools3文件夾
        filename = resource_path(os.path.dirname("tfbtools3"))   

        # pluginsPath = os.path.dirname(__file__)+'\\test'
        pluginsPath = filename + '\\tfbtools3'
        installPath = rootPath + 'python\\plugins\\TFB-Tools3'
    
        shutil.copytree(pluginsPath,installPath)
        print("Success: 安裝TFB-Tools3外掛工具成功!!")         
        TFBTools3msg = True
    except:
        print("Error: 安裝TFB-Tools3外掛工具失敗!!")         
        TFBTools3msg = False
        pass

# 設定QGIS3
def editQGIS3ini():
    try:
        config = configparser.ConfigParser()
        configPath = rootPath + 'QGIS\\QGIS3.ini'
        config.read(configPath)
        configList = config.sections()       

        

        # 設定操作語言
        config.set("locale","userLocale","zh-Hant")
        config.set("locale","overrideFlag","true")
        config.set("locale","globalLocale","zh_TW")
        config.set("locale","showGroupSeparator","false")
        print("Success: 設定 '中文操作語言' 成功!!")

        # 設定忽略Shape檔案編碼的宣告
        config.set("qgis","ignoreShapeEncoding","false")
        print("Success: 設定 '取消勾選 忽略Shape檔案編碼的宣告' 成功!!")

        ## 設定座標系統
        if ('Projections' in configList):
            config.set("Projections","defaultBehavior","useGlobal")
            config.set("Projections","layerDefaultCrs","EPSG:3826")
            config.set("Projections","projectDefaultCrs","EPSG:3826")
            config.set("Projections","showDatumTransformDialog","false")
            print("Success: 設定 '預設座標系統' 成功!!")
        else:
            config.add_section("Projections")
            config.set("Projections","defaultBehavior","useGlobal")
            config.set("Projections","layerDefaultCrs","EPSG:3826")
            config.set("Projections","projectDefaultCrs","EPSG:3826")
            config.set("Projections","showDatumTransformDialog","false")
            print("Success: 設定 '預設座標系統' 成功!!")

        ## 設定proxy
        if ('proxy' in configList): 
            config.set("proxy","proxyEnabled","true")
            config.set("proxy","proxyType","DefaultProxy")
            print("Success: 設定 '勾選proxy' 成功!!")
        else:            
            config.add_section("proxy")
            config.set("proxy","proxyEnabled","true")
            config.set("proxy","proxyType","DefaultProxy")
            print("Success: 設定 '勾選proxy' 成功!!")

        # 新增設定外掛程式主機
        config.set("app",r"plugin_installer\checkOnStart","true")
        config.set("app", r"plugin_repositories\TFB-Tools3Url\url", "http://qgis.forest/plugins.xml")
        config.set("app", r"plugin_repositories\TFB-Tools3Url\authcfg", "")
        config.set("app", r"plugin_repositories\TFB-Tools3Url\enabled", "true")
        print("Success: 設定 '新增外掛程式主機http://qgis.forest/plugins.xml' 成功!!")

        # 設定外掛程式
        if TFBTools3msg == True :            
            config.set("PythonPlugins","TFB-Tools3","true") 
            print("Success: 設定 '啟動TFB-Tools3外掛工具' 成功!!")


        # 寫入修改的設定值
        config.write(open(configPath, "w"))
        print("Success: 儲存設定 成功!!")
        
        
        
        
        

    except:
        print("Error: 設定QGIS3系統參數失敗!!")
        pass
        
copyTFB_Tools3()
editQGIS3ini()

os.system("pause")
    







# config = configparser.ConfigParser()    # 注意大小写
# config.read(r"D:\Vincent\01_Project\108_林務局QGIS\QGIS_auto\QGIS3.ini")   # 配置文件的路径
# print(config.sections())
# print(config.options("app"))
# print(config.items("Processing"))
# print(config.get("Processing", "tfb_tools"))  
# config.set("app", r"plugin_repositories\testurl\url", "http://orfeo-toolbox.org/qgis/plugins.xml")
# config.set("app", r"plugin_repositories\testurl\authcfg", "")
# config.set("app", r"plugin_repositories\testurl\enabled", "true")

# print(config.get("Processing", "tfb_tools"))  
# config.write(open(r"D:\Vincent\01_Project\108_林務局QGIS\QGIS_auto\QGIS3.ini", "w"))  
# conf.add_section('a_new_section')

# 複製外掛程式到指定資料夾
# shutil.copytree(r'C:\Users\vincentlu\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\TFB-Tools3',r'D:\Vincent\01_Project\108_林務局QGIS\QGIS_auto\TFB-Tools3_copy')





# import sys
# import configparser
# import os
 
# def loadINI():
#     curpath = os.path.dirname(os.path.realpath(__file__))
#     cfgpath = os.path.join(curpath, 'QGIS3.ini')
#     # 創建對象
#     conf = configparser.Configparser()
#     # 讀取INI
#     conf.read(cfgpath, encoding='utf-8')
#     # 取得所有sections
#     sections = conf.sections()
#     # 取得某section之所有items，返回格式為list
#     items = conf.items('section1')
#     return ([sections, items])
 
# iniContent = loadINI()
# print('Sections= ' + iniContent[0])
# print('\nItems= ' + iniContent[1])
 
# input("按下任意鍵結束")