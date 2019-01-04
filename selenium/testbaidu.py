# coding=utf-8
#from selenium import webdriver

#profileDir = r"/Users/mosy/library/Application Support/Firefox/Profiles/1aq928hk.default"
#profile = webdriver.FirefoxProfile(profileDir)
#self = webdriver.Firefox(profile)
#self.get("http://g.10086.cn/")
# self.find_element_by_tag_name(u'登录').click()
#self.find_element_by_class_name('log_lk').click()
# self.get("http://www.baidu.com/")
# self.find_element_by_id("kw").send_keys(u"火狐")
# self.find_element_by_id("su").click()
# self.maximize_window()
# self.find_element_by_link_text("登录").click()
# self.find_element_by_id("TANGRAM__PSP_8__userName").send_keys('123456')
def test(num):
    sum=0
    for n in num:
        sum+=n*n;
    return sum

print test([1,2,3])

def testx(m=5,*args,**kw):
    sum=0
    for n in range(m):
        sum+=n*n
    return sum

print(testx(6))