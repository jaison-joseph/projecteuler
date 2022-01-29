from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def run():
    search_bar_id = '//*[@id="side"]/div[1]/div/label/div/div[2]'
    chat_id = '//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]'
    driver = webdriver.Firefox()
    driver.get("http://web.whatsapp.com")
    sleep(7)
    search_bar = driver.find_element_by_xpath(search_bar_id)
    search_bar.send_keys("huuhuu")      # the name of contact in whatsapp
    search_bar.send_keys(Keys.ENTER)      # the name of contact in whatsapp
    chat_box = driver.find_element_by_xpath(chat_id)

    # the number of times to send message
    for i in range(1000):
        chat_box.send_keys("okay")
        chat_box.send_keys(Keys.ENTER)
run()
