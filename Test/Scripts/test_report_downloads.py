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

class ReportDownloads(Base):
    
    def test_ReportDownloads(self):
        try:
            var.dict_page["total_tc"] += 1
            self.demo_login()
            time.sleep(3)
            self.driver.find_element(By.ID, Locators.SideMenu_ReportDownloads).click()
            time.sleep(3)
            if self.driver.current_url == self.base_url + "report-downloads" and self.driver.find_element(By.ID, Locators.ReportDownloadsTxt).get_attribute('textContent') == "Report Downloads":
                self.sheet1.cell(15, 2).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_page["passed_tc"] += 1
            else:
                self.sheet1.cell(15, 2).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_page["failed_tc"] += 1
            time.sleep(3)
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_ReportDownloads"
            self.final_mail(exception, function_name)
            var.dict_page["failed_tc"] += 1 

    def test_report_downloads_search(self):
        try:
            var.dict_report_downloads["total_tc"] += 1
            search = self.driver.find_element(By.NAME, Locators.search_rep_downloads)
            search.clear()
            search.send_keys(self.sheet6.cell(2, 1).value)
            self.driver.find_element(By.ID, Locators.submit_btn).click()
            time.sleep(2)
            if self.driver.find_element(By.ID, Locators.ReportDownloadsTxt).get_attribute('textContent') == "Report Downloads":
                self.sheet6.cell(2, 2).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_report_downloads["passed_tc"] += 1
            else:
                self.sheet6.cell(2, 2).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_report_downloads["failed_tc"] += 1
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_report_downloads_search"
            self.final_mail(exception, function_name) 
            var.dict_report_downloads["failed_tc"] += 1   
