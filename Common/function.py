# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 
import time, sys
import setting
import sqlite3

setting.init()
cursor = setting.DB_CONN.cursor()
#
# 函数名：getDriver
# 获取Driver的相关信息
#
def getDriver():
	# driver = webdriver.Firefox()
	# driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
	driver = webdriver.Remote(
		'http://9.115.28.185:4444x/wd/hub',  #Change to your own port
		DesiredCapabilities.FIREFOX)
	return driver

###Start scroll page###
#
# 函数名：scrolltobtm
# 滚动浏览器到底部
#
def scrolltobtm(driver):
	# scroll_js = '''document.body.scrollTop = 2000'''#Chrome driver
	scroll_js = '''document.documentElement.scrollTop = 2000'''#Firefox driver
	driver.execute_script(scroll_js)

#
# 函数名：scrolltomid
# 滚动浏览器到中部
#
def scrolltomid(driver):
	# scroll_js = '''document.body.scrollTop = 1000'''#Chrome driver
	scroll_js = '''document.documentElement.scrollTop = 1200'''#Firefox driver
	driver.execute_script(scroll_js)

#
# 函数名：scrolltomidtop
# 滚动浏览器到中上部
#
def scrolltomidtop(driver):
	# scroll_js = '''document.body.scrollTop = 500'''#Chrome driver
	scroll_js = '''document.documentElement.scrollTop = 500'''#Firefox driver
	driver.execute_script(scroll_js)

#
# 函数名：scrollto50
# 滚动浏览器到中上部
#
def scrollto50(driver):
	# scroll_js = '''document.body.scrollTop = 50'''#Chrome driver
	scroll_js = '''document.documentElement.scrollTop = 50'''#Firefox driver
	driver.execute_script(scroll_js)

#
# 函数名：versionUrl
# 更换版本
#
def versionUrl():
	versionurl = "/tools/wse/runtime/sit/protect/esmt/dev"
	return versionurl
###END scroll page###


###Start with DB ###
#
# 函数名：rolelogin
# 用户登录
#
def rolelogin(role,driver):
    cursor.execute("select * from user")
    for row in cursor:
        InID = row[0]
        pw = row[1]
	driver.find_element_by_id("Intranet_ID").send_keys(InID)
	driver.find_element_by_id("password").send_keys(pw)
	driver.find_element_by_name("ibm-submit").click()
	time.sleep(3)
	driver.find_element_by_id("logonName").send_keys(role)
	driver.find_element_by_name("submit").click()

#
# 函数名：logonName
# 获取当前的logonName
#
def logonname(logname):
	if logname == "Cus":
		curlogname = "Steve"
	elif logname == "IBMDepMgr":
		curlogname = "Steve"
	elif logname == "App1":
		curlogname = "Applevel1"
	elif logname == "App2":
		curlogname = "Applevel2"
	elif logname == "App3":
		curlogname = "Appleve3"
	elif logname == "IBM":
		curlogname = "Steve"
	else:
		curlogname = "Steve"
	return curlogname

#
# 函数名：sitData
# 选择sit值
#
def siteData():
	sitdata = "sit1"
	return sitdata

#
# 函数名：catagoryData
# 选择catagory值
#
def catagoryData():
	catagorydata = "catagory3"
	return catagorydata


#
# 函数名：writerole
# 将当前role写进role表中
#
def writerole(curroles):
	db_conn = sqlite3.connect(setting.DB_URI)
	cursor_local = db_conn.cursor()
	cursor_local.execute("update currentrole set rolename = ? where id =1", (curroles,))
	cursor_local.close()
	db_conn.commit()
	db_conn.close()

#
# 函数名：readrole
# 从role表中读取当前role
#
def readrole():
	cursor.execute("select rolename from currentrole where id = 1")
	values = cursor.fetchall()
	print "Current role is : " , values[0][0]
	return values[0][0]

#
# 函数名：writefile
# 将获取到的requestid写到request表中
#
def writefile(reqid):
	db_conn = sqlite3.connect(setting.DB_URI)
	cursor_local = db_conn.cursor()
	cursor_local.execute("update requestno set requestid = ? where id =1", (reqid,))
	cursor_local.close()
	db_conn.commit()
	db_conn.close()

#
# 函数名：readfile
# 从request表中获取requestid
#
def readfile():
	cursor.execute("select requestid from requestno where id = 1")
	values = cursor.fetchall()
	print "Current Requestid is : " , values[0][0]
	return values[0][0]

#
# 函数名：writerole
# 将当前role写进role表中
#
def writeneeded(appneeded):
	db_conn = sqlite3.connect(setting.DB_URI)
	cursor_local = db_conn.cursor()
	cursor_local.execute("update appneed set appneeded = ? where id =1", (appneeded,))
	cursor_local.close()
	db_conn.commit()
	db_conn.close()

#
# 函数名：readrole
# 从role表中读取当前role
#
def readneeded():
	cursor.execute("select appneeded from appneed where id = 1")
	values = cursor.fetchall()
	print "Current Approver needed status is : " , values[0][0]
	return values[0][0]

#
# 函数名：cartData
# Catalogue Cart里选择数据
#
def cartData():
	cursor.execute("select data from cartdata")
	values = cursor.fetchall()
	data1 = values[0][0]
	data2 = values[1][0]
	data3 = values[2][0]
	return data1, data2, data3

#
# 函数名：depData
# Deployment Cart里选择数据
#
def depData():
	cursor.execute("select data from depdata")
	values = cursor.fetchall()
	data1 = values[0][0]
	data2 = values[1][0]
	data3 = values[2][0]
	return data1, data2, data3

###DB END ###

#
# 函数名：deployturnpage
# Deployment Workflow status的翻页功能
#
def deployturnpage(pageno,driver,reqtype):
	flag = True
	currentpage = 1	
	requestid = str(readfile())
	while currentpage <= pageno and flag == True:
		index = 1
		while (index <= 100):
			if reqtype == 'Submitted':
				requestno = str(driver.find_element_by_xpath("//*[@id='ibm-content-main']/table/tbody/tr[%s]/td[1]/a" % index).text)
			elif reqtype == 'Proposals':
				requestno = str(driver.find_element_by_xpath("//*[@id='ibm-content-main']/div[2]/table/tbody/tr[%s]/td[1]/a" % index).text)
			if requestid == requestno:
				flag = False
				driver.find_element_by_link_text(requestid).click()
				# driver.find_element_by_xpath("//*[@id='ibm-content-main']/table/tbody/tr[%s]/td[1]/a" % index).click()
				time.sleep(5)
				print "Find the request and forward to the detail page successfully!"
				break
			index += 1
		if flag == True:
			driver.find_element_by_xpath("//*[@id='next_top_rpt_listofldrequests']").click()
			print 'Turn page successfully!'
			currentpage +=1

#
# 函数名：catalogturnpage
# Catalogue Workflow status的翻页功能
#
def catalogturnpage(pageno,driver):
	flag = True
	currentpage = 1
	requestid = str(readfile())
	time.sleep(3)
	while currentpage <= pageno and flag == True:
		index = 1
		while (index <= 100):
			requestnum = driver.find_element_by_xpath("//*[@id='ibm-content-main']/table/tbody/tr[%d]/td[1]/a"%index).text
			requestno = str(requestnum)
			# print requestno
			if requestid == requestno:
				flag = False
				# driver.find_element_by_link_text(requestid).click()
				driver.find_element_by_xpath("//*[@id='ibm-content-main']/table/tbody/tr[%d]/td[1]/a"%index).click()
				time.sleep(5)
				print "Find the request and forward to the detail page successfully!"
				break
			index += 1
		if flag == True:
			driver.find_element_by_xpath("//*[@id='next_top_rpt_Catalogues']").click()
			print 'Turn page successfully!'
			currentpage +=1

#
# 函数名：switchwindow
# 切换不同的窗口
#
def switchwindow(location,driver):
	cur_handle = driver.current_window_handle
	scrollto50(driver)
	driver.find_element_by_link_text("View History").click()
	handles = driver.window_handles
	for handle in handles:
		if handle != cur_handle:
			driver.switch_to_window(handle)
			driver.maximize_window()
			time.sleep(6)
			driver.get_screenshot_as_file(location)
			driver.close()
	driver.switch_to_window(cur_handle)


#
# 函数名：upLoad
# 上传文件
#
# def upLoad(driver):
# 	# driver.find_element_by_id("attachedcontract").clear()
# 	driver.find_element_by_id("attachedcontract").send_keys("./Common/hello.txt")
# 	btnupload_js = '''document.getElementById('b_btn_AttachFile_LD').click()'''
# 	driver.execute_script(btnupload_js)

# #
# # 函数名：uploadCatalogue
# # 上传文件
# #
# def uploadCatalogue(driver):
# 	# driver.find_element_by_id("attachedcontract").clear()
# 	driver.find_element_by_id("attachedcontract").send_keys("./Common/hello.txt")
# 	btnupload_js = '''document.getElementById('b_btn_AttachFile_CAT').click()'''
# 	driver.execute_script(btnupload_js)


# #
# # 函数名：getCurrentFileName
# # 获取当前文件名
# #
# def getCurrentFileName():
#     argv0_list = sys.argv[0].split("\\")
#     script_name = argv0_list[len(argv0_list)-1]
#     script_name = script_name[0:-3]
#     # print "Current file name = " + script_name
#     return script_name

# def reportName():
# 	currentFileName = function.getCurrentFileName()
# 	localtime = str(time.strftime('%m%d-%H%M%S',time.localtime(time.time())))
# 	filename = "../Report/" + currentFileName + "-" + localtime + ".html" #tagart path and file name
# 	fp = file(filename, 'wb')
# 	runner = HTMLTestRunner.HTMLTestRunner(stream = fp, title = u'Result', description = u'Test_Report')
# 	return (runner)

# #
# # 函数名：writefile
# # 将获取到的requestid写到requestid.txt文档中
# #
# def writefile(requestid,types):
# 	if types == "Cat" :
# 		file_object = open("../Execute/Catalogue/Requestid.txt","w")
# 	elif types == "Dep" :
# 		file_object = open("../Execute/Deployment/Requestid.txt","w")
# 	else:
# 		file_object = open("../Execute/Substution/Requestid.txt","w")
# 	file_object.write(requestid)
# 	file_object.close()

# #
# # 函数名：readfile
# # 获取读取到的requestid
# #
# def readfile(types):
# 	if types == "Cat" :
# 		file_object = open("../Execute/Catalogue/Requestid.txt","w")
# 	elif types == "Dep" :
# 		file_object = open("../Execute/Deployment/Requestid.txt","w")
# 	else:
# 		file_object = open("../Execute/Substution/Requestid.txt","w")
# 	requestid = file_object.read()
# 	return requestid
# 	file_object.close()

# #
# # 函数名：writerole
# # 将获取到的role写到createrole.txt文档中
# #
# def writerole(role,types):
# 	if types == "Cat" :
# 		file_object = open("../Execute/Catalogue/Createrole.txt","w")
# 	elif types == "Dep" :
# 		file_object = open("../Execute/Deployment/Createrole.txt","w")
# 	else:
# 		file_object = open("../Execute/Substution/Createrole.txt","w")
# 	file_object.write(role)
# 	file_object.close()

# #
# # 函数名：readrole
# # 获取读取到的createrole
# #
# def readrole(types):
# 	if types == "Cat" :
# 		file_object = open("../Execute/Catalogue/Createrole.txt","w")
# 	elif types == "Dep" :
# 		file_object = open("../Execute/Deployment/Createrole.txt","w")
# 	else:
# 		file_object = open("../Execute/Substution/Createrole.txt","w")
# 	role = file_object.read()
# 	return role
# 	file_object.close()

# #
# # 函数名：getExcel
# # # 随机读取Excel中数据
# # #
# # def getExcel(rowValue, colValue, fileName):
# # 	#Create book
# # 	book = xlrd.open_workbook(fileName)
# # 	#Get sheet name
# # 	sheet = book.sheet_by_index(0)
# # 	#Get the data in sheet 
# # 	return sheet.cell_value(rowValue,colValue)

# # #
# # # 函数名：getAllExcel
# # # 读取Excel中所有数据
# # #
# # def getAllExcel(fileName):
# # 	rows = []
# # 	#Create book
# # 	book = xlrd.open_workbook(fileName)
# # 	#Get sheet name
# # 	sheet = book.sheet_by_index(0)
# # 	for row in range(1, sheet.nrows):
# # 		rows.append(list(sheet.row_values(row, 0, sheet.ncols)))
# # 	return rows

# #
# # 函数名：cartData
# # Catalogue Cart里选择数据
# #
# def cartData():
# 	data1 = "ifd_LicencetoRequest-13431"
# 	data2 = "ifd_LicencetoRequest-13381"
# 	data3 = "ifd_LicencetoRequest-13434"
# 	return data1,data2,data3

# #
# # 函数名：DeploycartData
# # 在Deployment Cart里选择数据
# #
# def DeploycartData():
# 	data1 = "ifd_LicencetoDeploy-13431"
# 	data2 = "ifd_LicencetoDeploy-13381"
# 	data3 = "ifd_LicencetoDeploy-13434"
# 	return data1,data2,data3

