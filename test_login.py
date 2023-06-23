import time
import pytest

import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wb = openpyxl.load_workbook("C:\\Users\\evanc\\Excel\\OrangeHrm.xlsx")
sheet = wb['Sheet1']


def test_setup():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()


def test_login_TC_01():
    driver.refresh()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys(sheet['B2'].value)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(sheet['B3'].value)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    driver.save_screenshot("TC_01.png")


def test_login_TC_02():
    driver.refresh()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys(sheet['C2'].value)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(sheet['C3'].value)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    driver.save_screenshot("TC_02.png")


def test_login_TC_03():
    driver.refresh()
    driver.implicitly_wait(10)
    driver.refresh()
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys(sheet['D2'].value)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(sheet['D3'].value)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    driver.save_screenshot("TC_03.png")
    driver.back()


def test_login_TC_04():
    driver.back()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys(sheet['E2'].value)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(sheet['E3'].value)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    driver.save_screenshot("TC_04.png")


def test_tearDown():
    driver.close()
