import unittest
import os
import sys
from dotenv import load_dotenv
load_dotenv()
sys.path.insert(0, os.getenv('basepy_path'))
from base import Base
from selenium.webdriver.common.by import By
import time

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


sys.path.insert(0, os.getenv('locator_path'))
from locator import Locators

sys.path.insert(0, os.getenv('project_path'))
import var

from tabulate import tabulate
from prettytable import PrettyTable

from datetime import date


class Mail(unittest.TestCase):
    
    def test_final_mail(self):
        today = date.today()
        d1 = today.strftime("%d-%m-%Y")
        toaddr = "aravind@auroraelabs.com"
        # sub = "MarketNgage Automated Testing Results for "
        # subject = sub+str(d1)
        subject = f"MarketNgage - Automation Test Results for {d1} "
        # body = f"Dear team, Below are the results for the automated testing carried out on {d1} for MarketNgage. For more details on the test cases and their results, please see the attached excel sheet."
        filename = f"MarketNgage - Automation Test Results {d1}.xlsx"
        Path = os.getenv('excel_path')

        fromaddr = "aravind@auroraelabs.com"

        msg = MIMEMultipart()
        recipients = ['aravind@auroraelabs.com']
        # r = os.getenv('recipients')
        # print(recipients)
        # print(r)
        msg['From'] = fromaddr
        # msg['To'] = toaddr
        msg['To'] = ", ".join(recipients)
        msg['Subject'] = subject

        tabular_fields = ["TestCases Group", "Total", "Passed", "Failed"]
        tabular_table = PrettyTable()
        tabular_table.field_names = tabular_fields

        for x in var.arr:
            # print(x)
            tabular_table.add_row(x.values())
            my_table = tabular_table.get_html_string()

        # html2 = """\
        # <html>
        #   <head></head>
        #   <body>
        #     <p>Please find the attachment to Automated testing results of Marketngage member portal<br>
           
        #     </p>
            
        #   </body>
        # </html>
        # """
        # html2 = """\<!DOCTYPE html><html><head><title>Marketngage Email</title><meta name='viewport' content='width=device-width, initial-scale=1.0'><style>.services{margin:0;padding:0;margin:0px;font-size:12px;font-weight:500;line-height:1.25;text-align:left;letter-spacing:0.5px;background-color:#055d9c;padding:5px;text-transform:uppercase;font-family:Roboto,RobotoDraft,Helvetica,Arial,sans-serif;color:white}.services-1{margin:0;padding:0;margin:0px;font-size:11px;font-weight:500;line-height:1.25;text-align:left;letter-spacing:0.5px;background-color:#055d9c;padding:5px;text-transform:uppercase;font-family:Roboto,RobotoDraft,Helvetica,Arial,sans-serif;color:white}.for-mobile{display:none}@media only screen and (max-width: 576px){.for-pc{display:none}}@media only screen and (max-width: 576px){.for-mobile{display:block}}</style></head><body style='width: 100%;height: auto;margin: 0;padding: 0;background-color: #ffffff;'><div class='container' style='width: 100%;margin-right: auto;margin-left: auto;background-color: #eff2f6;'> <a href='member.marketngage.com' target='_blank'><div class='header' style='background-color: #055d9c;text-align: center;'> <img src='member.marketngage.com/images/favicon.png' alt='' style='padding: 20px;'></div> </a><div style='padding: 20px;'><table width='100%' cellspacing='0' cellpadding='0' style='padding: 10px;text-align: center;background-color: #fff;padding:10% 0%;'><tbody><tr style='margin:0;padding:0'><td style='margin:0;padding:0;text-align:center'><p style='font-size: 15px;padding: 15px 10px;font-weight: 400;line-height: 1.55;text-align: left;letter-spacing: 0.5px;color: #055d9c;font-family: Roboto,RobotoDraft,Helvetica,Arial,sans-serif;'>Please find the attachment to Automated testing results of Marketngage member portal.</p></td></tr></tbody></table></div><div style='margin:0;padding:0 15px;background:#eff2f6;'><table width='100%' cellspacing='0' cellpadding='0' style='padding: 10px;text-align: center;background-color: #055d9c;'><tbody><tr style='margin:0;padding:0'><td style='margin:0;padding:0;text-align:center'><p style='font-size: 10px;padding: 8px;font-weight: 500;line-height: 1.55;text-align: center;letter-spacing: 0.5px;color: #fff;font-family: Roboto,RobotoDraft,Helvetica,Arial,sans-serif; margin: 0px;'>© Copyright 2021, Marketngage, Inc. All Rights Reserved.</p></td></tr></tbody></table></div></div></body></html>""" 

        html = """\
        <!DOCTYPE html>
        <html>
        <head>
            <title>Marketngage Email</title>
            <meta name='viewport' content='width=device-width, initial-scale=1.0'>
            <style>

            table {
            font-family: arial, sans-serif;
            border-collapse: collapse;
            width: 100%%;
            background-color: #f9f9f9;
            }

            td, th {
            border: 1px solid #e9ecef;
            text-align: center;
            padding: 8px;
            }

            tr:nth-child(even) {
            background-color: #dddddd !important;
            }

            .services {
                margin: 0;
                padding: 0;
                margin: 0px;
                font-size: 12px;
                font-weight: 500;
                line-height: 1.25;
                text-align: left;
                letter-spacing: 0.5px;
                background-color: #055d9c;
                padding: 5px;
                text-transform: uppercase;
                font-family: Roboto, RobotoDraft, Helvetica, Arial, sans-serif;
                color: white;
            }

            .services-1 {
                margin: 0;
                padding: 0;
                margin: 0px;
                font-size: 11px;
                font-weight: 500;
                line-height: 1.25;
                text-align: left;
                letter-spacing: 0.5px;
                background-color: #055d9c;
                padding: 5px;
                text-transform: uppercase;
                font-family: Roboto, RobotoDraft, Helvetica, Arial, sans-serif;
                color: white;
            }

            .for-mobile {
                display: none;
            }

            @media only screen and (max-width: 576px) {
                .for-pc {
                    display: none;
                }
            }

            @media only screen and (max-width: 576px) {
                .for-mobile {
                    display: block;
                }
            }
            </style>
        </head>
        <body style='width: 100%%;height: auto;margin: 0;padding: 0;background-color: #ffffff;'>
            <div class='container' style='width: 100%%;margin-right: auto;margin-left: auto;background-color: #eff2f6 !important;'> <a
                    href='member.marketngage.com' target='_blank'>
                    <div class='header' style='background-color: #055d9c;text-align: center;'> <img
                            src='member.marketngage.com/images/favicon.png' alt='' style='padding: 20px;'>
                    </div>
                </a>
                <div style='padding: 40px 40px 0px 40px;'>
                    <p
                        style='font-size: 15px;padding: 15px 10px;font-weight: 400;line-height: 1.55;text-align: left;letter-spacing: 0.5px;color: #055d9c;font-family: Roboto,RobotoDraft,Helvetica,Arial,sans-serif;'>
                        Dear team, Below are the results for the automated testing carried out on """+(d1)+""" for MarketNgage.<br> For more details on the test cases and their results, please see the attached excel sheet. 
                    </p>
                </div>   
            </div>
        </body>
        </html>""" 

        html2 = """\
        <!DOCTYPE html>
        <html>
        <head>
            <title>Marketngage Email</title>
            <meta name='viewport' content='width=device-width, initial-scale=1.0'>
            <style>

            table {
            font-family: arial, sans-serif;
            border-collapse: collapse;
            width: 100%%;
            background-color: #f9f9f9;
            }

            td, th {
            border: 1px solid #e9ecef;
            text-align: center;
            padding: 8px;
            }

            tr:nth-child(even) {
            background-color: #dddddd !important;
            }

            .services {
                margin: 0;
                padding: 0;
                margin: 0px;
                font-size: 12px;
                font-weight: 500;
                line-height: 1.25;
                text-align: left;
                letter-spacing: 0.5px;
                background-color: #055d9c;
                padding: 5px;
                text-transform: uppercase;
                font-family: Roboto, RobotoDraft, Helvetica, Arial, sans-serif;
                color: white;
            }

            .services-1 {
                margin: 0;
                padding: 0;
                margin: 0px;
                font-size: 11px;
                font-weight: 500;
                line-height: 1.25;
                text-align: left;
                letter-spacing: 0.5px;
                background-color: #055d9c;
                padding: 5px;
                text-transform: uppercase;
                font-family: Roboto, RobotoDraft, Helvetica, Arial, sans-serif;
                color: white;
            }

            .for-mobile {
                display: none;
            }

            @media only screen and (max-width: 576px) {
                .for-pc {
                    display: none;
                }
            }

            @media only screen and (max-width: 576px) {
                .for-mobile {
                    display: block;
                }
            }
            </style>
        </head>
        <body style='width: 100%%;height: auto;margin: 0;padding: 0;background-color: #ffffff;'>
            
                <div style='padding: 0px 40px 40px 40px;'>
                    <p
                        style='font-size: 15px;font-weight: 400;line-height: 1.55;text-align: left;letter-spacing: 0.5px;color: #055d9c;font-family: Roboto,RobotoDraft,Helvetica,Arial,sans-serif;'>
                        %s
                    </p>
                </div>
               
                    <div width='100%%' cellspacing='0' cellpadding='0'
                        style='padding: 10px;text-align: center;background-color: #055d9c;'>
                        <p
                            style='font-size: 10px;padding: 8px;font-weight: 500;line-height: 1.55;text-align: center;letter-spacing: 0.5px;color: #fff;font-family: Roboto,RobotoDraft,Helvetica,Arial,sans-serif; margin: 0px;'>
                            © Copyright 2022, Marketngage, Inc. All Rights Reserved.
                        </p>
                    </div>
                
            </div>
        </body>
        </html>""" % (my_table)

        # arr = [{'sheet_name': 'page', 'total_tc': 4, 'passe_tc': 4, 'failed_tc': 0}, {'sheet_name': 'login', 'total_tc': 4, 'passe_tc': 4, 'failed_tc': 0}]
        
        # html = """\<table id="data" class="table table-striped">
        # <thead>
        #     <tr>
        #     <th>sheet_name</th>
        #     <th>total_tc</th>
        #     <th>passe_tc</th>
        #     <th>failed_tc</th>
        #     </tr>
        # </thead>
        # <tbody>
        #     {% for a in arr %}
        #     <tr>
        #         <td>{{ a['sheet_name'] }}</td>
        #         <td>{{ a['total_tc'] }}</td>
        #         <td>{{ a['passe_tc'] }}</td>
        #         <td>{{ a['failed_tc'] }}</td>
        #     </tr>
        #     {% endfor %}
        # </tbody>
        # </table> """
            # html = """\
            # <html>
            #     <head>
            #     <style>
            #         table, th, td {
            #             border: 1px solid black;
            #             border-collapse: collapse;
            #         }
            #         th, td {
            #             padding: 5px;
            #             text-align: left;    
            #         }    
            #     </style>
            #     </head>
            # <body>
            # <p>
            # %s
            # </p>
            # </body>
            # </html>
            # """ % (my_message)

        msg.attach(MIMEText(html, 'html'))
        msg.attach(MIMEText(html2, 'html'))

        attachment = open(Path, "rb")

        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "tpmmlcsquprvwdyo")
        # text = msg.as_string()
        try:
        # sending the mail
            s.sendmail(fromaddr, recipients, msg.as_string())
            print("Successfully sent email to", recipients)
        except Exception as e:
            print("Error: unable to send email")
            # print(e)
        # terminating the session
        s.quit()

    # def test_mail(self):
    #     today = date.today()
    #     toaddr = "aravind@auroraelabs.com"
    #     subject = "MarketNgage Automated Testing Results for 26-04-2022"
    #     # body = "Please find the attachment to Automated testing results of Marketngage member portal"
    #     filename = "member.xlsx"
    #     Path = os.getenv('excel_path')
    #     self.final_mail(subject, filename, Path)