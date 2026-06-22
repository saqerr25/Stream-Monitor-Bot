import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class StreamGuard:
    def __init__(self, email, password):
        self.driver = uc.Chrome()
        self.safe_list = []
        self.email = email
        self.password = password
        self.login()
    def login(self):
        self.driver.get("https://accounts.google.com/signin")
        self.driver.find_element(By.NAME, "identifier").send_keys(self.email + Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(By.NAME, "Passwd").send_keys(self.password + Keys.ENTER)
        time.sleep(5)
    def process(self, stream_url):
        if stream_url in self.safe_list:
            return "مستثنى"
def run_guard(url, bot_instance):
    driver = uc.Chrome()
    bot_instance.current_driver = driver # ربط المتصفح بالبوت
        self.driver.get(stream_url)
        time.sleep(5
        is_streamer = "owner" in self.driver.page_source.lower()
        msg = "تحذير: تم رصد محتوى مخالف."
        if is_streamer:
            msg += " If you didn't do anything and you think the bot sent this by mistake please sent 'no I didn't'"
        for i in range(4):
            try:
                chat_box = self.driver.find_element(By.ID, "input")
                chat_box.send_keys(msg + Keys.ENTER)
            except: pass
            time.sleep(10)
        try:
            self.driver.find_element(By.ID, "report-button-id").click()
        except: pass
        return "تمت المراقبة"
