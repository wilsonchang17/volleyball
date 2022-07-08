from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time, datetime
import os

class volleyballsnap2:
    def apply2(self, day,court,timeee, id, passwordd):
        print("start volleyball2 immidiately court")
        student_id = id
        password = passwordd
        court = court.lower()
        
        #option = webdriver.ChromeOptions()
        #option.add_argument("headless")
        
        op = webdriver.ChromeOptions()
        op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        op.add_argument("--headless")
        op.add_argument("--disable-dev-shm-usage")
        op.add_argument("--no-sandbox")
        browser =  webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=op)
        
        #browser = webdriver.Chrome("D:/google_download/chromedriver_win32/chromedriver.exe")
        browser.get('https://sys.ndhu.edu.tw/gc/sportcenter/SportsFields/login.aspx')

        #帳號
        std_id = browser.find_element_by_xpath('//*[@id="MainContent_TextBox1"]')
        std_id.send_keys(student_id)
        #密碼
        passwordd= browser.find_element_by_xpath('//*[@id="MainContent_TextBox2"]')
        passwordd.send_keys(password)
        #登入
        
        browser.find_element_by_xpath('//*[@id="MainContent_Button1"]').click()
        

        #案新增申請
        try:
            browser.find_element_by_xpath('//*[@id="MainContent_Button2"]').click()
        except:
            browser.close()
            browser.quit()
            return "帳號或密碼錯誤"
        #場
        time.sleep(0.5)
        if court == 'a':
            browser.find_element_by_xpath('//*[@id="MainContent_DropDownList1"]/option[24]').click()
        elif court == 'b':
            browser.find_element_by_xpath('//*[@id="MainContent_DropDownList1"]/option[25]').click()
        elif court == 'c':
            browser.find_element_by_xpath('//*[@id="MainContent_DropDownList1"]/option[26]').click()
        elif court == 'd':
            browser.find_element_by_xpath('//*[@id="MainContent_DropDownList1"]/option[27]').click()
        elif court == 'e':
            browser.find_element_by_xpath('//*[@id="MainContent_DropDownList1"]/option[28]').click()
        elif court == 'f':
            browser.find_element_by_xpath('//*[@id="MainContent_DropDownList1"]/option[29]').click()
        elif court == 'j':
            browser.find_element_by_xpath('//*[@id="MainContent_DropDownList1"]/option[30]').click()
        else:
            browser.close()
            browser.quit()
            return "場地錯誤"
        
        js = "$('input').removeAttr('readonly')"
        browser.execute_script(js)
        input_datetime = browser.find_element_by_xpath('//*[@id="MainContent_TextBox1"]')
        input_datetime.clear()
        input_datetime.send_keys(day)
        browser.find_element_by_xpath('//*[@id="MainContent_Button1"]').click()
        #input_datetime.click()
        
   

        timee = timeee

        #更改時間
        t = 0
        #print(start)
        ntime = time.time()
        while True:
            etime = time.time()
            gap = etime - ntime
            #t = t+1
            if gap > 3:
                print ("按下查詢")
                browser.find_element_by_xpath('//*[@id="MainContent_Button1"]').click()
                break

        #browser.find_element_by_xpath('//*[@id="MainContent_Button1"]').click()
        
        time.sleep(0.5)
        #時段
        for i in range(6,23):
            if str(timee) == str(i):
                try:
                    browser.find_element_by_xpath('//*[@id="MainContent_Table1"]/tbody/tr['+str(i-3)+']/td[2]/button').click()
                    print("按下時段場地")
                    break
                except Exception as e:
                    browser.close()
                    browser.quit()
                    return "時段無法借用"

        #理由
        try:
            reason = browser.find_element_by_xpath('//*[@id="MainContent_ReasonTextBox1"]')
            reason.send_keys("1")
        except:
            browser.close()
            browser.quit()
            print("同系有人借到了")
            return("可能同系有人借到了")
        #送出
        time.sleep(0.5)
        browser.find_element_by_xpath('//*[@id="MainContent_Button4"]').click()
        print("done")
        browser.close()
        browser.quit()
        return("成功")
     

#temp = volleyballsnap()
#temp.apply("2022/05/20","e","7","410821312", "Ww34087697")

