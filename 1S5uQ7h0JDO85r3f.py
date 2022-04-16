import requests,sys,hashlib,os
r=""

for q in range(32407,32409):
    w=requests.get(sys.argv[1]+str(q)+".png", verify=False)
    if (w.status_code==404 or w.status_code==503):
        continue
    e=hashlib.md5(w.content).hexdigest()
    r=r+str(q)+","+e+"\n"
    with open("./t/"+str(q)+".png","wb") as code:
            code.write(w.content)
with open("./t/123.csv","w") as d:
    d.write(r)
