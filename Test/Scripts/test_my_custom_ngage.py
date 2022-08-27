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

class my_custom_ngage(Base):

    def test_my_custom_ngage(self):
        try:
            var.dict_page["total_tc"] += 1
            self.demo_login()
            time.sleep(3)
            self.driver.find_element(By.ID, Locators.SideMenu_my_custom_ngage).click()
            time.sleep(3)
            if self.driver.current_url == self.base_url + "my-custom-ngage" and self.driver.find_element(By.ID, Locators.myCustomNgageTxt).get_attribute('textContent') == "My Custom Ngage":
                self.sheet1.cell(5, 2).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_page["passed_tc"] += 1
            else:
                self.sheet1.cell(5, 2).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_page["failed_tc"] += 1 
            # time.sleep(3)    
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_my_custom_ngage"
            self.final_mail(exception, function_name)  
            var.dict_page["failed_tc"] += 1        

    def test_my_requests(self):
        try:
            var.dict_page["total_tc"] += 1
            self.driver.find_element(By.ID, Locators.MyRequests).click()
            time.sleep(3)
            if self.driver.current_url == self.base_url + "my-customization-requests" and self.driver.find_element(By.ID, Locators.myRequestsTxt).get_attribute('textContent') == "My Requests":
                self.sheet1.cell(10, 2).value = "pass"
                self.wb.save("member.xlsx")
                self.driver.back()
                var.dict_page["passed_tc"] += 1
            else:
                self.sheet1.cell(10, 2).value = "fail"
                self.wb.save("member.xlsx")
                self.driver.back()
                var.dict_page["failed_tc"] += 1 
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_my_requests"
            self.final_mail(exception, function_name)
            var.dict_page["failed_tc"] += 1 
        
    def test_request_customization(self):
        try:
            var.dict_My_Custom_Ngage["total_tc"] += self.sheet3.max_row-1
            for row in range(2, self.sheet3.max_row + 1):
                time.sleep(2)
                self.driver.find_element(By.ID, Locators.RequestCustomization).click()
                time.sleep(3)
                report_Name = self.driver.find_element(By.ID, Locators.report_Name)
                report_Name.clear()
                report_Name.send_keys(self.sheet3.cell(row, 1).value)
                select = Select(self.driver.find_element(By.NAME, Locators.category))
                select.select_by_visible_text(self.sheet3.cell(row, 2).value)
                description = self.driver.find_element(By.ID, Locators.description)
                description.clear()
                description.send_keys(self.sheet3.cell(row, 3).value)
                self.driver.find_element(By.ID, "save_changes").click()
                time.sleep(3)
                # success = driver.find_element(By.ID, "request_customization_message").get_attribute('textContent')
                # expected_text = "Successfully submited report customization."
                # driver.assertEquals(success, expected_text)
                # time.sleep(3)

                # expected_op = self.sheet3.cell(row, 4).value
                if self.sheet3.cell(row, 4).value == "pass":
                    if self.driver.find_element(By.ID, Locators.request_customization_message).get_attribute('textContent') == "Successfully submited report customization.":
                        self.sheet3.cell(row, 5).value = "pass"
                        self.wb.save("member.xlsx")
                        var.dict_My_Custom_Ngage["passed_tc"] += 1
                        time.sleep(4)
                    else:
                        self.sheet3.cell(row, 5).value = "fail"
                        self.wb.save("member.xlsx")
                        var.dict_My_Custom_Ngage["failed_tc"] += 1
                        self.driver.find_element(By.ID, "Close").click()
                else:
                    if self.driver.find_element(By.ID, Locators.request_customization_message).get_attribute('textContent') == "Successfully submited report customization.":
                        self.sheet3.cell(row, 5).value = "fail"
                        self.wb.save("member.xlsx")
                        # time.sleep(4)
                        var.dict_My_Custom_Ngage["failed_tc"] += 1
                        # driver.find_element(By.ID, "Close").click()
                    else:
                        self.sheet3.cell(row, 5).value = "pass"
                        self.wb.save("member.xlsx")
                        var.dict_My_Custom_Ngage["passed_tc"] += 1
                        time.sleep(4)
                        self.driver.find_element(By.ID, "Close").click()
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_request_customization"
            self.final_mail(exception, function_name)
            var.dict_My_Custom_Ngage["failed_tc"] += 1
    