import requests
from bs4 import BeautifulSoup
import time
import streamlit as st
import csv
import pandas as pd
import re
import lxml
import re
from lxml import html
import datetime
import selenium
from shutil import which
import os, sys
import numpy as np
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import win32clipboard
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
firefoxOptions = Options()
FIREFOXPATH = which("firefox")
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
firefoxOptions.add_argument(f'user-agent={user_agent}')
firefoxOptions.add_argument('--headless')
firefoxOptions.add_argument('--no-sandbox')
firefoxOptions.add_argument("--window-size=1920,1080")
firefoxOptions.add_argument('--disable-dev-shm-usage')
firefoxOptions.add_argument('--ignore-certificate-errors')
firefoxOptions.add_argument('--allow-running-insecure-content')
firefoxOptions.binary = FIREFOXPATH

path = os.getcwd()
st.write(path)

@st.experimental_singleton
def installff():
  os.system('sbase install geckodriver')
  os.system('ln -s /home/appuser/venv/lib/python3.9/site-packages/seleniumbase/drivers/geckodriver /home/appuser/venv/bin/geckodriver.exe')

_ = installff()

url = 'https://miro.com/login/'

st.title('Create Miro table APP')
st.subheader("Box for input user's name and surname")
test_name = st.text_input('Fill this rows (name and surname)')
button_pass = st.button('Click for start running app')
if button_pass:
  st.write(test_name)
  browser = webdriver.Firefox(executable_path=r'/home/appuser/venv/bin/geckodriver.exe', options = firefoxOptions)
  browser.implicitly_wait(7)
  browser.get(url)
  time.sleep(4)
  # logging
  email = 'aleksandra.gu+1@miro.com'
  password = '12112v12pole'
  em = browser.find_element(By.XPATH, "//input[@name = 'email']")
  em.send_keys(email)
  time.sleep(3)
  ps = browser.find_element(By.XPATH, "//input[@name = 'password']")
  ps.send_keys(password)
  time.sleep(3)
  submit = browser.find_element(By.XPATH, "//button[@class = 'signup__submit']").click()
  time.sleep(4)
  st.write('I logging')
  # check table for duplicate
  check_table =  browser.find_element(By.XPATH,"//div[@class = 'icon-3JFhr']")#.click()
  browser.execute_script("arguments[0].click();", check_table)
  time.sleep(1)
  duplicate =  browser.find_element(By.XPATH, "//div[@data-testid = 'duplicate_board_action']").click()
  time.sleep(1)
  # test_name = 'trial_browser_100'
  window_before = browser.window_handles[0]
  name_of_table =  browser.find_elements(By.XPATH, "//input[@data-testid = 'duplicate-modal__name-input']")[-1]
  name_of_table.clear()
  name_of_table.send_keys(test_name)
  submit_copy =  browser.find_element(By.XPATH,"//button[@class = 'button-3p1cD button_theme_primary-3hdLu button_size_m-bCnJ5 button_view_default-1hW6w button_round_default-1Bh_c']").click()
  time.sleep(2)
  window_after = browser.window_handles[1]
  # edit setting of dashboard
  browser.switch_to.window(window_after)
  time.sleep(15)
  st.write('I create table')
  miro_url = browser.current_url
  share_but = browser.find_element(By.XPATH, "//div[@data-id = 'permissionPanel']").click()
  time.sleep(1)
  to_edit_but = browser.find_element(By.XPATH, "//button[@data-testid = 'public-access__select-button']").click()
  time.sleep(0.5)
  edit_share = browser.find_element(By.XPATH,  "//button[@data-testid = 'board-sharing-options-edit']").click()
  time.sleep(2)
  save_share = browser.find_element(By.XPATH, "//a[@data-testid = 'shareMdButtonManageAccess']").click()
  save_share_1 =  browser.find_element(By.XPATH, "//button[@data-testid = 'board-access-modal__submit-button']").click()
  # get link for users
  time.sleep(2)
  browser.switch_to.window(window_before)
  time.sleep(2)
  check_table_for_copy_link =  browser.find_element(By.XPATH,"//div[@class = 'icon-3JFhr']").click()
  time.sleep(1)
  duplicate_link =  browser.find_element(By.XPATH,"//div[@data-testid = 'copy_link_board_action']").click()
  time.sleep(1)
  win32clipboard.OpenClipboard()
  head_links = win32clipboard.GetClipboardData()
  win32clipboard.CloseClipboard()
  browser.quit()
  st.write(f"It's your url for work in Miro dashboard - {head_links}")
  time.sleep(120)
