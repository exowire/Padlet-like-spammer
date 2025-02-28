#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

def load_all_posts(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def like_all_posts():
    url = "https://padlet.com/dsuljkanovic/was-ist-aufkl-rung-a3fvf8c12qkbt6vu"
    
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=192,108")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    count = 0  # Durchlaufzähler
    
    while True:
        driver = webdriver.Chrome(options=chrome_options)
        
        try:
            driver.get(url)
            
            WebDriverWait(driver, 10).until(
                lambda d: d.find_element(By.ID, "app").get_attribute("innerHTML") != ""
            )
            
            time.sleep(1)
            load_all_posts(driver)

            while True:
                like_buttons = driver.find_elements(By.XPATH, "//button[@aria-label='Post liken']")
                
                if not like_buttons:
                    break
                
                for btn in like_buttons:
                    try:
                        driver.execute_script("arguments[0].click();", btn)
                        
                        confirm_buttons = driver.find_elements(By.XPATH, "//button[@title='Fertig']")
                        if confirm_buttons:
                            driver.execute_script("arguments[0].click();", confirm_buttons[0])
                    except:
                        pass
                
                time.sleep(0.3)
            
            driver.quit()
            count += 1
            print(f"Durchlauf abgeschlossen: {count}")
            time.sleep(1)

        except:
            driver.quit()
            time.sleep(2)

if __name__ == "__main__":
    like_all_posts()
