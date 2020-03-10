import os
import subprocess
import time

from appium import webdriver

from Comment.DeviceInfo import DeviceInfo


class AppiumOperation():

    def start_appium(self):
        try:
            cmd = 'nohup /home/mi/Appium/Appium-linux-1.13.0.AppImage > a.info_log 2>&1&'
            subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
        except Exception as msg:
            errormsg = str(msg)
            return errormsg

    def stop_appium(self):
        end_appium_cmd = "ps -ef |grep appium |grep -v grep |awk '{print $2}' |xargs kill -9"
        os.popen(end_appium_cmd)


class AppiumConfig():

    def __init__(self, deviceId: str, appPackAge: str = None, appActivity: str = None):
        AppiumOperation().start_appium()
        self.deviceId = deviceId
        time.sleep(6)
        self.desired_caps = {
            "PlatFormName": "Android",
            "PlatFormVersion": DeviceInfo().getAndroidVersion(device_id=self.deviceId),
            "DeviceName": self.deviceId,
        }
        print(self.desired_caps)
        self.driver = webdriver.Remote("http:127.0.0.1:4723/wd/hub", self.desired_caps)


if __name__ == '__main__':
    # AppiumOperation().start_appium()
    AppiumConfig(deviceId='4b8a8dc27cf5')
