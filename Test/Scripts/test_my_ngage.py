import unittest
import os
import sys
from dotenv import load_dotenv
load_dotenv()
sys.path.insert(0, os.getenv('basepy_path'))
from base import Base
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

sys.path.insert(0, os.getenv('locator_path'))
from locator import Locators

sys.path.insert(0, os.getenv('project_path'))
import var

class my_ngage(Base):

    def test_my_ngage(self):
        try:
            var.dict_page["total_tc"] += 1
            self.demo_login()
            time.sleep(2)
            self.driver.find_element(By.ID, Locators.sideMenu_myNgage).click()
            time.sleep(3)
            if self.driver.current_url == self.base_url + "my-ngage" and self.driver.find_element(By.ID, Locators.myNgageTxt).get_attribute('textContent') == "My Ngage":
                self.sheet1.cell(8, 2).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_page["passed_tc"] += 1
            else:
                self.sheet1.cell(8, 2).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_page["failed_tc"] += 1
            time.sleep(2)
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_my_ngage"
            self.final_mail(exception, function_name) 
            var.dict_page["failed_tc"] += 1        

    def test_report_details(self):
        try:
            var.dict_page["total_tc"] += 1
            self.driver.find_element(By.XPATH, Locators.first_report).click()
            time.sleep(3)
            if self.driver.find_element(By.ID, Locators.Subscription_Info).get_attribute('textContent') == "Subscription Info":
                self.sheet1.cell(11, 2).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_page["passed_tc"] += 1
                # self.driver.back()
            else:
                self.sheet1.cell(11, 2).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_page["failed_tc"] += 1
                # self.driver.back()
            time.sleep(2)
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_report_details"
            self.final_mail(exception, function_name) 
            var.dict_page["failed_tc"] += 1        
    
    # def test_report_view(self):
    #     try:
    #         at_ViewFullReport=self.driver.find_element(By.ID, Locators.at_ViewFullReport).get_attribute("href")
    #         if(len(at_ViewFullReport) == 0):
    #             print ("Yes")
    #         else :
    #             print ("No") 
           
    #     except Exception as exception:
    #         self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
    #         function_name = "test_report_details"
    #         self.final_mail(exception, function_name)         
