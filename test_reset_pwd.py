import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def test_TC1_reset_pwd():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//div[contains(@class, 'forgot')]/p").click()
    textbox = driver.find_element(By.XPATH, "//input[@name='username']")
    print("\n Textbox visibility -> ", textbox.is_displayed())
    textbox.send_keys("evanchgladson")
    driver.find_element(By.XPATH, "//button[contains(@type, 'submit')]").click()
    time.sleep(5)
    driver.save_screenshot("reset_pwd.png")

def test_tearDown():
    driver.close()