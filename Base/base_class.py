import datetime
from tkinter.font import names


class Bases():
    def __init__(self, driver):
        self.driver = driver

    """Method Get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url "+ get_url)

    """Method assert world"""

    def assert_world(self, world, result):
        value_world = world.text
        assert value_world == result
        print("good value world")

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot_' + now_date + '.png'
        path = 'C:\\Users\\sD\\PycharmProjects\\Automation project\\Screen\\' + name_screenshot
        self.driver.save_screenshot(path)
        print(f"Скриншот сохранён: {path}")
