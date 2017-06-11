import requests
import time
import json
a={}
for j in range(1,80):
    url='http://www.wanplus.com/ajax/hero/recent?isAjax=1&id=73&page=%d&gametype=2&timerange=all&eid=-1&result=-1&totalitems=79'%(j)
    headers={
        'Cookie':'wp_pvid=5079675510; wp_info=ssid=s3663004572; Hm_lvt_f69cb5ec253c6012b2aa449fb925c1c2=1497105975; Hm_lpvt_f69cb5ec253c6012b2aa449fb925c1c2=1497107041; wanplus_token=c88c97f3feeffec516277cb79f3a0a14; wanplus_storage=lf4m67eka3o; wanplus_sid=1f651f2fc0badac4afcda688db16ec24; wanplus_csrf=_csrf_tk_1246928625; gameType=2',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'X-CSRF-Token':'1330814705',
        'Referer':'http://www.wanplus.com/lol/player/1187',
    }
    data={
        '_gtk':'1330814705',
        'id':'73',
        'eid':'-1',
        'result':'-1',
        'totalitems':'79',
        'page':'%d'%(j),
        'gametype':'2',
    }

    r=requests.post(url,headers=headers,data=data)
    orianna=r.json()
    for i in orianna['data']['plDatumList']:
        # print(i)
        # print(i['playername'])
        if i['playername'] in a.keys():
            a[i['playername']]+=1
        else:
            a.update({i['playername']: int(1)})
    time.sleep(2)
    print('抓取%d页'%j)
print(a)
a=json.dumps(a)
with open('data-orianna.text','w')as f:
    f.write(a)
