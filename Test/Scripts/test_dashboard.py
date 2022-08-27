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

class dashboard(Base):
   
    def test_a_dashboard(self):
        try:
            var.dict_page["total_tc"] += 1
            self.demo_login()
            time.sleep(2)
            self.driver.find_element(By.ID, Locators.SideMenu_Dashboard).click()
            time.sleep(2)
            if self.driver.current_url == self.base_url + "dashboard" and self.driver.find_element(By.ID, Locators.dashboard).get_attribute('textContent') == "Recent Reports":
                self.sheet1.cell(9, 2).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_page["passed_tc"] += 1
            else:
                self.sheet1.cell(9, 2).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_page["failed_tc"] += 1
            time.sleep(3)
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_dashboard"
            self.final_mail(exception, function_name)
            var.dict_page["failed_tc"] += 1         

    def test_b_dashboard_news(self):
        try:
            var.dict_page["total_tc"] += 1
            self.driver.find_element(By.ID, Locators.in_the_news).click()
            time.sleep(2)
            if self.driver.current_url == self.base_url + "news" and self.driver.find_element(By.ID, Locators.all_news_txt).get_attribute('textContent') == "All News":
                self.sheet1.cell(18, 2).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_page["passed_tc"] += 1
            else:
                self.sheet1.cell(18, 2).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_page["failed_tc"] += 1
            time.sleep(3)
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_dashboard"
            self.final_mail(exception, function_name) 
            var.dict_page["failed_tc"] += 1                
    
    def test_c_news_by_category(self):
        try:
            var.dict_news_list["total_tc"] += 1
            select = Select(self.driver.find_element(By.ID, Locators.inputCategory_filter))
            select.select_by_visible_text(self.sheet12.cell(2, 1).value)
            self.driver.find_element(By.ID, Locators.news_filter_submit).click()
            time.sleep(2)
            if self.driver.find_element(By.ID, Locators.all_news_txt).get_attribute('textContent') == "All News":
                self.sheet12.cell(2, 4).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_news_list["passed_tc"] += 1
            else:
                self.sheet12.cell(2, 4).value = "fail"
                self.wb.save("member.xlsx")
                self.driver.back()
                var.dict_news_list["failed_tc"] += 1
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_c_news_by_category"
            self.final_mail(exception, function_name)
            var.dict_news_list["failed_tc"] += 1                     

    def test_d_news_by_year(self):
        try:
            var.dict_news_list["total_tc"] += 1
            select = Select(self.driver.find_element(By.ID, Locators.inputCategory_filter))
            select.select_by_visible_text('Select Category')
            select = Select(self.driver.find_element(By.ID, Locators.news_by_year))
            select.select_by_visible_text(self.sheet12.cell(3, 2).value)
            self.driver.find_element(By.ID, Locators.news_filter_submit).click()
            time.sleep(2)
            if self.driver.find_element(By.ID, Locators.all_news_txt).get_attribute('textContent') == "All News":
                self.sheet12.cell(3, 4).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_news_list["passed_tc"] += 1
            else:
                self.sheet12.cell(3, 4).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_news_list["failed_tc"] += 1 
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_e_news_by_year"
            self.final_mail(exception, function_name) 
            var.dict_news_list["failed_tc"] += 1  

    def test_e_news_filters(self):
        try:
            var.dict_news_list["total_tc"] += 1
            select = Select(self.driver.find_element(By.ID, Locators.inputCategory_filter))
            select.select_by_visible_text(self.sheet12.cell(4, 1).value)
            select = Select(self.driver.find_element(By.ID, Locators.news_by_year))
            select.select_by_visible_text(self.sheet12.cell(4, 2).value)
            self.driver.find_element(By.ID, Locators.news_filter_submit).click()
            time.sleep(2)
            if self.driver.find_element(By.ID, Locators.all_news_txt).get_attribute('textContent') == "All News":
                self.sheet12.cell(4, 4).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_news_list["passed_tc"] += 1
            else:
                self.sheet12.cell(4, 4).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_news_list["failed_tc"] += 1 
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_e_news_filters"
            self.final_mail(exception, function_name)
            var.dict_news_list["failed_tc"] += 1                                     