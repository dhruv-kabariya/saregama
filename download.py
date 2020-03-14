from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import os

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--verbose')
chrome_options.add_experimental_option("prefs", {
        "download.default_directory": "/Download",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
})
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-software-rasterizer')



f = open("songname.txt","r")
fail = open("fail.txt","w")
s = f.readlines()


driver = webdriver.Chrome(executable_path="chromedriver",chrome_options=chrome_options)

download_dir = "/Download"
for i in range(40):
    driver.get("https://www.google.com/search?q =" )

    wait = WebDriverWait(driver,10)
    wait.until(ec.presence_of_element_located((By.XPATH,"//input[@name='q']")))

    que=driver.find_element_by_xpath("//input[@name='q']")
    que.send_keys(s[i][:-2] + ' raag fm')
    que.send_keys(Keys.RETURN)
    # enable_download_headless(driver, download_dir)
    try:
        links = driver.find_elements(by=By.PARTIAL_LINK_TEXT,value="raag.fm")[0].click()
        wait.until(ec.presence_of_element_located((By.TAG_NAME,"button")))
        dow = driver.find_elements(by=By.TAG_NAME,value="button")[1]
    except:
        fail.write(s[i] + "\n")
        
# print(fail)
