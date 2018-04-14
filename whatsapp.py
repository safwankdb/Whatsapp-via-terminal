from selenium import webdriver
import time
web = webdriver.Chrome()
web.get('http://web.whatsapp.com')
time.sleep(10)
print('Enter name of the victim')
name="'"+input()+"'"
elem = web.find_element_by_xpath("//span[@title={name}]".format(name=name))
elem.click()
elem1 = web.find_element_by_xpath("//div[@contenteditable='true']")
for i in range(1,1000):
    elem1.send_keys(i)
    elem1.send_keys('\n')
elem1.send_keys('\nYou are being spammed by my python bot bitch')
web.find_element_by_class_name("_2lkdt").click()
