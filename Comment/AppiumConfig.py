import os
import subprocess
import time

from appium import webdriver

from Comment.DeviceInfo import DeviceInfo


class AppiumOperation():

    def start_appium(self):
        try:
            cmd = 'appium'
            subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
        except Exception as msg:
            errormsg = str(msg)
            return errormsg

    def stop_appium(self):
        end_appium_cmd = "ps -ef |grep appium |grep -v grep |awk '{print $2}' |xargs kill -9"
        os.popen(end_appium_cmd)


class AppiumConfig():

    def __init__(self, deviceId: str, appPackAge: str = None, appActivity: str = None):
        # AppiumOperation().start_appium()
        # time.sleep(4)
        self.deviceId = deviceId
        # time.sleep(6)
        self.desired_caps = {
            "platformName": "Android",
            "platformVersion": "10",
            "deviceName": "Android Emulator",
            "appPackage": appPackAge,
            "appActivity": appActivity,
            "noReset": True,
        }
        print(self.desired_caps)
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)

    def swipeUp(self, t=500, n=1):
        '''向上滑动屏幕'''

        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标

        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)


if __name__ == '__main__':
    # AppiumOperation().start_appium()
    #   {'package': 'com.jingdong.app.mall', 'activity': 'com.jingdong.app.mall.MainFrameActivity'}
    package = 'com.xiaomi.onetrackdemo'
    activity = 'com.xiaomi.onetrackdemo.TrackActivity'

    a = AppiumConfig(deviceId='a19908ae', appPackAge='com.mi.global.bbs',
                     appActivity='com.mi.global.bbs.ui.PrevSelectLanguageActivity')

    # a.swipeUp()
