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

class my_sectors(Base):

    def test_my_sectors_list(self):
        try:
            var.dict_page["total_tc"] += 1
            self.demo_login()
            time.sleep(2)
            self.driver.find_element(By.ID, Locators.SideMenu_My_Sectors).click()
            time.sleep(3)
            if self.driver.current_url == self.base_url + "subscriptions" and self.driver.find_element(By.ID, Locators.SubscriptionsTxt).get_attribute('textContent') == "Subscriptions":
                self.sheet1.cell(7, 2).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_page["passed_tc"] += 1
            else:
                self.sheet1.cell(7, 2).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_page["failed_tc"] += 1
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_my_sectors_list"
            self.final_mail(exception, function_name)
            var.dict_page["failed_tc"] += 1         

    def test_subscriptions(self):
        try:
            var.subscriptions["total_tc"] += 1
            self.driver.find_element(By.XPATH, Locators.sub_tag).click()
            time.sleep(2)
            success_msg = self.driver.find_element(By.ID, Locators.successmsg).get_attribute('textContent')
            errormsg = self.driver.find_element(By.ID, Locators.errormsg).get_attribute('textContent')
            if self.driver.current_url == self.base_url + "subscriptions" and self.driver.find_element(By.ID, Locators.SubscriptionsTxt).get_attribute('textContent') == "Subscriptions":
                self.sheet7.cell(2, 2).value = "pass"
                self.wb.save("member.xlsx")
                var.subscriptions["passed_tc"] += 1
            else:
                self.sheet7.cell(2, 2).value = "fail"
                self.wb.save("member.xlsx")
                var.subscriptions["failed_tc"] += 1 
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_subscriptions"
            self.final_mail(exception, function_name) 
            var.subscriptions["failed_tc"] += 1         
    