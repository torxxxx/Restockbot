from urllib import request

url = "https://billing.spartanhost.net/cart.php?a=add&pid=206"
header={'Host': 'billing.spartanhost.net',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Connection': 'keep-alive',
'Cookie': 'cf_clearance=BmeFQPFC7j0_Sk4IN5CfetIQRsNBKYuD8JXehw0M_UY-1636980530-0-150; __stripe_mid=0a9a4b6c-e5ac-4f26-acb9-150be8e1a28cbc57d5; __stripe_sid=405c31de-f59f-4362-96ee-d198fd39c02628a8b0; WHMCSYGwdvD9rORze=j2l6dhufot6o8r3g5vphj54110',
'Upgrade-Insecure-Requests':'1',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Cache-Control': 'max-age=0',
'TE': 'trailers'
}
while True:
    req=request.Request(url,headers=header)
    page=request.urlopen(req).read()
    if page.decode("utf-8").find("We are currently out of stock") > 0:
        print("No Stock")
    else :
        print("reStocked")