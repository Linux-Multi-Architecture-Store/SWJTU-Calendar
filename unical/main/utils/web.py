import asyncio
import pyppeteer
import requests
import platform

# from .CaptchaRecognition import captcha as captcha_ocr

cookie = None


def _get_options():
    os = platform.system()
    if os == "Linux":
        opt = {
            'handleSIGINT': False,
            'handleSIGTERM': False,
            'handleSIGHUP': False,
            'headless': True,
            "devtools": False,
            "executablePath": "/usr/bin/x-www-browser",
            "args": [
                '--window-size=1280,720'
            ],
            'defaultViewport': {"width": 1280, "height": 720}
        }
    else:
        opt = {
            'handleSIGINT': False,
            'handleSIGTERM': False,
            'handleSIGHUP': False,
            'headless': True,
            "devtools": False,
            "args": [
                '--window-size=1280,720'
            ],
            'defaultViewport': {"width": 1280, "height": 720}
        }

    return opt


async def main(username: str, password: str):
    """

    :param username: 用户名
    :type username: str
    :param password: 密码
    :type password: str
    :return: Coroutine[Any, Any, None]
    """
    browser = await pyppeteer.launch(_get_options())
    page = await browser.newPage()
    # 首页登录功能已失效！
    # await page.goto("http://jwc.swjtu.edu.cn/service/login.html")
    await page.goto(
        "https://cas.swjtu.edu.cn/authserver/login?service=http%3A%2F%2Fjwc.swjtu.edu.cn%2Fvatuu%2FUserLoginForWiseduAction")
    # await page.waitFor(3 * 1000)  # 等待10秒看看验证码长什么样
    # captcha = await page.waitForSelector('#randomPhoto img')  # 通过css selector定位验证码元素
    # await captcha.screenshot({'path': '/tmp/captcha.png'})  # 注意这里用的是ele.screenshot方法与教程1 page.screenshot是不同的
    # captcha_text = captcha_ocr("/tmp/captcha.png")

    await page.type("#username", username)
    await page.type("#password", password)
    # await page.type("#ranstring", str(captcha_text))
    await page.click("#login_submit")

    await page.waitFor(15 * 1000)
    global cookie
    cookie = await page.cookies()
    await browser.close()


async def get_cookie(username, password):
    await main(username=username, password=password)
    return cookie


"""
[{'name': 'username', 'value': '2021110181', 'domain': 'jwc.swjtu.edu.cn', 'path': '/', 'expires': 1665748852.774616, 'size': 18, 'httpOnly': False, 'secure': False, 'session': False}, {'name': 'Hm_lpvt_87cf2c3472ff749fe7d2282b7106e8f1', 'value': '1663156852', 'domain': '.jwc.swjtu.edu.cn', 'path': '/', 'expires': -1, 'size': 50, 'httpOnly': False, 'secure': False, 'session': True}, {'name': 'Hm_lvt_87cf2c3472ff749fe7d2282b7106e8f1', 'value': '1663156852', 'domain': '.jwc.swjtu.edu.cn', 'path': '/', 'expires': 1694692852, 'size': 49, 'httpOnly': False, 'secure': False, 'session': False}, {'name': 'JSESSIONID', 'value': 'FFFD9FF63EEC80C282E8CC72A193E0A3', 'domain': 'jwc.swjtu.edu.cn', 'path': '/', 'expires': -1, 'size': 42, 'httpOnly': True, 'secure': False, 'session': True}]

"""


def get_class_table(cookies, week):
    my_cookie = ""
    for each in cookies:
        my_cookie += each['name']
        my_cookie += "="
        my_cookie += each['value']
        my_cookie += "; "

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": my_cookie
    }

    data = {
        "setAction": "userCourseScheduleTable",
        "viewType": "studentCourseTableWeek",
        "selectTableType": "ThisTerm",
        "queryType": "student",
        "weekNo": week
    }
    url = "http://jwc.swjtu.edu.cn/vatuu/CourseAction"
    res = requests.post(url=url, data=data, headers=headers)
    print("[ info ] Get table: ", week)
    return res.text
