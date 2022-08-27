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

class Research_Library(Base):
    
    def test_a_Research_Library(self):
        try:
            var.dict_page["total_tc"] += 1
            self.demo_login()
            time.sleep(2)
            self.driver.find_element(By.ID, "at_Research_Library").click()
            time.sleep(2)
            if self.driver.current_url == self.base_url + "reports-list" and self.driver.find_element(By.ID, Locators.reports).get_attribute('textContent') == "Reports":
                self.sheet1.cell(6, 2).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_page["passed_tc"] += 1
            else:
                self.sheet1.cell(6, 2).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_page["failed_tc"] += 1
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_a_Research_Library"
            self.final_mail(exception, function_name) 
            var.dict_page["failed_tc"] += 1         

    def test_b_reports_search(self):
        try:
            var.dict_Research_library["total_tc"] += 1
            search = self.driver.find_element(By.ID, Locators.search_filter)
            search.clear()
            search.send_keys(self.sheet5.cell(3, 1).value)
            self.driver.find_element(By.ID, Locators.submit_btn).click()
            time.sleep(2)
            if self.driver.find_element(By.ID, "at_reports").get_attribute('textContent') == "Reports":
                self.sheet5.cell(3, 5).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_Research_library["passed_tc"] += 1
            else:
                self.sheet5.cell(3, 5).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_Research_library["failed_tc"] += 1
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_b_reports_search"
            self.final_mail(exception, function_name) 
            var.dict_Research_library["failed_tc"] += 1                            

    def test_c_reports_by_category(self):
        try:
            var.dict_Research_library["total_tc"] += 1
            search = self.driver.find_element(By.ID, Locators.search_filter)
            search.clear()
            select = Select(self.driver.find_element(By.ID, Locators.category_filter))
            select.select_by_visible_text(self.sheet5.cell(4, 2).value)
            self.driver.find_element(By.ID, Locators.submit_btn).click()
            time.sleep(2)
            if self.driver.find_element(By.ID, "at_reports").get_attribute('textContent') == "Reports":
                self.sheet5.cell(4, 5).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_Research_library["passed_tc"] += 1
            else:
                self.sheet5.cell(4, 5).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_Research_library["failed_tc"] += 1
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_c_reports_by_category"
            self.final_mail(exception, function_name)
            var.dict_Research_library["failed_tc"] += 1                     

    def test_d_reports_by_type(self):
        try:
            var.dict_Research_library["total_tc"] += 1
            select = Select(self.driver.find_element(By.ID, Locators.category_filter))
            select.select_by_visible_text('Select Category')
            select = Select(self.driver.find_element(By.NAME, Locators.type_filter))
            select.select_by_visible_text(self.sheet5.cell(5, 3).value)
            self.driver.find_element(By.ID, Locators.submit_btn).click()
            time.sleep(2)
            if self.driver.find_element(By.ID, "at_reports").get_attribute('textContent') == "Reports":
                self.sheet5.cell(5, 5).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_Research_library["passed_tc"] += 1
            else:
                self.sheet5.cell(5, 5).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_Research_library["failed_tc"] += 1
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_d_reports_by_type"
            self.final_mail(exception, function_name)
            var.dict_Research_library["failed_tc"] += 1                  

    def test_e_reports_by_year(self):
        try:
            var.dict_Research_library["total_tc"] += 1
            select = Select(self.driver.find_element(By.NAME, Locators.type_filter))
            select.select_by_visible_text('Select Type')
            select = Select(self.driver.find_element(By.ID, Locators.year_filter))
            select.select_by_visible_text(self.sheet5.cell(6, 4).value)
            self.driver.find_element(By.ID, Locators.submit_btn).click()
            time.sleep(2)
            if self.driver.find_element(By.ID, "at_reports").get_attribute('textContent') == "Reports":
                self.sheet5.cell(6, 5).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_Research_library["passed_tc"] += 1
            else:
                self.sheet5.cell(6, 5).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_Research_library["failed_tc"] += 1
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_e_reports_by_year"
            self.final_mail(exception, function_name) 
            var.dict_Research_library["failed_tc"] += 1                    

    def test_f_reports(self):
        try:
            var.dict_Research_library["total_tc"] += 1
            search = self.driver.find_element(By.ID, Locators.search_filter)
            search.clear()
            search.send_keys(self.sheet5.cell(2, 1).value)        
            select = Select(self.driver.find_element(By.ID, Locators.category_filter))
            select.select_by_visible_text(self.sheet5.cell(2, 2).value)
            select = Select(self.driver.find_element(By.NAME, Locators.type_filter))
            select.select_by_visible_text(self.sheet5.cell(2, 3).value)
            select = Select(self.driver.find_element(By.ID, Locators.year_filter))
            select.select_by_visible_text(self.sheet5.cell(2, 4).value)
            self.driver.find_element(By.ID, Locators.submit_btn).click()
            # self.driver.find_element(By.ID, Locators.year_filter).send_keys(self.sheet5.cell(2, 4).value)
            time.sleep(2)
            if self.driver.find_element(By.ID, Locators.reports).get_attribute('textContent') == "Reports":
                self.sheet5.cell(2, 5).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_Research_library["passed_tc"] += 1
            else:
                self.sheet5.cell(2, 5).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_Research_library["failed_tc"] += 1
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_f_reports"
            self.final_mail(exception, function_name)
            var.dict_Research_library["failed_tc"] += 1  
