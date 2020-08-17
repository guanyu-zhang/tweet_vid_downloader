#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import argparse
import sys

def openurl(url,home="https://twdown.net"):
        # CHROME_PATH = 'C:\Program Files (x86)\Google'
        WINDOW_SIZE = "1920,1080" # set the window size based on your screen 
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--window--size=%s" % WINDOW_SIZE)
        browser = webdriver.Chrome(options=chrome_options) 
        # browser.set_page_load_timeout(30)
        # browser.implicitly_wait(30)
        browser.get(home)               
        browser.find_element_by_xpath("/html/body/div[2]/div/center/form/div/input").send_keys(url)
        browser.find_element_by_class_name("btn.btn-primary.input-lg").click()
        # desired_capabilities = DesiredCapabilities.CHROME
        # desired_capabilities["pageLoadStrategy"] = "none"
        try: # catch exception when the given link does not include a vid url 
            browser.find_element_by_xpath("/html/body/div[2]/div/center/div[2]/div/div[3]/table")
        except Exception as e:
            browser.delete_all_cookies() # delete cookies to avoid browser crash
            browser.close()
            browser.quit()
            return
        max_size = 0
        max_link = ""
        for i in range(3):
            root = "/html/body/div[2]/div/center/div[2]/div/div[3]/table/tbody/tr[" + str(i + 1) + "]/td["
            size_xpath = root + "2]"
            link_xpath = root + "4]/a"
            size = browser.find_element_by_xpath(size_xpath)
            link = browser.find_element_by_xpath(link_xpath)
            link_attrs = browser.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;',link)
            try:
                size = eval(size.text.replace("x","*"))
            except Exception as e:
                max_link = link_attrs["href"]
                break
            if size >= max_size:
                max_size = size
                max_link = link_attrs["href"]
        browser.delete_all_cookies()
        browser.close()
        browser.quit()
        return max_link

parser = argparse.ArgumentParser(description="get vid_list of a user")
parser.add_argument("--user", "-u", help="twitter user name", type=str)
args = parser.parse_args()
file_name = args.user + "_vid_list.txt"
f = open("tweet_list.txt","r")
f_out = open(file_name,"w")
count = 1
for line in f:
    sys.stdout.write("checking No." + str(count) + " link\n")
    sys.stdout.flush()
    link = openurl(line[:-1])
    if link == None:
        pass
    else:
        f_out.write(link + "\n")
        f.flush()
    # print("checking No." + str(count) + " link")
    count += 1
f.close()
f_out.close()




