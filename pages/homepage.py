class homepage():
    def __init__(self,driver):
        self.driver = driver

        self.logout_partial_link_test = "Logout"


    def logouttab(self):
        self.driver.find_element_by_partial_link_text(self.logout_partial_link_test).click()
