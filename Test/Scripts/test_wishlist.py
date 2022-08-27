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

class wishlist(Base):
    
    def test_wishlist(self):
        try:
            var.dict_page["total_tc"] += 1
            self.demo_login()
            time.sleep(3)
            self.driver.find_element(By.ID, Locators.sideMenu_Wish_List).click()
            time.sleep(3)
            if self.driver.current_url == self.base_url + "wishlist" and self.driver.find_element(By.ID, Locators.wishlistTxt).get_attribute('textContent') == "Wish List":
                self.sheet1.cell(3, 2).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_page["passed_tc"] += 1
            else:
                self.sheet1.cell(3, 2).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_page["failed_tc"] += 1
            time.sleep(3)
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_wishlist"
            self.final_mail(exception, function_name)
            var.dict_page["failed_tc"] += 1

    # def test_z(self):
    #     # var.arr.append(var.dict_page) 
    #     # var.arr.append(var.dict_login)

    #     # var.arr.append(self.dict_login) 
    #     print(var.arr)            