from selenium.webdriver.common.alert import Alert
from urllib.parse import urlparse
from libs.driverGetter import getDriver
import time

FMID = '아이디 입력'
FMPW = '비번 입력'

def get_page():
    driver = getDriver()
    url = 'https://www.fmkorea.com/'
    driver.get(url)
    return driver

def login(driver):
    # login
    driver.find_element_by_name('user_id').send_keys(FMID)
    driver.find_element_by_name('password').send_keys(FMPW)
    driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/form/button').click()
    time.sleep(1)
    return driver

def post_remove(driver):
    for j in range(2, 10):
        for i in range(1, 20):
            try:
                driver.get(f"https://www.fmkorea.com/index.php?act=dispMy_commentViewMyComment&page={j}")
                time.sleep(1)
                driver.find_element_by_xpath(f'//*[@id="N_"]/table/tbody/tr[{i}]/td[3]/div/a').click()  # 옛날 댓글 처리
                time.sleep(1)
                post_num = urlparse(driver.current_url).query[-10:]
                driver.find_element_by_xpath(f'//*[@id="comment_{post_num}"]/div[3]/a').click()
                time.sleep(1)
                Alert(driver).accept()
            except:
                print('?')
Open_state = get_page()
Login_state = login(Open_state)
post_remove(Login_state)
