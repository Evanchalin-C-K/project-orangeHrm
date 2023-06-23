# _Menu Validation
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def test_setup():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()


def test_login():
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()


def test_TC_03():

    values = ("Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance",
              "Dashboard", "Directory", "Maintenance", "Buzz")
    elements = driver.find_elements(By.XPATH, "//ul[@class='oxd-main-menu']/li/a//span")
    m = []
    for i in elements:
        m.append(i.text)
    print(len(values) == len(m))
    for val in values:
        if val in m:
            print(val + "\t--> Exist")
        else:
            print(val + "\t--> Not Exists")


def test_tearDown():
    driver.close()
