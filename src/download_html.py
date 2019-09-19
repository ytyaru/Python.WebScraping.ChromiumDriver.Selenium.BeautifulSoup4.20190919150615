# 使い方: python3 URL 出力先HTMLパス
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import extractcontent3
import sys
import os


if len(sys.argv) < 2:
    raise Error('第1引数にURLパスを指定してください。')
    exit()
url = sys.argv[1]
path_html = sys.argv[2] if 2 < len(sys.argv) else '/tmp/work/index.html'

options = Options()
options.set_headless(True)
driver = webdriver.Chrome(chrome_options=options)
driver.get(url)
html = driver.page_source.encode('utf-8')
print(html)
soup = BeautifulSoup(html, "html.parser")

os.makedirs(os.path.dirname(path_html), exist_ok=True)
with open(path_html, mode='w') as f:
    f.write(str(html))

