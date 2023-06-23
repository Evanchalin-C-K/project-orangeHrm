import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

openJson = open("../test/json/readData.json")
readData = json.load(openJson)
openJson.close()

driver = webdriver.Chrome()


def test_pim_add():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.refresh()
    driver.maximize_window()
    driver.implicitly_wait(15)

    driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # add new employee

    driver.find_element(By.XPATH, "//ul[@class='oxd-main-menu']/li[2]").click()
    driver.find_element(By.XPATH, '//button[text()=" Add "]').click()
    driver.find_element(By.XPATH, "//input[@name='firstName']").send_keys(readData['Name'][0].get('FirstName'))
    driver.find_element(By.XPATH, "//input[@name='lastName']").send_keys(readData['Name'][0].get('LastName'))
    element = driver.find_element(By.XPATH, "//div[@class='oxd-form-row']/div[2]//input")
    element.send_keys(Keys.CONTROL + "a", Keys.DELETE)
    element.send_keys(readData['ID'])
    driver.find_element(By.XPATH, "// button[ @ type = 'submit']").click()
    time.sleep(5)


def test_TC_pim_02():
    # driver.refresh()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//a[text()='Employee List']").click()
    driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Type')]") \
        .send_keys(readData['Name'][0].get('FirstName'))
    driver.find_element(By.XPATH, '//button[text()=" Search "]').click()
    driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-pencil-fill']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//div[@class='oxd-form-row'][2]/child::div[2]//input") \
        .send_keys(readData["License_No"])
    driver.find_element(By.XPATH, "//div[@class='oxd-select-wrapper']/child::div//i").click()
    driver.find_element(By.XPATH, "//div[@class='oxd-date-input']/input").send_keys("2023-12-31")
    driver.execute_script("arguments[0].click()", (driver.find_element(By.XPATH, "//input[@value='2']")))

    driver.find_element(By.XPATH, "//div[@class='oxd-select-text-input']").click()
    driver.find_element(By.XPATH, "//span[text()='Indian']").click()
    driver.find_element(By.XPATH, "//div[@class='oxd-select-wrapper']/../following::div").click()
    driver.find_element(By.XPATH, "//span[text()='Married']").click()

    driver.find_element(By.XPATH, "//label[text()='Date of Birth']/../following::div//input").send_keys(readData["DOB"])

    driver.find_element(By.XPATH, "//div[@role='tablist']/div[6]/a").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//form[@class='oxd-form']/div/div/div[5]/div/div[2]//i").click()
    driver.find_element(By.XPATH, "//span[text()='Quality Assurance']").click()
    time.sleep(5)


def test_TC_pim_03_delete():
    driver.find_element(By.XPATH, "//a[text()='Employee List']").click()
    driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']") \
        .send_keys(readData['Name'][0].get('FirstName'))
    driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-trash']").click()


def test_tearDown():
    driver.quit()
