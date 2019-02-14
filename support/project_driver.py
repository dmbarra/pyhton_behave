from selenium import webdriver


class ProjectDriver:

    def __init__(self, type="local", browser="chrome"):
        if type == "local" and browser == "chrome":
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)

    def load_website(self, url):
        self.driver.get(url)
