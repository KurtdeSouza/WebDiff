from WebPage import WebPage
import difflib
class Main:
    def __init__(self, frequency, WebPage):
        self.frequency = frequency
        self.WebPage = WebPage
    def get_frequency(self):
        return self.frequency
    def set_frequency(self, frequency):
        self.frequency = frequency
    def set_WebPage(self, WebPage):
        self.WebPage = WebPage
    def get_WebPage(self):
        return self.WebPage
    def compare(self):
        old_version = self.WebPage.get_HTML()
        self.WebPage.set_HTML('http://10.0.0.57:8081/test2.html')
        new_version = self.WebPage.get_HTML()
        print(difflib.SequenceMatcher(None, old_version, new_version).ratio())

if __name__ == "__main__":
    #LinkedIN = WebPage("LinkedIN", 'https://www.linkedin.com/jobs/search/?f_E=2&f_TPR=r3600&geoId=101174742&keywords=software%20engineer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true%2F')
    #LinkedIN.test()
    #session = Main(10, LinkedIN)
    #page = session.get_WebPage()
    #page.print_HTML()  

    Test = WebPage("Test", 'http://10.0.0.57:8080/test.html')
    test_session = Main(10, Test)
    test_session.get_WebPage().print_HTML()

    while True:
        user_input = input("Enter something (type 'quit' to exit): ")
        if user_input.lower() == 'q':
            print("Exiting the program.")
            break  # Exit the loop
        else:
            test_session.compare()






