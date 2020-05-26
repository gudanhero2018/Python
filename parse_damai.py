import requests
import json
import pandas as pd

#封装数据的网站
def crawl(url): 
    
    headers={
        'cookie': 'cna=J7K2Fok5AXECARu7QWn6+cxu; isg=BCcnDiP-NfKV5bF-OctWuXuatl3xrPuOyBVJJfmQLrZn6ESqAX0y3jrhCuj2ANMG; l=eBSmWoPRQeT6Zn3iBO5whurza77O1CAf1sPzaNbMiIncC6BR1AvOCJxQLtyCvptRR8XcGLLB4nU7C5eTae7_7CDmndLHuI50MbkyCef..',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    response=requests.get(url,headers=headers)
    json_text=json.loads(response.text)
    # print(json_text.keys())
    rdata=json_text['pageData']['resultData']
#     print(rdata)
    return(rdata)

#构造目标数据网址
inidata=pd.DataFrame(columns=('name','actors','cityname','showtime','price_str','venue','venuecity','verticalPic'))
for i in range(1,7):
    url=f'https://search.damai.cn/searchajax.html?keyword=&cty=&ctl=%E6%BC%94%E5%94%B1%E4%BC%9A&sctl=&tsg=0&st=&et=&order=1&pageSize=30&currPage={i}&tn='
#     print(url)
#     print(crawl(url))
    data=pd.DataFrame(crawl(url))
    data1=data[['name','actors','cityname','showtime','price_str','venue','venuecity','verticalPic']]
    inidata=inidata.append(data1)
# print(inidata)
inidata.to_excel('大麦网演唱会.xlsx',index=0)