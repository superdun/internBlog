from selenium import webdriver
import requests
from pyquery import PyQuery as pq
import re
import time
import dbORM as db


def getPost(driver):
    freshCount = 0
    while True:
        postSubject = driver.find_element_by_id('subject').text
        postUser = driver.find_element_by_tag_name('b').text
        postTime = driver.find_element_by_xpath(
            '//*[@id="tbOtherOptions"]/tbody/tr[1]/td[1]/b').text
        postContent = driver.find_element_by_id('mailContentContainer').text
        freshCount += 1

        db.session.merge(db.Users(name=postUser))
        db.session.commit()
        db.session.close()

        print '%d done' % freshCount
        is_next_disable = "normal" not in driver.find_element_by_id(
            'nextmail').get_attribute("type")
        if is_next_disable:
            driver.find_element_by_xpath(
                '//*[@id="mainmail"]/div[1]/div[2]/a[1]').click()
            try:
                is_last_post = driver.find_element_by_id('nextpage')
            except:
                is_last_post = True
            if is_last_post:
                break
            else:
                driver.find_element_by_id('nextpage').click()
                time.sleep(1)
                driver.find_elements_by_class_name('l')[0].click()
        else:
            driver.find_element_by_id('nextmail').click()
    print 'OK!!!'


driver = webdriver.PhantomJS()
driver.get('https://exmail.qq.com/login')
inputUsrname = driver.find_element_by_id('inputuin')
inputPsw = driver.find_element_by_id('pp')
inputUsrname.send_keys('lidun@wallstreetcn.com')
inputPsw.send_keys('Qw96163')
loginBtn = driver.find_element_by_id('btlogin')
loginBtn.click()
time.sleep(3)

driver.find_element_by_id('folder_1').click()
driver.switch_to_frame("mainFrame")

driver.find_elements_by_class_name('l')[0].click()
getPost(driver)
