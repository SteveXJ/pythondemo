"""
WorkFlow: Catalogue
Current Action: Customer role create request
Status: Draft -->Submitted to Approver
"""
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,doctest
import Common.function as function
# import setting

class Cust_Draft_SubtoApp(unittest.TestCase):
    def setUp(self):
        self.driver = function.getDriver()
        self.driver.implicitly_wait(60)
        self.base_url = "https://w3-01.sso.ibm.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_draft_to_submitted(self):
        driver = self.driver
        driver.maximize_window()  #max the browser
        driver.get(self.base_url + function.versionUrl() +"/WWW/CUSTOMER/CUSTOMER_homepage.wss")
        function.writerole("Customer")
        role = function.logonname("Cus")
        function.rolelogin(role,driver)
        sitvalue = function.siteData()
        catagoryvalue = function.catagoryData() 
        driver.find_element_by_link_text("New request").click()
        Select(driver.find_element_by_id("lb_selectCategoryLB")).select_by_visible_text("Catalogue list")
        Select(driver.find_element_by_id("lb_selectCustomerLB")).select_by_visible_text(sitvalue)
        Select(driver.find_element_by_id("lb_selectTLCategoryLB")).select_by_visible_text(catagoryvalue)
        btncontinue_js = '''document.getElementById('b_btn_ContinueShoppingRequestApprover').click()'''
        driver.execute_script(btncontinue_js)
        data1,data2,data3 = function.cartData()
        driver.find_element_by_id(data1).send_keys("1")
        time.sleep(2)
        driver.find_element_by_id(data2).send_keys("2")
        time.sleep(2)
        driver.find_element_by_id(data3).send_keys("2")
        #Forward to scrolltobtm func in function.py
        function.scrolltobtm(driver)
        time.sleep(2)
        #button: Add to cart
        btncart_js = '''document.getElementById('b_btn_addCatalogueToCart').click();'''
        driver.execute_script(btncart_js)
        time.sleep(3)
        #Forward to scrolltomid func in function.py
        function.scrolltomid(driver)
        time.sleep(2)
        #button: Continue with Catalogue details
        btncontinue_js = '''document.getElementById('b_btn_ContinuetoCATRequest').click(); '''
        driver.execute_script(btncontinue_js)
        time.sleep(3)
        driver.find_element_by_id("ifd_DepReference").send_keys("Customer Create")
        time.sleep(2)
        driver.find_element_by_id("ta_DepDescription").send_keys("Catalogue workflow")
        time.sleep(2)
        driver.find_element_by_id("ta_DeploymentComments").send_keys("Customer role create request")
        time.sleep(2)
        #Forward to scrolltobtm function in function.py
        function.scrolltobtm(driver)
        time.sleep(3)
        #SaveAsDraft button
        btndraft_js = '''document.getElementById('b_btn_SaveasDraft_CAT').click()'''
        driver.execute_script(btndraft_js)
        time.sleep(3)
        #Get Current URL and split 
        termDocId = driver.current_url.split("&")[0].split('=')[1]
        #Get record number and calculate the page number
        recnumber = int(driver.find_element_by_xpath("//*[@id='type1top_rpt_Catalogues_Draft']/strong[2]").text)
        pageno = int(recnumber)/100+1
        # Draft status turn page code begin
        flag = True
        currentpage = 1
        while currentpage <= pageno and flag == True:
            index = 1
            while(index <= 100):
                href = driver.find_element_by_xpath("//*[@id='ibm-content-main']/table/tbody/tr[%s]/td[2]/a"%index).get_attribute("href")
                docid = str(href.split("&")[0].split("=")[1])
                if docid == termDocId:
                    flag = False
                    reqid = driver.find_element_by_xpath("//*[@id='ibm-content-main']/table/tbody/tr[%s]/td[2]/a"%index).text
                    function.writefile(reqid)
                    driver.find_element_by_xpath("//*[@id='ibm-content-main']/table/tbody/tr[%s]/td[2]/a"%index).click()
                    break
                index += 1
            if flag == True:
                driver.find_element_by_id("next_top_rpt_Catalogues_Draft").click()
                currentpage += 1
        # Draft status turn page code end
        time.sleep(15)
        function.scrolltobtm(driver)
        time.sleep(3)
        btnsubmittoapp = '''document.getElementById('b_btn_SendforApproval_CAT').click()'''
        driver.execute_script(btnsubmittoapp)
        time.sleep(3)
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to perform this action[\s\S]$")
        try:
            self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^The request has been successfully submitted[\s\S]$")
        except:
            pass
        print "Status from Draft to Submitted to Approval Successfully!!" 

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # setting.init()
    suite = unittest.TestSuite()
    suite.addTest(Cust_Draft_SubtoApp("test_draft_to_submitted"))
    unittest.TextTestRunner().run(suite)