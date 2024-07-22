import sys
import codecs
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# executable_path="./chromedriver-mac-arm64/chromedriver"
driver = webdriver.Chrome()
driver.get("https://udndata.com/ndapp/Index?cp=udn")
driver.find_element(By.XPATH, """//*[@id="container"]/header/div[2]/ul/li[2]/a""").click()
k = 0
j = 0
while k <= 1303:
    k += 1
    driver.get("https://udndata.com/ndapp/Searchdec?udndbid=udndata&page=" + str(k) + "&SearchString=%C2%E5%C0%F8%2B%A4%E9%B4%C1%3E%3D20070101%2B%A4%E9%B4%C1%3C%3D20141231%2B%B3%F8%A7%4F%3D%C1%70%A6%58%B3%F8&sharepage=20&select=1&kind=2")
    myElem = WebDriverWait(driver, 8)
    link = driver.find_elements(By.CLASS_NAME, 'control-pic')
    b = ['apple']*20
    i = 0
    for a in link:
        b[i] = a.text
        i += 1
    #     a = a.find_element_by_xpath("//*[@href]")
    for c in b:
        j += 1
        driver.find_element(By.LINK_TEXT, c).click()
        myElem = WebDriverWait(driver, 5)
    #     print("Page is ready!")
        d = driver.find_element(By.CLASS_NAME, 'story-content')
        path = 'articles/' + str(j)+'.txt'
        sys.stdout = open(path,'wb')
        UTF8Writer = codecs.getwriter('utf8')
        sys.stdout = UTF8Writer(sys.stdout)
        print(d.text)
        driver.back()