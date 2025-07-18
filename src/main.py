from WebPage import WebPage
from Email import Email
import difflib
import schedule
import time
from dotenv import load_dotenv
import os
class Main:
    def __init__(self, frequency, WebPage, Email):
        self.frequency = frequency
        self.WebPage = WebPage
        self.Email = Email
    def get_frequency(self):
        return self.frequency
    def set_frequency(self, frequency):
        self.frequency = frequency
    def set_WebPage(self, WebPage):
        self.WebPage = WebPage
    def get_WebPage(self):
        return self.WebPage
    def set_Email(self, Email):
        self.Email = Email
    def get_Email(self):
        return self.Email
    def evaluate_compare(self, diff_ratio):
        if diff_ratio < 1:
            msg = f'The contents of {self.get_WebPage().get_link()}'
            self.get_Email().set_message(msg)
            self.get_Email().write_email()
            print("Program has detected a change in the providede web page, sending email now")
        else:
            print("No change detected...")
        return
    def compare(self):
        old_version = self.WebPage.get_HTML()
        self.WebPage.set_HTML()
        new_version = self.WebPage.get_HTML()
        diff_ratio = difflib.SequenceMatcher(None, old_version, new_version).ratio()
        self.evaluate_compare(diff_ratio)
    def job(self):
        self.compare()
if __name__ == "__main__":
    LinkedIN = WebPage("LinkedIN", 'https://www.linkedin.com/jobs/search/?f_E=2&f_TPR=r3600&geoId=101174742&keywords=software%20engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true%2F')
    #LinkedIN.test()
    #session = Main(10, LinkedIN)
    #page = session.get_WebPage()
    #page.print_HTML()  
    load_dotenv()  # Load environment variables from .env

    email_user = os.getenv("EMAIL_USER")
    email_pass = os.getenv("EMAIL_PASS")
    #Test_W = WebPage("Test", 'http://10.0.0.57:8080/test.html')
    Test_E = Email(email_user, email_user, email_pass)
    test_session = Main(10, LinkedIN, Test_E)
    schedule.every(test_session.get_frequency()).minutes.do(test_session.job)

    #schedule.every(10).minutes.do(test_session.job)
    print("Starting Program...")
    
    while True:
        schedule.run_pending()
        time.sleep(1)





