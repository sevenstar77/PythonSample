from selenium import webdriver
from bs4 import BeautifulSoup


#your chromedriver.exe path
#driver = webdriver.Chrome('c:\\git\\auth\\chromedriver')
driver = webdriver.Chrome('/Users/1/Documents/auth/chromedriver')
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login')

driver.find_element_by_name('id').send_keys('your ID')
driver.find_element_by_name('pw').send_keys('your password')

#driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

driver.get('https://section.cafe.naver.com/')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
