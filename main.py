# Usando RPA, hacer dos procesos:
#  1) El primero:
#     a) Entrar a gmail.
#     b) Crear un correo
#     c) Adjuntar un archivo.
#     d) Luego enviarlo.

from dotenv import load_dotenv

load_dotenv()

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import utils
import pyautogui
import os

options = webdriver.ChromeOptions()

driver_path = 'C:\\Users\\JHONAS\\Documents\\APEC-20220124T004744Z-001\\APEC\\Cuatrimestre 10\\Calidad\\automatize_task_1\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

driver.get("https://outlook.live.com/owa/")

login_button_xpath = "//a[@data-task='signin']"
login_button = driver.find_element(By.XPATH, login_button_xpath)
login_button.click()
# -----------------------------------------------------------
email_input_selector = 'input.form-control ltr_override input ext-input text-box ext-text-box'.replace(
    ' ', '.')
email_input = utils.get_element_by_css_selector(driver, email_input_selector)
email_input.send_keys(os.environ['EMAIL'])

next_button_selector = 'input.win-button button_primary button ext-button primary ext-primary'.replace(
    ' ', '.')
next_button = utils.get_element_by_css_selector(driver, next_button_selector)
next_button.click()

time.sleep(2)

password_input_id = 'i0118'
password_input = driver.find_element(By.ID, password_input_id)
password_input.send_keys(os.environ['PASSWORD'])

sign_in_button_id = 'idSIButton9'
sign_in_button = driver.find_element(By.ID, sign_in_button_id)
sign_in_button.click()

time.sleep(2)

yes_button_selector = "input.win-button button_primary button ext-button primary ext-primary".replace(
    ' ', '.')
yes_button = utils.get_element_by_css_selector(driver, yes_button_selector)
yes_button.click()

time.sleep(2)

new_email_button_selector = "button.ms-Button m2Lea b4BZP ms-Button--commandBar UhijP root-174".replace(
    ' ', '.')
new_email_button = utils.get_element_by_css_selector(
    driver, new_email_button_selector)
new_email_button.click()

time.sleep(1)

to_input_selector = "input.ms-BasePicker-input pickerInput_9f838726".replace(
    ' ', '.')
to_input = driver.find_element(By.CSS_SELECTOR, to_input_selector)
to_input.send_keys("jhonas724@gmail.com")

time.sleep(1)

subject_input_xpath = "//input[@placeholder='Add a subject']"
subject_input = driver.find_element(By.XPATH, subject_input_xpath)
subject_input.send_keys("Prueba RPA")

time.sleep(1)

pyautogui.click('./images/attach_button.png')

time.sleep(1)

pyautogui.click('./images/browse_this_computer.png')

time.sleep(1)

pyautogui.click('./images/folder_quickaccess.png')

time.sleep(1)

pyautogui.click('./file_tab.png')

time.sleep(1)

pyautogui.press('enter')

time.sleep(3)

pyautogui.click('./images/send_button.png')
# pyautogui.click('./images/send_button_2.png')
