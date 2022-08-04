from random import random, seed
from selenium.webdriver.common.by import By


def generate_random_email():
    random_email = 'test{random_number}@gmail.com'.format(
        random_number=random())
    return random_email


def get_element_by_css_selector(driver, selector):
    return driver.find_element(By.CSS_SELECTOR, selector)


def generate_random_name_by_word():
    template = 'test{random}'.format(random=random())
    return template
