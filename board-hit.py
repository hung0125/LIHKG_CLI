import seleniumMain as sm
from random import randrange as rr
from datetime import datetime as dt
from time import sleep

print('__連登純文字版 v1__')

sm.startChrome('https://lihkg.com/category/2','C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
sm.minimize()


while True:
    print(f'{"_"*47}即時熱門{"_"*47}')
    for i in range(1, 11):
        path_t = f'/html/body/div[1]/div[2]/div[1]/div[2]/div[{i}]/div/div[2]/div[2]/span'
        path_c = f'/html/body/div[1]/div[2]/div[1]/div[2]/div[{i}]/div/div[2]/a[2]'
        path_ago = f'/html/body/div[1]/div[2]/div[1]/div/div[{i}]/div/div[1]/div[2]/span[2]'
        path_cde = f'/html/body/div[1]/div[2]/div[1]/div/div[{i}]/div/div[2]/a[1]'

        sm.waitForEle('xpath', path_t, 20)
        title = sm.findEle('xpath', path_t)[0].text
        cat = sm.findEle('xpath', path_c)[0].text
        ago = sm.findEle('xpath', path_ago)[0].text
        code = sm.findEle('xpath', path_cde)[0].get_attribute('href').split('/')[-3]
        print(f'[{i}][{cat}][{ago}] {title} [code:{code}]')
    print(f'Updated as of {dt.now().strftime("%H:%M:%S")}\n{"_"*100}')
    sleep(rr(60, 121))
    sm.manage.delete_all_cookies()
    sleep(1)
    sm.manage.refresh()