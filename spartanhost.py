from urllib import request
import re
import telegram
baseurl="https://billing.spartanhost.net/"
url = "https://billing.spartanhost.net/cart.php?gid=8"
header={'Host': 'billing.spartanhost.net',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests':'1',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Cache-Control': 'max-age=0',
'TE': 'trailers'
}
#pattern1=re.compile(r"AMD Ryzen 7 5800X.+\n<span class=\"qty\">\n(.+)Available\n",re.MULTILINE|re.DOTALL)
#pattern1=re.compile(r'Dual Intel Xeon L5520.+?([0-9]{1,3}) Available.+?<a href="(.+?)"',re.MULTILINE|re.DOTALL)
#pattern2=re.compile(r'Dual Intel Xeon L5630.+?([0-9]{1,3}) Available.+?<a href="(.+?)"',re.MULTILINE|re.DOTALL)
#pattern3=re.compile(r'Intel Xeon E3-1230 v2.+?([0-9]{1,3}) Available.+?<a href="(.+?)"',re.MULTILINE|re.DOTALL)
pattern1=re.compile(r'Dual Intel Xeon L5520.+?<a href="(.+?)"',re.MULTILINE|re.DOTALL)
pattern2=re.compile(r'Dual Intel Xeon L5630.+?<a href="(.+?)"',re.MULTILINE|re.DOTALL)
pattern3=re.compile(r'Intel Xeon E3-1230 v2.+?<a href="(.+?)"',re.MULTILINE|re.DOTALL)
bot=telegram.Bot("")
print("Start My Monitoring")
#status=bot.send_video(chat_id="@RestockBot",video=open("/home/silence/Videos/鲨臂.mp4",'rb'))
while True:
    req=request.Request(url,headers=header)
    page=request.urlopen(req).read()
    text=page.decode()
    f=open('./spartanhost.txt','w')
    f.write(text)
    f.close()
    m1=pattern1.search(text)
    m2=pattern2.search(text)
    m3=pattern3.search(text)
    #m1=re.search('AMD Ryzen 7 5800X.*Available',page.decode())
    #print(m1.group())
    if m1!= None:
        tmp=re.search(r'([1-9]{1,3}) Available',m1.group())
        if tmp!=None:
            print('Dual Intel Xeon L5520 %s Available link : %s\r\n' %(tmp.group(1),baseurl+m1.group(1)))
            status=bot.send_message(chat_id="@RestockBot",text='Dual Intel Xeon L5520 %s Available link : %s\r\n' %(tmp.group(1),baseurl+m1.group(1)))
    if m2!=None:
        tmp=re.search(r'([1-9]{1,3}) Available',m2.group())
        if tmp!=None:
            print('Dual Intel Xeon L5630 %s Available link : %s\r\n' %(tmp.group(1),baseurl+m2.group(1)))
            status=bot.send_message(chat_id="@RestockBot",text='Dual Intel Xeon L5520 %s Available link : %s\r\n' %(tmp.group(1),baseurl+m1.group(1)))
    if m3!=None:
        tmp=re.search(r'([1-9]{1,3}) Available',m3.group())
        if tmp!=None:
            print('Intel Xeon E3-1230 v2 %s Available link : %s\r\n' %(tmp.group(1),baseurl+m3.group(1)))
            status=bot.send_message(chat_id="@RestockBot",text='Dual Intel Xeon L5520 %s Available link : %s\r\n' %(tmp.group(1),baseurl+m1.group(1)))

