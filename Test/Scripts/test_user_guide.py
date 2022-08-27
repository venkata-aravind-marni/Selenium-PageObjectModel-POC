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

class user_guide(Base):

    def test_user_guide(self):
        try:
            var.dict_page["total_tc"] += 1
            self.demo_login()
            time.sleep(2)
            self.driver.find_element(By.ID, Locators.SideMenu_user_Guide).click()
            time.sleep(3)
            if self.driver.current_url == self.base_url + "user-guide" and self.driver.find_element(By.ID, Locators.userGuideTxt).get_attribute('textContent') == "User Guide":
                self.sheet1.cell(4, 2).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_page["passed_tc"] += 1
            else:
                self.sheet1.cell(4, 2).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_page["failed_tc"] += 1
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_user_guide"
            self.final_mail(exception, function_name) 
            var.dict_page["failed_tc"] += 1        

    def test_user_guide_view(self):
        try:
            var.dict_userGuide["total_tc"] += self.sheet2.max_row-1
            for row in range(2, self.sheet2.max_row + 1):
                pg = self.sheet2.cell(row, 1).value
                rt = self.sheet2.cell(row, 2).value
                self.driver.find_element(By.ID, pg).click()
                time.sleep(3)
                if self.sheet2.cell(row, 3).value == "pass":
                    if self.driver.current_url == self.base_url + "user-guide-details/" + rt and self.driver.find_element(By.ID, Locators.userGuideView).get_attribute('textContent') == "User Guide":
                        self.sheet2.cell(row, 4).value = "pass"
                        self.wb.save("member.xlsx")
                        self.driver.back()
                        var.dict_userGuide["passed_tc"] += 1
                    else:
                        self.sheet2.cell(row, 4).value = "fail"
                        self.wb.save("member.xlsx")
                        var.dict_userGuide["failed_tc"] += 1
                else:
                    if self.driver.current_url == self.base_url + "user-guide-details/" + rt and self.driver.find_element(By.ID, Locators.userGuideView).get_attribute('textContent') == "User Guide":
                        self.sheet2.cell(row, 4).value = "fail"
                        self.wb.save("member.xlsx")
                        var.dict_userGuide["failed_tc"] += 1
                    else:
                        self.sheet2.cell(row, 4).value = "pass"
                        self.wb.save("member.xlsx")
                        self.driver.back()
                        var.dict_userGuide["passed_tc"] += 1
            time.sleep(3)
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_user_guide_view"
            self.final_mail(exception, function_name)
            var.dict_userGuide["failed_tc"] += 1
    