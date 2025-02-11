from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager 
import sys
sys.path.append('C:/Users/vaibh/AppData/Local/Programs/Python/Python312/Lib/site-packages')
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def linkedin_login(email, password):
    # Set up WebDriver with ChromeDriverManager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # Open LinkedIn's login page
    driver.get('https://www.linkedin.com/login')
    
    # Locate email and password fields and enter credentials
    email_field = driver.find_element(By.ID, 'username')
    email_field.send_keys(email)
    
    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys(password)
    
    # Submit the login form
    password_field.send_keys(Keys.RETURN)
    
    # Wait for the login to complete
    time.sleep(5)
    return driver
