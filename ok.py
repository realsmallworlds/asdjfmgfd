import tarfile
with tarfile.open('firefox-121.0.tar.bz2', 'r') as archive:
    archive.extractall()
import tarfile
with tarfile.open('geckodriver-v0.34.0-linux64.tar.gz', 'r') as archive:
    archive.extractall()

from tempmail import EMail
from urlextract import URLExtract
import time
import re
import random
import string
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import FirefoxOptions

def random_char(y):
  return ''.join(random.choice(string.ascii_letters) for x in range(y))
extractor = URLExtract()

binary = FirefoxBinary("./firefox/firefox")
opts = FirefoxOptions()
opts.add_argument("--headless")
opts.set_preference('detach', True)

i = 0
while i < 1:
    #try:
        email = EMail()
        name = random_char(5)
        name_2 = random_char(5)
        driver = webdriver.Firefox(executable_path="./geckodriver", firefox_binary=binary,options=opts)
        print("starting")
        wait = WebDriverWait(driver, 30)
        driver.get("https://myco.io/")

        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/nav/div/div[3]/button'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/span'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="firstName"]'))).send_keys(name)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lastName"]'))).send_keys(name_2)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]'))).send_keys(email.address)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="userName"]'))).send_keys(name)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]'))).send_keys("zxcasdqwe12!A")
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="confirmPassword"]'))).send_keys("zxcasdqwe12!A")
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="link-checkbox"]'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register-btn"]'))).click()
        time.sleep(5)
        msg = email.wait_for_message()
        myCode = msg.body
        link = (re.findall(r'(https?://auth.myco.io?.*\?.*?)\s', myCode))[0]
        link2 = extractor.find_urls(link)[0]
        driver.get(link2)
        #time.sleep(8)
        driver.get("https://myco.io/")
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/nav/div/div[3]/button'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/div/form/div[2]/div[2]/input'))).send_keys(name)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div/form/div[2]/div[3]/input'))).send_keys("zxcasdqwe12!A")
        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div[1]/div/form/div[2]/div[4]/button'))).click()
        time.sleep(8)
        driver.get("https://myco.io/videohome?v=64e459e5a9addef12597ac3a")
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div/div[1]/div/div[1]/div/video-js/button'))).click()
        print("done")
        time.sleep(3700)
    #except:
        print("error")
        driver.quit()
