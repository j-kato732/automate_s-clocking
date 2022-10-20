import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class SClocking:
    driver = None

    def __init__(self):
        self.driver = self.get_driver()

    def get_driver(self):
        driver = webdriver.Chrome(executable_path="./chromedriver")
        driver.get("https://cl.i-abs.co.jp/s-clocking/login.asp")

        return driver

    def quit(self):
        self.driver.quit()


class SClockingHandler(SClocking):
    def __init__(self, company_code, employee_code, password):
        super().__init__()
        self.company_code = company_code
        self.employee_code = employee_code
        self.password = password

    def login(self):
        # login処理
        company_code_element = self.driver.find_element(By.ID, 'inDataSource')
        company_code_element.send_keys(self.company_code)

        employ_code_element = self.driver.find_element(By.ID, 'inEmpCode')
        employ_code_element.send_keys(self.employee_code)

        password_element = self.driver.find_element(By.ID, 'inPassWord')
        password_element.send_keys(self.password)

        login_buttun_element = self.driver.find_element(By.ID, 'login')
        login_buttun_element.click()

        time.sleep(1)

    def select_engraving(self):
        # 打刻登録
        to_move_enter_time_screen_element = self.driver.find_element(
            By.XPATH, '/html/body/form/div/div/ul/li[1]/div')
        to_move_enter_time_screen_element.click()
        time.sleep(1)

    def clock_in(self):
        # 出勤を選択し、打刻する
        start_buttun_element = self.driver.find_element(By.ID, 'imgAtt0')
        start_buttun_element.click()

        self.click_engraving_buttun()
        self.click_check_buttun()
        time.sleep(1)

    def clock_out(self):
        # 退勤を選択し、打刻する
        end_time_element = self.driver.find_element(By.ID, 'imgAtt1')
        end_time_element.click()

        self.click_engraving_buttun()
        self.click_check_buttun()
        time.sleep(1)

    def click_engraving_buttun(self):
        enter_buttun_element = self.driver.find_element(By.ID, 'tdbtnEnter')
        enter_buttun_element.click()
        time.sleep(1)

    def click_check_buttun(self):
        check_buttun_element = self.driver.find_element(By.ID, 'tdbtnOK')
        check_buttun_element.click()
        time.sleep(1)
