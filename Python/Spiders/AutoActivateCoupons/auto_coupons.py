from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time

import configparser
import os

abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)

config = configparser.ConfigParser()
config.read('config.cfg')

# create a new Firefox session
driver = webdriver.Chrome('C:/bin/chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()

if 'DeutschlandCard' in config:
   driver.get("https://www.deutschlandcard.de/login")

   # get the search textbox
   driver.find_element_by_css_selector('a.login-mode-link').click()
   time.sleep(0.21) # sleep otherwise recognize us as an bot

   card_number_field = driver.find_element_by_css_selector('input#text-field-cardNumber')
   password_field = driver.find_element_by_css_selector('div.pin-field input')
   card_number_field.clear()
   password_field.clear()

   card_number = config['DeutschlandCard']['CardNumber']
   password = config['DeutschlandCard']['Password']

   # enter search keyword and submit
   card_number_field.send_keys(card_number)
   time.sleep(0.21) # sleep otherwise recognize us as an bot
   password_field.send_keys(password)
   time.sleep(0.21) # sleep otherwise recognize us as an bot
   password_field.send_keys(Keys.RETURN)

   # just wait for login process done
   driver.find_element_by_css_selector('.o-profile-menu')


   driver.get('https://www.deutschlandcard.de/e-coupons-aktionen/e-coupons')

   driver.find_element_by_css_selector('section.o-cookie-layer .o-button').click()

   driver.implicitly_wait(1)

   coupons_button_fields = driver.find_elements_by_css_selector('button.o-button:not([disabled])')
   for coupons in coupons_button_fields:
      coupons.click()


if 'Payback' in config:
   # Payback

   card_number = config['Payback']['CardNumber']
   password = config['Payback']['Password']

   driver.get('https://www.payback.de/login')
   time.sleep(0.21) # sleep otherwise recognize us as an bot

   name_field = driver.find_element_by_css_selector('input[name="aliasTypePassName"]')
   name_field.clear()
   name_field.send_keys(card_number)

   pass_field = driver.find_element_by_css_selector('input[name="passwordName"]')
   pass_field.clear()
   pass_field.send_keys(password)
   
   time.sleep(0.2) # sleep otherwise recognize us as an bot
   pass_field.send_keys(Keys.RETURN)

   time.sleep(1.5) # sleep otherwise recognize us as an bot

   driver.get('https://www.payback.de/coupons')

   def select_shadow_element_by_css_selector():
      running_script = "return [...document.querySelector('pb-coupon-center').shadowRoot.querySelectorAll('pb-coupon')].map((obj) => obj.shadowRoot.querySelector('.offline .circle.not-activated')).filter(Boolean)"
      element = driver.execute_script(running_script)
      return element

   shadow_section = select_shadow_element_by_css_selector()
   while len(shadow_section) > 0:
      try:
         shadow_section[0].click()
      except ElementClickInterceptedException as exception:
         print('coupon not activated')
   print('coupons')

# close the browser window
driver.quit()