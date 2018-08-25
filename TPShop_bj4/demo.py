from appium import webdriver

desired_caps = dict()
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'aa1ce00d'
# app信息
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = '.ui.LauncherUI'

desired_caps['automationName'] = 'Uiautomator2'

webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
