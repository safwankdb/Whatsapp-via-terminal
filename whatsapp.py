from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import sys
opt=Options()
opt.add_argument("user-data-dir=" + os.path.dirname(sys.argv[0]))
web = webdriver.Chrome(chrome_options=opt)
time.sleep(5)
web.get('http://web.whatsapp.com')
print('Enter name of the victim')
name=input()
searchBar=web.find_element_by_class_name("_2MSJr")
searchBar.send_keys(name)
time.sleep(1)
elem1 = web.find_element_by_class_name("_1wjpf")
elem1.click()
print("Type your message below. Press Enter to send.")
message=input()
ElementTree = web.find_element_by_xpath("//div[@contenteditable='true']")
elem.send_keys(message)
web.find_element_by_class_name("_2lkdt").click()
print("Enter y to attach an image, enter anything else oterwise")
resp=input()
if resp=='y':
	attach = web.find_element_by_xpath("//div[@title='Attach']")
	attach.click()
	photoButton = web.find_elements_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/input')
	print("Enter image path")
	path=input()
	photoButton[0].send_keys(path)
	time.sleep(3)
	sendImage=web.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div/span');
	sendImage.click()
