from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options # オプションを使うために必要
from datetime import datetime, timedelta, timezone
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.relative_locator import locate_with
import time
import datetime

#ヘッドレスモードで実行#
option = Options()                          # オプションを用意
#option.add_argument() # '--headless'           # ヘッドレスモードの設定を付与
#driver = webdriver.Chrome(r"C:/Users/t-oot/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
# タイムゾーンの生成

def MONDAY():
    driver.get("http://10.100.12.17:3000/playlists")
    driver.maximize_window()
    #曜日選択動作
    time.sleep(2)
    # ここにコピーしたselectorを入力する
    csss1 = '#reactRoot > div > main > div.css-nqt9pt > div > div.scrollbar-view > div > div.page-container.page-body > div:nth-child(2) > div > div > div.css-e3op7n > div > button > span'
    monday = driver.find_element(By.CSS_SELECTOR, csss1)
    monday.click()
    time.sleep(1)
    #AutoFit選択動作
    csss2 = 'body > div:nth-child(11) > div > div.css-mfszas > div.css-1ad80n9 > div.css-66nrdr-vertical-group > div:nth-child(2) > label > span.css-i7s5lk'
    monday2 = driver.find_element(By.CSS_SELECTOR, csss2)
    monday2.click()
    time.sleep(1)
    #Start動作
    csss3= 'body > div:nth-child(11) > div > div.css-mfszas > div.css-1ad80n9 > div.css-g4isi4 > div > div > button > span'
    monday3 = driver.find_element(By.CSS_SELECTOR, csss3)
    monday3.click()

def TUESDAY():
    driver.get("http://10.100.12.17:3000/playlists")
    driver.maximize_window()
    #曜日選択動作
    time.sleep(2)
    # ここにコピーしたselectorを入力する
    csss1 = '#reactRoot > div > main > div.css-nqt9pt > div > div.scrollbar-view > div > div.page-container.page-body > div:nth-child(3) > div > div > div.css-e3op7n > div > button > span'
    monday = driver.find_element(By.CSS_SELECTOR, csss1)
    monday.click()
    time.sleep(1)
    #AutoFit選択動作
    csss2= 'body > div:nth-child(11) > div > div.css-mfszas > div.css-1ad80n9 > div.css-66nrdr-vertical-group > div:nth-child(2) > label > span.css-i7s5lk'
    monday2 = driver.find_element(By.CSS_SELECTOR, csss2)
    monday2.click()
    time.sleep(1)
    #Start動作
    csss3= 'body > div:nth-child(11) > div > div.css-mfszas > div.css-1ad80n9 > div.css-g4isi4 > div > div > button > span'
    monday3 = driver.find_element(By.CSS_SELECTOR, csss3)
    monday3.click()

def WEDNESDAY():
    driver.get("http://10.100.12.17:3000/playlists")
    driver.maximize_window()
    #曜日選択動作
    time.sleep(2)
    csss1 = '#reactRoot > div > main > div.css-nqt9pt > div > div.scrollbar-view > div > div.page-container.page-body > div:nth-child(4) > div > div > div.css-e3op7n > div > button > span' #ここにコピーしたselectorを入力する
    monday = driver.find_element(By.CSS_SELECTOR, csss1)
    monday.click()
    time.sleep(1)
    #AutoFit選択動作
    csss2 = 'body > div:nth-child(11) > div > div.css-mfszas > div.css-1ad80n9 > div.css-66nrdr-vertical-group > div:nth-child(2) > label > span.css-i7s5lk'
    monday2 = driver.find_element(By.CSS_SELECTOR, csss2)
    monday2.click()
    time.sleep(1)
    #Start動作
    csss3= 'body > div:nth-child(11) > div > div.css-mfszas > div.css-1ad80n9 > div.css-g4isi4 > div > div > button > span'
    monday3 = driver.find_element(By.CSS_SELECTOR, csss3)
    monday3.click()

def THURSDAY():
    driver.get("http://10.100.12.17:3000/playlists")
    driver.maximize_window()
    #曜日選択動作
    time.sleep(2)
    csss1 = '#reactRoot > div > main > div.css-nqt9pt > div > div.scrollbar-view > div > div.page-container.page-body > div:nth-child(5) > div > div > div.css-e3op7n > div > button > span' #ここにコピーしたselectorを入力する
    monday = driver.find_element(By.CSS_SELECTOR, csss1)
    monday.click()
    time.sleep(1)
    #AutoFit選択動作
    csss2 = 'body > div:nth-child(11) > div > div.css-mfszas > div.css-1ad80n9 > div.css-66nrdr-vertical-group > div:nth-child(2) > label > span.css-i7s5lk'
    monday2 = driver.find_element(By.CSS_SELECTOR, csss2)
    monday2.click()
    time.sleep(1)
    #Start動作
    csss3= 'body > div:nth-child(11) > div > div.css-mfszas > div.css-1ad80n9 > div.css-g4isi4 > div > div > button > span'
    monday3 = driver.find_element(By.CSS_SELECTOR, csss3)
    monday3.click()

def FRIDAY():
    driver.get("http://10.100.12.17:3000/playlists")
    driver.maximize_window()
    #曜日選択動作
    time.sleep(2)
    csss1 = '#reactRoot > div > main > div.css-nqt9pt > div > div.scrollbar-view > div > div.page-container.page-body > div:nth-child(6) > div > div > div.css-e3op7n > div > button > span' #ここにコピーしたselectorを入力する
    monday = driver.find_element(By.CSS_SELECTOR, csss1)
    monday.click()
    time.sleep(1)
    #AutoFit選択動作
    csss2= 'body > div:nth-child(11) > div > div.css-mfszas > div.css-1ad80n9 > div.css-66nrdr-vertical-group > div:nth-child(2) > label > span.css-i7s5lk'
    monday2 = driver.find_element(By.CSS_SELECTOR, csss2)
    monday2.click()
    time.sleep(1)
    #Start動作
    csss3 = 'body > div:nth-child(11) > div > div.css-mfszas > div.css-1ad80n9 > div.css-g4isi4 > div > div > button > span'
    monday3 = driver.find_element(By.CSS_SELECTOR, csss3)
    monday3.click()

def ENV():
    driver.get("http://10.100.1.60:3000/d/fZqiZvT4k/huan-jing-datsushiyubodo2?orgId=1&refresh=10s&kiosk=tv")
    driver.maximize_window()
    time.sleep(20)
    driver.get("http://10.100.1.60:3000/d/8v0mAh1Vk/huan-jing-datsushiyubodo-xin-xi?orgId=1&refresh=10s&kiosk=tv")
    driver.maximize_window()
    time.sleep(20)
    driver.get("http://10.100.1.60:3000/d/fZqiZvT4k/huan-jing-datsushiyubodo-xian-tai?orgId=1&refresh=10s")
    driver.maximize_window()
    time.sleep(20)
    driver.get("http://10.100.1.60:3000/d/0FoWNyr4z/huan-jing-datsushiyubodo-xian-tai-b?orgId=1&refresh=10s")
    driver.maximize_window()
    time.sleep(20)

def HP():
    driver.get("https://www.read.co.jp/")
    driver.maximize_window()
    csss_hp = '#newsBox > div:nth-child(1) > h3 > a'
    hp = driver.find_element(By.CSS_SELECTOR, csss_hp)
    hp.click()
    time.sleep(1)
    #ページの高さを取得
    height = driver.execute_script("return document.body.scrollHeight")
    #最後までスクロールすると長いので、半分の長さに割る。
    height = height // 2
	#ループ処理で少しづつ移動
    for x in range(1,height):
        driver.execute_script("window.scrollTo(0, "+str(x)+");")
        time.sleep(0.05)
    time.sleep(10)


today = datetime.date.today()


if today.weekday() == 0:
    try:
        for i in range(10):
            MONDAY()
            time.sleep(600)
            ENV()
            time.sleep(120)
            HP()
    except Exception: pass
elif today.weekday() == 1:
    try:
        for i in range(10):
            TUESDAY()
            time.sleep(600)
            ENV()
            time.sleep(120)
            HP()
    except Exception: pass
elif today.weekday() == 2:
    try:
        for i in range(10):
            WEDNESDAY()
            time.sleep(600)
            ENV()
            time.sleep(120)
            HP()
    except Exception: pass
elif today.weekday() == 3:
    try:
        for i in range(10):
            THURSDAY()
            time.sleep(600)
            ENV()
            time.sleep(120)
            HP()
    except Exception: pass
elif today.weekday() == 4:
    try:
        for i in range(10):
            FRIDAY()
            time.sleep(600)
            ENV()
            time.sleep(120)
            HP()
    except Exception: pass
else: pass


driver.quit()
