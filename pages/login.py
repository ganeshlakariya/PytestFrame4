class login():
    def __init__(self,driver):
        self.driver = driver

        self.username_name = "username"
        self.password_name = "password"
        self.login_class_name = "button"

    def usernamebox(self,uvalue):
        self.driver.find_element_by_name(self.username_name).send_keys(uvalue)

    def passwordbox(self,pvalue):
        self.driver.find_element_by_name(self.password_name).send_keys(pvalue)

    def logintab(self):
        self.driver.find_element_by_class_name(self.login_class_name).click()

