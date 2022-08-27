import unittest
import os
import sys
from dotenv import load_dotenv
load_dotenv()
import schedule
import time

# from base import Base

sys.path.insert(0, os.getenv('test_script_path'))
from test_login import Login
from test_Research_Library import Research_Library
from test_my_ngage import my_ngage
from test_results_mail import Mail
from test_order_history import order_history
from test_report_downloads import ReportDownloads
from test_wishlist import wishlist
from test_my_custom_ngage import my_custom_ngage
from test_user_guide import user_guide
from test_my_sectors import my_sectors
from test_dashboard import dashboard
from test_profile import profile
from test_users import users

# from dummy import Login


sys.path.insert(0, os.getenv('base'))



from excel import Excel
e = Excel()
e.test_excel()

# a = Base()
# a.setUpClass()
# a.demo_login()

Login = unittest.TestLoader().loadTestsFromTestCase(Login)
dashboard = unittest.TestLoader().loadTestsFromTestCase(dashboard)
my_ngage = unittest.TestLoader().loadTestsFromTestCase(my_ngage)
my_custom_ngage = unittest.TestLoader().loadTestsFromTestCase(my_custom_ngage)
my_sectors = unittest.TestLoader().loadTestsFromTestCase(my_sectors)
Research_Library = unittest.TestLoader().loadTestsFromTestCase(Research_Library)
wishlist = unittest.TestLoader().loadTestsFromTestCase(wishlist)
order_history = unittest.TestLoader().loadTestsFromTestCase(order_history)
users = unittest.TestLoader().loadTestsFromTestCase(users)
ReportDownloads = unittest.TestLoader().loadTestsFromTestCase(ReportDownloads)
user_guide = unittest.TestLoader().loadTestsFromTestCase(user_guide)
profile = unittest.TestLoader().loadTestsFromTestCase(profile)
Mail = unittest.TestLoader().loadTestsFromTestCase(Mail)

# excel = unittest.TestLoader().loadTestsFromTestCase(excel)
# Login = unittest.TestLoader().loadTestsFromTestCase(Login)



# create a test suite 
test_suite = unittest.TestSuite([wishlist, Mail])
# test_suite = unittest.TestSuite([Login, dashboard, my_ngage, my_custom_ngage, my_sectors, Research_Library, wishlist, order_history, users, ReportDownloads, user_guide, profile, Mail])

# def run():
    # run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)
# run()

# schedule.every().saturday.at("10:59").do(run)
# while True:
#     schedule.run_pending()
#     time.sleep(1)