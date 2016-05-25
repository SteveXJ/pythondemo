"""
WorkFlow: Catalogue
Current action: IBMOPERATION role take action
Status: Acknowledged  --> Processed
"""
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest,time,re
import Common.function as function

class AcknowledgedToProcessed(unittest.TestCase):
    def setUp(self):
        self.driver = function.getDriver()
        self.driver.implicitly_wait(30)
        self.base_url = "https://w3-01.sso.ibm.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_acknowledged_to_processed(self):
        driver = self.driver
        driver.maximize_window()  #max the browser
        driver.get(self.base_url + function.versionUrl() +"/W3/IBMOPERATIONS/IBMOPERATIONS_homepage.wss")
        role = function.logonname("IBMOpe")
        function.rolelogin(role,driver)
        driver.find_element_by_link_text("Catalogues").click()
        driver.find_element_by_link_text("Acknowledged").click()
        recordno = int(driver.find_element_by_xpath("//*[@id='type1top_rpt_Catalogues']/strong[2]").text)
        pageno = int(recordno)/100+1
        #Forward to catalogturnpage function in function.py
        function.catalogturnpage(pageno,driver)
        time.sleep(15)
        # capturelocation = "../Capture/AcknowledgedStatus_07.png"
        # #Forward to switchwindow function in function.py
        # function.switchwindow(capturelocation,driver)
        # print "Screenshot Acknowledged status successfully"
        # time.sleep(5)
        #Forward to scrolltomid function in function.py
        function.scrolltomid(driver)
        time.sleep(2)
        btnackled_js = '''document.getElementById('b_btn_NotifyCATRequest').click()'''
        driver.execute_script(btnackled_js)
        time.sleep(3)
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to perform this action[\s\S]$")
        try:
            self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^The request has been successfully submitted[\s\S]$")
        except:
            pass
        print "Status from Acknowledged to Processed Successfully!!" 
        lotime = str(time.strftime('%m%d-%H%M%S',time.localtime(time.time())))
        capturelocation = "./Capture/" + lotime + "_CatalogueWorkflow.png"
        #Forward to switchwindow function in function.py
        function.switchwindow(capturelocation,driver)
        print "Screenshot Processed status successfully"
        
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
    suite = unittest.TestSuite()
    suite.addTest(AcknowledgedToProcessed("test_acknowledged_to_processed"))
    unittest.TextTestRunner().run(suite)