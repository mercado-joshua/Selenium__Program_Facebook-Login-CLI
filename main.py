#===========================
# Imports
#===========================

import pyinputplus as pyip
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys

#===========================
# Main App
#===========================

class Facebook_Login:
    """Facebook Login by command-line."""
    def __init__(self, username, password):
        self.driver = wd.Firefox(executable_path='C:\\Python\\Selenium\\Firefox\\geckodriver.exe')
        self.facebook_url = 'https://www.facebook.com'
        self.username = username
        self.password = password
        self.login()

    def credentials(self, _id, value):
        """Input fields to be filled-out."""
        selector = self.driver.find_element_by_id(_id)
        selector.clear()
        selector.send_keys(value)

    def clicked(self, name):
        """Simulate button clicking."""
        selector = self.driver.find_element_by_name(name)
        selector.click()

    def login(self):
        self.driver.maximize_window()
        self.driver.get(self.facebook_url)

        self.credentials('email', self.username)
        self.credentials('pass', self.password)
        self.clicked('login')

def main():
    username = pyip.inputStr('Username: ')
    password = pyip.inputPassword('Password: ')
    app = Facebook_Login(username, password)

#===========================
# Start App
#===========================

if __name__ == '__main__':
    main()

