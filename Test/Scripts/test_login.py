import unittest
import os
import sys
from dotenv import load_dotenv
load_dotenv()
sys.path.insert(0, os.getenv('basepy_path'))
from base import Base
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

sys.path.insert(0, os.getenv('locator_path'))
from locator import Locators

sys.path.insert(0, os.getenv('project_path'))
import var

class Login(Base):

    def test_login_page(self):
        try:
            var.dict_page["total_tc"] += 1
            if self.driver.find_element(By.ID, Locators.signInTxt).get_attribute('textContent') == "Sign in to MarketNgage":
                self.sheet1.cell(13, 2).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_page["passed_tc"] += 1
            else:
                self.sheet1.cell(13, 2).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_page["failed_tc"] += 1
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_login_page"
            self.final_mail(exception, function_name)
            var.dict_page["failed_tc"] += 1 


    def test_login(self):
        try:
            var.dict_login["total_tc"] += self.sheet.max_row-1
            for row in range(2, self.sheet.max_row+1):
                email = self.driver.find_element(By.ID, Locators.email)
                email.clear()
                email.send_keys(self.sheet.cell(row, 1).value)
                password = self.driver.find_element(By.NAME, Locators.password)
                password.clear()
                password.send_keys(self.sheet.cell(row, 2).value)
                self.driver.find_element(By.ID, Locators.login).click()
                time.sleep(3)
                # expected_op = self.sheet.cell(row, 3).value
                if self.sheet.cell(row, 3).value == "pass":
                    if self.driver.current_url == self.base_url + "dashboard" and self.driver.find_element(By.ID, Locators.dashboard).get_attribute('textContent') == "Recent Reports":
                        self.sheet.cell(row, 4).value = "pass"
                        var.dict_login["passed_tc"] += 1
                        self.wb.save("member.xlsx")
                        self.driver.find_element(By.ID, Locators.logout).click()
                    else:
                        self.sheet.cell(row, 4).value = "fail"
                        self.wb.save("member.xlsx")
                        var.dict_login["failed_tc"] += 1
                else:
                    if self.driver.current_url == self.base_url + "dashboard":
                        self.sheet.cell(row, 4).value = "fail"
                        self.wb.save("member.xlsx")
                        var.dict_login["failed_tc"] += 1
                    else:
                        self.sheet.cell(row, 4).value = "pass"
                        self.wb.save("member.xlsx")
                        var.dict_login["passed_tc"] += 1
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_login"
            self.final_mail(exception, function_name)
            var.dict_login["failed_tc"] += 1         

    def test_logout(self):
        try:
            var.dict_page["total_tc"] += 1
            time.sleep(1)
            self.driver.get(self.base_url)
            # self.demo_login()
            self.driver.find_element(By.ID, Locators.email).send_keys(self.sheet.cell(2, 1).value)
            self.driver.find_element(By.NAME, Locators.password).send_keys(self.sheet.cell(2, 2).value)
            self.driver.find_element(By.ID, Locators.login).click()
            time.sleep(1)
            time.sleep(1)
            self.driver.find_element(By.ID, Locators.logout).click()
            self.driver.get(self.base_url+"dashboard")
            if self.driver.current_url == self.base_url + "dashboard" and self.driver.find_element(By.ID, Locators.dashboard).get_attribute('textContent') == "Recent Reports":
                self.sheet1.cell(14, 2).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_page["failed_tc"] += 1
                self.driver.find_element(By.ID, Locators.logout).click()
            else:
                self.sheet1.cell(14, 2).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_page["passed_tc"] += 1
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_logout"
            self.final_mail(exception, function_name)
            var.dict_page["failed_tc"] += 1 

    # def test_z(self):
    #     var.arr.append(var.dict_page) 
    #     var.arr.append(var.dict_login)

    #     # var.arr.append(self.dict_login) 
    #     print(var.arr)                
   
# if __name__ == '__main__':
#     unittest.main()


    # test1 = unittest.TestLoader().loadTestsFromTestCase(Test1)
    # test2 = unittest.TestLoader().loadTestsFromTestCase(Test2)
    #
    # # create a test suite combining search_text and home_page_test
    # test_suite = unittest.TestSuite([test1, test2])
    #
    # # run the suite
    # unittest.TextTestRunner(verbosity=2).run(test_suite)