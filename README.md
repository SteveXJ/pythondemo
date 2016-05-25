# Welcome to ESMT Project 

**Below Message is about the structure of ESMT project. Before you run the code, please read this file seriously:**
 
- **1** ：Before running the code, please run "initdb.py" file under esmt folder to init the database in your local. After generated the db file(under db folder), you need to take some action.
    - Download SqliteBrowser: http://sqlitebrowser.org/ and install it as default.
    - Download HTMLTestRunner: http://tungwaiyip.info/software/HTMLTestRunner.html and transfer HTMLTestRunner.py into C:\Python27\Lib\
    - Use the sqlitebrowser to open the db file then update table "user" : Change to your mail and password
    - Update getDriver function in Common/function.py file
    ```
    def getDriver():
    	driver = webdriver.Remote(
			'http://9.115.28.185:4444x/wd/hub',  #Change 4444x to your port
			DesiredCapabilities.FIREFOX)
		return driver
    ```
- **2** ：Run "main.py" file as an entrance 
- **3** ：This Structure used sqlite db to store the data
- **4** ：Structure describtion:
	- Capture: store workflow screenshot 
	- Common: store fucntion file
	- db: store the database file
	- TestResult: store HTMLTestRunner result files
	- TS_XXX: store the case about the workflow

-------------------

**If you want to run your own data, please change below functions and tables data to yours.**

- Function: "siteData" , "catagoryData" and "logonname" in Common/function.py file
- Table: "depdata" and "cartdata" in your db file

-------------------

## Version History

> Below message is about the history version about ESMT project. You can clear each version's function after scanning it.


### 1. Catalogue Workflow  2.SendtoFirstApprover 3.Single Approver

| Version| Description  |
| :-------- | :--------:|
| V1.0.1| Customer Create |
| V1.0.2|IBMDepMgr Create|
| V1.0.3|Applevel2 Create and ApproverNeededisNO |

### 2. Catalogue Workflow  2.SendtoFirstApprover 3.Muilt Approver

| Version| Description  |
| :-------- | :--------:|
| V1.0.4| Customer Create |
| V1.0.5|IBMDepMgr Create|
| V1.0.6|Applevel2 Create and ApproverNeededisNO |

### 3. Catalogue Workflow  2.SendtoNextApprover 3.Muilt Approver

| Version| Description  |
| :-------- | :--------:|
| V1.0.7| Customer/IBMDepMgr/Applevel2(ApproverNeededisNO) Create |

### 4. Deployment Workflow  2.SendtoFirstApprover 3.Single Approver

| Version| Description  |
| :-------- | :--------:|
| V1.0.8| Customer/IBMDepMgr/Applevel2(ApproverNeededisNO) Create |

### 5. Deployment Workflow  2.SendtoFirstApprover 3.Muilt Approver

| Version| Description  |
| :-------- | :--------:|
| V1.0.9| Customer/IBMDepMgr/Applevel2(ApproverNeededisNO) Create |

### 6. Deployment Workflow  2.SendtoNextApprover 3.Muilt Approver

| Version| Description  |
| :-------- | :--------:|
| V1.0.10| Customer/IBMDepMgr/Applevel2(ApproverNeededisNO) Create |