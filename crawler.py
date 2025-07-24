import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def login(URL, EMAIL, PASS):
    #initialize webdriver and launch
    global driver
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.get(URL)
    #sign in to monday
    email_box = driver.find_element(By.ID, "user_email")
    password_box = driver.find_element(By.ID, "user_password")
    sign_in = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div/div[4]/div/button")
    email_box.send_keys(EMAIL)
    password_box.send_keys(PASS)
    sign_in.click()

def getInvoiceURL():
    global driver
    menu_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[3]/div/div/main/div/div/div/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td[5]/button")
 #   view_invoice = driver.find_element(By.TAG_NAME, "ul")
    menu_button.click()
    view_invoice = driver.find_element(By.XPATH, '//*[@id="menu-0"]')
    view_invoice.click()
    time.sleep(4)
    original_window = driver.current_window_handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    return driver.current_url
