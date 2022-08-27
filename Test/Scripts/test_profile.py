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

class profile(Base):

    def test_profile(self):
        try:
            var.dict_page["total_tc"] += 1
            self.demo_login()
            time.sleep(3)
            self.driver.find_element(By.ID, Locators.SideMenu_profile).click()
            time.sleep(3)
            if self.driver.current_url == self.base_url + "profile" and self.driver.find_element(By.ID, Locators.profleTxt).get_attribute('textContent') == "Profile":
                self.sheet1.cell(12, 2).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_page["passed_tc"] += 1
            else:
                self.sheet1.cell(12, 2).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_page["failed_tc"] += 1
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_profile"
            self.final_mail(exception, function_name)  
            var.dict_page["failed_tc"] += 1 

    def test_profile_add(self):
        try:
            var.dict_profile_edit_profile["total_tc"] += self.sheet4.max_row-1
            for row in range(2, self.sheet4.max_row + 1):
                time.sleep(5)
                self.driver.find_element(By.ID, Locators.edit_profile).click()
                time.sleep(2)
                fullName = self.driver.find_element(By.NAME, Locators.fullName)
                fullName.clear()
                fullName.send_keys(self.sheet4.cell(row, 1).value)
                select = Select(self.driver.find_element(By.NAME, Locators.country_id))
                select.select_by_visible_text(self.sheet4.cell(row, 2).value)
                txtPhone = self.driver.find_element(By.ID, Locators.txtPhone)
                txtPhone.clear()
                txtPhone.send_keys(self.sheet4.cell(row, 3).value)
                txtCompany = self.driver.find_element(By.ID, Locators.txtCompany)
                txtCompany.clear()
                txtCompany.send_keys(self.sheet4.cell(row, 4).value)
                txtDesignation = self.driver.find_element(By.ID, Locators.txtDesignation)
                txtDesignation.clear()
                txtDesignation.send_keys(self.sheet4.cell(row, 5).value)
                txtAddress = self.driver.find_element(By.ID, Locators.txtAddress)
                txtAddress.clear()
                txtAddress.send_keys(self.sheet4.cell(row, 6).value)
                self.driver.find_element(By.ID, Locators.Save_changes).click()
                time.sleep(2)
                if self.sheet4.cell(row, 7).value == "pass":
                    if self.driver.find_element(By.ID, Locators.submit_message).get_attribute('textContent') == "Profile updated successfully!":
                        self.sheet4.cell(row, 8).value = "pass"
                        self.wb.save("member.xlsx")
                        var.dict_profile_edit_profile["passed_tc"] += 1
                    else:
                        self.sheet4.cell(row, 8).value = "fail"
                        self.wb.save("member.xlsx")
                        self.driver.find_element(By.ID, "Close").click()
                        var.dict_profile_edit_profile["failed_tc"] += 1
                else:
                    if self.driver.find_element(By.ID, Locators.submit_message).get_attribute('textContent') == "Profile updated successfully!":
                        self.sheet4.cell(row, 8).value = "fail"
                        self.wb.save("member.xlsx")
                        var.dict_profile_edit_profile["failed_tc"] += 1
                        # driver.find_element(By.ID, "Close").click()
                    else:
                        self.sheet4.cell(row, 8).value = "pass"
                        self.wb.save("member.xlsx")
                        var.dict_profile_edit_profile["passed_tc"] += 1
                        self.driver.find_element(By.ID, "Close").click()
            time.sleep(4) 
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_profile_add"
            self.final_mail(exception, function_name) 
            var.dict_profile_edit_profile["failed_tc"] += 1 

    def test_profile_change_password(self):
        try:
            var.dict_change_password["total_tc"] += self.sheet11.max_row-1
            for row in range(2, self.sheet11.max_row + 1):
                time.sleep(5)
                self.driver.find_element(By.ID, Locators.changePasswordModal).click()
                time.sleep(2)
                currentPassword = self.driver.find_element(By.NAME, Locators.currentPassword)
                currentPassword.clear()
                currentPassword.send_keys(self.sheet11.cell(row, 1).value)
                newPassword = self.driver.find_element(By.NAME, Locators.newPassword)
                newPassword.clear()
                newPassword.send_keys(self.sheet11.cell(row, 2).value)
                confirm_password = self.driver.find_element(By.NAME, Locators.confirm_password)
                confirm_password.clear()
                confirm_password.send_keys(self.sheet11.cell(row, 3).value)
                self.driver.find_element(By.ID, Locators.change_password_btn).click()
                time.sleep(3)
                if self.sheet11.cell(row, 5).value == "pass":
                    if self.driver.find_element(By.ID, Locators.change_password_message).get_attribute('textContent') == "Password updated successfully":
                        self.sheet11.cell(row, 6).value = "pass"
                        self.wb.save("member.xlsx")
                        var.dict_change_password["passed_tc"] += 1
                        time.sleep(2)
                    else:
                        self.sheet11.cell(row, 6).value = "fail"
                        self.wb.save("member.xlsx")
                        self.driver.find_element(By.ID, Locators.Close_pwd_modal).click()
                        var.dict_change_password["failed_tc"] += 1
                else:
                    if self.driver.find_element(By.ID, Locators.change_password_message).get_attribute('textContent') == "Password updated successfully":
                        self.sheet11.cell(row, 6).value = "fail"
                        self.wb.save("member.xlsx")
                        var.dict_change_password["failed_tc"] += 1
                    else:
                        self.sheet11.cell(row, 6).value = "pass"
                        self.wb.save("member.xlsx")
                        self.driver.find_element(By.ID, Locators.Close_pwd_modal).click()
                        var.dict_change_password["passed_tc"] += 1
            time.sleep(1) 
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_profile_change_password"
            self.final_mail(exception, function_name)  
            var.dict_change_password["failed_tc"] += 1                    

      
    