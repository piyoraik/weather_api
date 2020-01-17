import requests
import json
import schedule
import time
from datetime import datetime
import pymysql
import datetime

def osaka():
    url = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1?city=270000')
    date = json.loads(url.text)
    getapi(date)

def tokyo():
    url = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1?city=130010')
    date = json.loads(url.text)
    getapi(date)

def hokkaido():
    url = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1?city=016010')
    date = json.loads(url.text)
    getapi(date)

def okinawa():
    url = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1?city=471010')
    date = json.loads(url.text)
    getapi(date)

def nigata():
    url = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1?city=150010')
    date = json.loads(url.text)
    getapi(date)

def asahikawa():
    url = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1?city=012010')
    date = json.loads(url.text)
    getapi(date)

def kumagaya():
    url = requests.get('http://weather.livedoor.com/forecast/webservice/json/v1?city=110020')
    date = json.loads(url.text)
    getapi(date)

def getapi(date):

    timen = datetime.datetime.fromtimestamp(time.time())
    timenow = timen.strftime('%Y-%m-%d %H:%M:%S')
   	
    city = date['location']['city']
    
    timedate = date['forecasts'][1]['date']
    
    image = date["forecasts"][1]["image"]["url"]
    
    weather = date["forecasts"][1]["telop"]
    
    if date["forecasts"][1]["temperature"]["min"]["celsius"]  == None:
        minw = None
    else:
        minw = date["forecasts"][1]["temperature"]["min"]["celsius"]
    
    if not date["forecasts"][1]["temperature"]["max"]["celsius"] == None:
        maxw = date["forecasts"][1]["temperature"]["max"]["celsius"] 
    else:
        maxw = None
    
    textw = date["description"]["text"]

    
    dateset = set()
    for list in date:
        dateset.add((timenow,city,timedate,image,weather,minw,maxw,textw))

    
    connect = pymysql.connect(host="35.223.82.174",
                         port=3306,
                         user='root',
                         password='heptad8002reform',
                         db='python')
    cursor = connect.cursor()
    sql = 'INSERT INTO weather VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
    cursor.executemany(sql, dateset)
    connect.commit()
    connect.close()

schedule.every().day.at('06:00').do(osaka)
schedule.every().day.at('06:01').do(tokyo)
schedule.every().day.at('06:02').do(hokkaido)
schedule.every().day.at('06:03').do(okinawa)
schedule.every().day.at('06:04').do(nigata)
schedule.every().day.at('06:05').do(asahikawa)
schedule.every().day.at('06:06').do(kumagaya)


schedule.every().day.at('09:00').do(osaka)
schedule.every().day.at('09:01').do(tokyo)
schedule.every().day.at('09:02').do(hokkaido)
schedule.every().day.at('09:03').do(okinawa)
schedule.every().day.at('09:04').do(nigata)
schedule.every().day.at('09:05').do(asahikawa)
schedule.every().day.at('09:06').do(kumagaya)

schedule.every().day.at('12:00').do(osaka)
schedule.every().day.at('12:01').do(tokyo)
schedule.every().day.at('12:02').do(hokkaido)
schedule.every().day.at('12:03').do(okinawa)
schedule.every().day.at('12:04').do(nigata)
schedule.every().day.at('12:05').do(asahikawa)
schedule.every().day.at('12:06').do(kumagaya)

schedule.every().day.at('15:00').do(osaka)
schedule.every().day.at('15:01').do(tokyo)
schedule.every().day.at('15:02').do(hokkaido)
schedule.every().day.at('15:03').do(okinawa)
schedule.every().day.at('15:04').do(nigata)
schedule.every().day.at('15:05').do(asahikawa)
schedule.every().day.at('15:06').do(kumagaya)

schedule.every().day.at('18:00').do(osaka)
schedule.every().day.at('18:01').do(tokyo)
schedule.every().day.at('18:02').do(hokkaido)
schedule.every().day.at('18:03').do(okinawa)
schedule.every().day.at('18:04').do(nigata)
schedule.every().day.at('18:05').do(asahikawa)
schedule.every().day.at('18:06').do(kumagaya)

schedule.every().day.at('21:00').do(osaka)
schedule.every().day.at('21:01').do(tokyo)
schedule.every().day.at('21:02').do(hokkaido)
schedule.every().day.at('21:03').do(okinawa)
schedule.every().day.at('21:04').do(nigata)
schedule.every().day.at('21:05').do(asahikawa)
schedule.every().day.at('21:06').do(kumagaya)

schedule.every().day.at('22:00').do(osaka)
schedule.every().day.at('22:01').do(tokyo)
schedule.every().day.at('22:02').do(hokkaido)
schedule.every().day.at('22:03').do(okinawa)
schedule.every().day.at('22:04').do(nigata)
schedule.every().day.at('22:05').do(asahikawa)
schedule.every().day.at('22:06').do(kumagaya)

while True:
    schedule.run_pending()
    time.sleep(1)
