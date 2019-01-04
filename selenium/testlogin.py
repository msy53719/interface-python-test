#coding = UTF-8
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.action_chains import ActionChains

#jsImage = "window.document.getElementById('info').innerHTML='<input type=\"hidden\" name=\"isCheckImage\" value=\"false\">'"
#url="https://www.unicompayment.com/per"
profileDir = r"/Users/mosy/library/Application Support/Firefox/Profiles/1aq928hk.default"
profile = webdriver.FirefoxProfile(profileDir)
driver = webdriver.Firefox(profile)
driver.get('https://www.unicompayment.com/per')
driver.switch_to_frame("iframe")
driver.find_element_by_id("userid").send_keys("15886678949")
driver.fi
pwdtxt=driver.find_element_by_id("_ocx_password")
ActionChains(driver).send_keys_to_element(pwdtxt,"").perform()