import requests
import json
url='http://www.wanplus.com/ajax/statelist/player?isAjax=1&playerId=410&gametype=2&page=1&totalPage=undefined&totalItems=365&heroId=0&_gtk=1330814705'
headers={
    'Cookie':'wp_pvid=5079675510; wp_info=ssid=s3663004572; Hm_lvt_f69cb5ec253c6012b2aa449fb925c1c2=1497105975; Hm_lpvt_f69cb5ec253c6012b2aa449fb925c1c2=1497107041; wanplus_token=c88c97f3feeffec516277cb79f3a0a14; wanplus_storage=lf4m67eka3o; wanplus_sid=1f651f2fc0badac4afcda688db16ec24; wanplus_csrf=_csrf_tk_1246928625; gameType=2',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'X-CSRF-Token':'1330814705',
    'Referer':'http://www.wanplus.com/lol/player/1187',
}
data={
    '_gtk':'1330814705',
    'playerid':'410',
    'eid':'',
    'istime':'1',
    'gametype':'2',
}

r=requests.post(url,headers=headers,data=data)
# print(r)
faker=r.json()
# print(faker)
a={}
for i in faker['data']['stateList']['usedheroes']:
    # print(i)
    data="('%s':%s)"%(i['cpherokey'],i['appearancetimes'])
    a.update({i['cpherokey']: int(i['appearancetimes'])})
print(a)
a=json.dumps(a)
with open('data.txt','w')as f:
    f.write(a)
    # for i in a:
    #     f.writelines(i)
