import requests,sys,hashlib,os
r=""
l = requests.session()
    info = {}
    header = {"Origin": "https://jksb.v.zzu.edu.cn","Referer": "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x17001126) NetType/WIFI Language/zh_CN","Host": "jksb.v.zzu.edu.cn"}
for q in range(32407,32409):
    w=l.get(sys.argv[1]+str(q)+".png", verify=False)
    if (w.status_code==404 or w.status_code==503):
        continue
    e=hashlib.md5(w.content).hexdigest()
    r=r+str(q)+","+e+"\n"
    with open("./t/"+str(q)+".png","wb") as code:
            code.write(w.content)
with open("./t/123.csv","w") as d:
    d.write(r)
