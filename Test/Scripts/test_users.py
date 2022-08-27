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

class users(Base):
    
    def test_a_users(self):
        try:
            var.dict_page["total_tc"] += 1
            self.demo_login()
            time.sleep(3)
            self.driver.find_element(By.ID, Locators.SideMenu_Users).click()
            time.sleep(3)
            if self.driver.current_url == self.base_url + "users" and self.driver.find_element(By.ID, Locators.usersTxt).get_attribute('textContent') == "Users":
                self.sheet1.cell(16, 2).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_page["passed_tc"] += 1
            else:
                self.sheet1.cell(16, 2).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_page["failed_tc"] += 1
            time.sleep(3)
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_users"
            self.final_mail(exception, function_name) 
            var.dict_page["failed_tc"] += 1

    def test_b_users_search(self):
        try:
            var.dict_users_list["total_tc"] += 1
            search = self.driver.find_element(By.ID, Locators.users_search)
            search.clear()
            search.send_keys(self.sheet8.cell(2, 1).value)
            self.driver.find_element(By.ID, Locators.users_search_submit).click()
            time.sleep(2)
            if self.driver.find_element(By.ID, Locators.usersTxt).get_attribute('textContent') == "Users":
                self.sheet8.cell(2, 4).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_users_list["passed_tc"] += 1
            else:
                self.sheet8.cell(2, 4).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_users_list["failed_tc"] += 1
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_users_search"
            self.final_mail(exception, function_name)
            var.dict_users_list["failed_tc"] += 1

    def test_c_users_stats(self):
        try:
            var.dict_page["total_tc"] += 1
            self.driver.find_element(By.XPATH, Locators.stats).click()
            time.sleep(2)
            if self.driver.find_element(By.ID, Locators.statsTxt).get_attribute('textContent') == "Downloads":
                self.sheet1.cell(17, 2).value = "pass"
                self.wb.save("member.xlsx")
                self.driver.back()
                var.dict_page["passed_tc"] += 1
            else:
                self.sheet1.cell(17, 2).value = "fail"
                self.wb.save("member.xlsx")
                self.driver.back()
                var.dict_page["failed_tc"] += 1
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_users_stats"
            self.final_mail(exception, function_name) 
            var.dict_page["failed_tc"] += 1 

    def test_d_users_add(self):
        try:
            var.dict_users_add["total_tc"] += self.sheet9.max_row-1
            for row in range(2, self.sheet9.max_row + 1):
                time.sleep(2)
                self.driver.find_element(By.ID, Locators.add_org_user).click()
                time.sleep(2)
                fullName = self.driver.find_element(By.NAME, Locators.user_full_name)
                fullName.clear()
                fullName.send_keys(self.sheet9.cell(row, 1).value)

                txtPhone = self.driver.find_element(By.NAME, Locators.user_phone_no)
                txtPhone.clear()
                txtPhone.send_keys(self.sheet9.cell(row, 2).value)

                user_businessEmail = self.driver.find_element(By.ID, Locators.user_businessEmail)
                user_businessEmail.clear()
                user_businessEmail.send_keys(self.sheet9.cell(row, 3).value)

                user_job_title = self.driver.find_element(By.NAME, Locators.user_job_title)
                user_job_title.clear()
                user_job_title.send_keys(self.sheet9.cell(row, 4).value)

                select = Select(self.driver.find_element(By.NAME, Locators.user_country_id))
                select.select_by_visible_text(self.sheet9.cell(row, 5).value)

                user_address = self.driver.find_element(By.NAME, Locators.user_address)
                user_address.clear()
                user_address.send_keys(self.sheet9.cell(row, 5).value)

                user_password = self.driver.find_element(By.NAME, Locators.user_password)
                user_password.clear()
                user_password.send_keys(self.sheet9.cell(row, 7).value)

                select = Select(self.driver.find_element(By.NAME, Locators.user_member_type))
                select.select_by_visible_text(self.sheet9.cell(row, 8).value)

                

                self.driver.find_element(By.ID, Locators.at_save_user).click()
                time.sleep(8)
                # a=self.driver.find_element(By.ID, Locators.save_user_message).get_attribute('textContent')
                # print(a)
                # expected_op = self.sheet9.cell(row, 7).value
                if self.sheet9.cell(row, 11).value == "pass":
                    if self.driver.current_url == self.base_url + "users" and self.driver.find_element(By.ID, Locators.usersTxt).get_attribute('textContent') == "Users":
                        self.sheet9.cell(row, 12).value = "pass"
                        self.wb.save("member.xlsx")
                        var.dict_users_add["passed_tc"] += 1
                    else:
                        self.sheet9.cell(row, 12).value = "fail"
                        self.wb.save("member.xlsx")
                        self.driver.back()
                        var.dict_users_add["failed_tc"] += 1
                else:
                    if self.driver.current_url == self.base_url + "users" and self.driver.find_element(By.ID, Locators.usersTxt).get_attribute('textContent') == "Users":
                        self.sheet9.cell(row, 12).value = "fail"
                        self.wb.save("member.xlsx")
                        var.dict_users_add["failed_tc"] += 1
                        # self.driver.back()

                    else:
                        self.sheet9.cell(row, 12).value = "pass"
                        self.wb.save("member.xlsx")
                        self.driver.back()
                        var.dict_users_add["passed_tc"] += 1
            time.sleep(4) 
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_users_add"
            self.final_mail(exception, function_name)  
            var.dict_users_add["failed_tc"] += 1  

    def test_e_users_edit(self):
        try:
            var.dict_users_edit["total_tc"] += self.sheet10.max_row-1
            for row in range(2, self.sheet10.max_row + 1):
                time.sleep(2)
                self.driver.find_element(By.XPATH, Locators.edit_org_user).click()
                time.sleep(2)
                fullName = self.driver.find_element(By.NAME, Locators.user_full_name)
                fullName.clear()
                fullName.send_keys(self.sheet10.cell(row, 1).value)

                txtPhone = self.driver.find_element(By.NAME, Locators.user_phone_no)
                txtPhone.clear()
                txtPhone.send_keys(self.sheet10.cell(row, 2).value)

                user_job_title = self.driver.find_element(By.NAME, Locators.user_job_title)
                user_job_title.clear()
                user_job_title.send_keys(self.sheet10.cell(row, 4).value)

                select = Select(self.driver.find_element(By.NAME, Locators.user_country_id))
                select.select_by_visible_text(self.sheet10.cell(row, 5).value)

                user_address = self.driver.find_element(By.NAME, Locators.user_address)
                user_address.clear()
                user_address.send_keys(self.sheet10.cell(row, 5).value)

                user_password = self.driver.find_element(By.NAME, Locators.user_password)
                user_password.clear()
                user_password.send_keys(self.sheet10.cell(row, 7).value)

                select = Select(self.driver.find_element(By.NAME, Locators.user_member_type))
                select.select_by_visible_text(self.sheet10.cell(row, 8).value)

                

                self.driver.find_element(By.ID, Locators.at_edit_user).click()
                time.sleep(8)
            
                if self.sheet10.cell(row, 11).value == "pass":
                    if self.driver.current_url == self.base_url + "users" and self.driver.find_element(By.ID, Locators.usersTxt).get_attribute('textContent') == "Users":
                        self.sheet10.cell(row, 12).value = "pass"
                        self.wb.save("member.xlsx")
                        var.dict_users_edit["passed_tc"] += 1
                    else:
                        self.sheet10.cell(row, 12).value = "fail"
                        self.wb.save("member.xlsx")
                        var.dict_users_edit["failed_tc"] += 1
                        self.driver.back()
                else:
                    if self.driver.current_url == self.base_url + "users" and self.driver.find_element(By.ID, Locators.usersTxt).get_attribute('textContent') == "Users":
                        self.sheet10.cell(row, 12).value = "fail"
                        self.wb.save("member.xlsx")
                        var.dict_users_edit["failed_tc"] += 1
                        # self.driver.back()
                    else:
                        self.sheet10.cell(row, 12).value = "pass"
                        self.wb.save("member.xlsx")
                        self.driver.back()
                        var.dict_users_edit["passed_tc"] += 1

            time.sleep(4) 
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_e_users_edit"
            self.final_mail(exception, function_name) 
            var.dict_users_edit["failed_tc"] += 1                                                             