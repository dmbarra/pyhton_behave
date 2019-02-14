class BasePage(object):

    def __init__(self, context):
        self.browser = context.browser
        self.timeout = 4

    def find_element(self, *loc):
        return self.browser.find_element(*loc)



