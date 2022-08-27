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

class order_history(Base):
    
    def test_Order_History(self):
        try:
            var.dict_page["total_tc"] += 1
            self.demo_login()
            time.sleep(3)
            self.driver.find_element(By.ID, Locators.sideMenu_orderHistory).click()
            time.sleep(3)
            if self.driver.current_url == self.base_url + "orders" and self.driver.find_element(By.ID, Locators.orderHistoryTxt).get_attribute('textContent') == "Order History":
                self.sheet1.cell(2, 2).value = "pass"
                self.wb.save("member.xlsx")
                var.dict_page["passed_tc"] += 1
            else:
                self.sheet1.cell(2, 2).value = "fail"
                self.wb.save("member.xlsx")
                var.dict_page["failed_tc"] += 1
            time.sleep(3)
        except Exception as exception:
            self.driver.get_screenshot_as_file(os.getenv('screenshot_path'))
            function_name = "test_Order_History"
            self.final_mail(exception, function_name)
            var.dict_page["failed_tc"] += 1

    # def test_z(self):
    #     # var.arr.append(var.dict_page) 
    #     # var.arr.append(var.dict_login)

    #     # var.arr.append(self.dict_login) 
    #     print(var.arr) 
    #     head = {"page", "total_tc", "passed_tc", "failed_tc"}
    #     # tabulate(var.arr, headers={'foo': 'Foo Value', 'bar': 'Bar Count'})

    #     print(tabulate(var.arr, tablefmt="grid"))   
