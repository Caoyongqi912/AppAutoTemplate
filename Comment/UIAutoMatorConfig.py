import os

import uiautomator2 as U2
from Comment.Log import LogInfo

path = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class UI:
    """
    基类
    """

    def __init__(self, ip=None, deviceID=None):
        self.log = LogInfo()

        # try:
        #     cmd = "python -m uiautomator2 init"
        #     os.popen(cmd)
        # except Exception as e:
        #     print(str(e))

        if ip:
            self.d = U2.connect(ip)
        elif deviceID:
            self.d = U2.connect_usb(deviceID)
        else:
            self.log.error("请输入IP,或者插入设备")
            return

    def Get_DeviceInfo(self):
        """
        获取机器信息
        :return:  Dict
        {'currentPackageName': 'com.android.systemui',
        'displayHeight': 1344,
         'displayRotation': 0,
          'displaySizeDpX': 360,
           'displaySizeDpY': 720,
           'displayWidth': 720,
            'productName': 'rosy',
            'screenOn': False,
             'sdkInt': 27,
             'naturalOrientation': True}
        """
        try:
            return self.d.info
        except Exception as e:
            self.log.error(str(e))

    def Get_Current_App(self):
        """
        获取正在运行的appInfo
        :return:  {'package': 'com.jingdong.app.mall', 'activity': '.MainFrameActivity', 'pid': 7611}
        """
        try:
            return self.d.app_current()
        except Exception as e:
            self.log.error(str(e))

    def Get_AppInfo(self, pkg_name):
        """Get_AppInfo"""
        try:
            return self.d.app_info(pkg_name)
        except Exception as e:
            self.log.error(str(e))

    def Screen_Light(self, flag: bool):
        """
        开关屏幕
        :param flag: 1 开  2 关
        :return:
        """
        if flag:
            self.d.screen_on()
        else:
            self.d.screen_off()

    def Get_Size(self):
        """
        获取手机尺寸
        :return: (xx,xxx)
        """
        return self.d.window_size()

    def Strat_App(self, packageName, activity=None):
        """
        启动App
        :param app:
        :return:
        """
        try:
            self.d.app_start(package_name=packageName, activity=activity)
            self.log.info(f"{packageName}    启动成功")

        except Exception as e:
            self.log.error(f"{packageName}   启动失败")
            self.log.error(str(e))

    def Kill_App(self, packageName):
        """
        停止app
        :param packageName:
        :return:
        """
        try:
            self.d.app_stop(pkg_name=packageName)
            self.log.info(f"{packageName} 关闭成功")
        except Exception as e:
            self.log.error(f"{packageName} 关闭失败")
            self.log.error(str(e))

    def Install_App(self, url):
        try:
            self.d.app_install(url)
            self.log.info(f"    安装  {url}   成功")
        except Exception as e:
            self.log.error(f"    安装  {url}   失败")
            self.log.error(str(e))

    def Kill_All_App(self):
        """關閉所有app"""
        try:
            self.d.app_stop_all()
            self.log.info("关闭所有App")
        except Exception as e:
            self.log.error("关闭失败")
            self.log.error(str(e))

    def Press(self, *args):
        """
            key (str): on of
            ("home", "back", "left", "right", "up", "down", "center",
            "search", "enter", "delete", "del", "recent", "volume_up",
            "menu", "volume_down", "volume_mute", "camera", "power")
        """
        try:
            self.d.press(*args)
        except Exception as e:
            self.log.error(str(e))

    def Unlock(self):
        """解锁"""
        try:
            self.d.unlock()
            self.log.info("unclock")
        except Exception as e:
            self.log.error(str(e))

    def ScreenShot(self, name):
        """err pass"""
        try:
            self.d.screenshot(f"{path('PIC')}/{name}")

        except Exception as e:
            self.log.error(str(e))

    def _Find_Element(self, element):
        """
        根据具体需求查找元素,
        """
        try:
            if element[0] == 'resourceId':
                return self.d(resourceId=f"{element[1]}")
            elif element[0] == "text":
                return self.d(text=f"{element[1]}")
            elif element[0] == "description":
                return self.d(description=f"{element[1]}")
            elif element[0] == 'className':
                return self.d(className=f"{element[1]}")
            elif element[0] == 'index':
                return self.d(index=f"{element[1]}")
            elif element[0] == "xpath":
                return self.d.xpath(element[1])

            elif isinstance(element[0], float):
                return element
            else:
                self.log.error('传入元素错误')
                return None

        except Exception as e:

            self.log.error(f'无效的{element}')
            self.log.error(str(e))

    def Click(self, element: tuple):
        """点击"""
        try:
            ele = self._Find_Element(element)
            if isinstance(ele, tuple):
                self.d.click(ele[0], ele[1])
            else:
                ele.click()
            self.log.info(f'点击 {element}')

        except Exception as e:
            self.log.error(f'无效的{element}')
            self.log.error(str(e))

    def Double_Click(self, element, time=1):
        """双击 时间间隔默认1s 需传坐标"""
        try:
            ele = self._Find_Element(element)
            if isinstance(ele, tuple):
                self.d.double_click(ele[0], ele[1], time)
            else:
                ele.click(time)
            self.log.info(f'点击 {element}')

        except Exception as e:
            self.log.error(f'无效的{element}')
            self.log.error(str(e))

    def Lone_Click(self, element, time=3):
        """长点击 点击时间默认3s  需传坐标"""
        try:
            ele = self._Find_Element(element)
            if isinstance(ele, tuple):
                self.d.long_click(ele[0], ele[1], time)
            else:
                ele.click(time)
            self.log.info(f'点击 {element}')

        except Exception as e:
            self.log.error(f'无效的{element}')
            self.log.error(str(e))

    def Send_keys(self, element, text):
        """输入文本"""
        try:
            ele = self._Find_Element(element)
            print(ele)
            ele.clear_text()
            ele.set_text(text)
            self.log.info(f'對 {element} 录入信息 {text}')

        except Exception as e:
            self.log.error(f'无效的{element}')
            self.log.error(str(e))

    def Push(self, files, url):
        try:
            self.d.push(files, url)
        except Exception as e:
            self.log.error(str(e))

    def Pull(self, files, url):
        try:
            return self.d.pull(files, url)
        except Exception as e:
            self.log.error(str(e))

    def Toast(self, msg):
        """
        获取toast,
        msg 默认返回
        """
        try:
            return self.d.toast.get_message(5, 10, msg)
        except Exception as e:
            self.log.error(str(e))

    def Watcher(self, name: str, element: tuple):
        """
        """
        self.d.watcher(name).when(element)


if __name__ == '__main__':
    u = UI(deviceID="4b8a8dc27cf5")
    # {'package': 'com.jingdong.app.mall', 'activity': 'com.jingdong.app.mall.MainFrameActivity'}

    # u.Kill_App(packageName="com.jingdong.app.mall")
    # u.Press("left")
    # u.Click(("resourceId", "com.miui.home:id/icon_icon"))
    # u.Click(("xpath", '//*[@resource-id="com.miui.home:id/cell_layout"]/android.widget.RelativeLayout[1]'))
    # u.Send_keys(("resourceId", 'com.xiaomi.onetrackdemo:id/property_et_key'), 'hah')
    # u.d.toast.show("hello", 10)
    # print(u.Get_AppInfo('com.jingdong.app.mall'))
    # print(u.Toast('hello'))
    a = u.Get_Current_App()
    print(a)