import requests
class WebPage:
    def __init__(self, name, link):
        self.name = name
        self.link = link
        self.HTML = requests.get(link).text
    def get_HTML(self):
        return self.HTML
    def set_link(self, link):
        self.link = link
    def get_link(self):
        return self.link
    def print_HTML(self):
        print(self.get_HTML())
    def set_HTML(self, link):
        self.HTML = requests.get(link).text
    def test(self):
        self.set_HTML(self.get_link())
        self.print_HTML()
if __name__ == "__main__":
    Test = WebPage("Test", 'https://w3schools.com/python/demopage.htm')
    #Test.test()
    Test.print_HTML()
