import grequests,sys,hashlib,os,urllib3
urllib3.disable_warnings()
r=""
u=[]
task = []
header = {"Origin": "https://jksb.v.zzu.edu.cn","Referer": "https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x17001126) NetType/WIFI Language/zh_CN","Host": "jksb.v.zzu.edu.cn"}
for a in range(10000,100000):
    u.append(sys.argv[1]+str(a)+".png")
for o in u:
    req = grequests.request("get", url=o, headers=header)
    task.append(req)
resp = grequests.map(task, size=200)
for q in resp:
    if w.status_code==404:
        continue
    e=hashlib.md5(w.content).hexdigest()
    r=r+str(q)+","+e+"\n"
with open("./t/123.csv","w") as d:
    d.write(r)
