#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests,bs4,json,os,sys,random,datetime,time,re
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
import os, re, sys, time, json, random, requests
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich.progress import track
from time import sleep
############ Indikator
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni,ses,freetoken,loop,opost= [],[],0,0,0,[],[],[],[],[],[],[],[],requests.Session(),[],[],[]
########################
H = '\x1b[1;92m' # HIJAU.
K = '\x1b[1;93m' # KUNING.
B = '\x1b[1;94m' # BIRU.
U = '\x1b[1;95m' # UNGU.
O = '\x1b[1;96m' # BIRU MUDA.
N = '\x1b[0m'   # WARNA MATI
#################
def vino():
	os.system('clear')
	print("""\x1b[1;91m ___      ___       __        ________  ____  ____  __   ___  
|"  \    /"  |     /""\      /"       )("  _||_ " ||/"| /  ") 
 \   \  //   |    /    \    (:   \___/ |   (  ) : |(: |/   /  
 /\\  \/.    |   /' /\  \    \___  \   (:  |  | . )|    __/   
\x1b[1;97m|: \.        |  //  __'  \    __/  \\   \\ \__/ // (// _  \   
|.  \    /:  | /   /  \\  \  /" \   :)  /\\ __ //\ |: | \  \  
|___|\__/|___|(___/    \___)(_______/  (__________)(__|  \__) 
                                                              """),time.sleep(2)
	print('\x1b[1;95m====================================================================='),time.sleep(1)
	print('\x1b[1;93m 1. Mulai Ambil Token Gratis '),time.sleep(1)
#	print(' [2] Ambil Token Gratis '),time.sleep(1)
#	print(' [3] Login '),time.sleep(1)
#	print(' [4] Keluar '),time.sleep(1)
	pox = input(' Pilih : ')
	if pox in ('',' '):
	    jalan('Jangan Kosong'),time.sleep(2);vino()
	elif pox in ('1','01'):
		free_token()
		os.sys.exit()
#	elif pox in ("2","02"):
#		free_token()
#		os.sys.exit()
#	elif pox in ("3","03"):
#		login()
#		os.sys.exit()
#	elif pox in ("4","04"):
#		os.sys.exit()
def free_token():
        num = 0
        llink_token = ses.get("https://www.facebook.com/100040708001839/posts/716737126359881/?app=fbl")
        ttoken_free = re.findall("EAAB\w+", llink_token.text)
        for nnaa in ttoken_free:
                num += 1
                if len(nnaa)>=37:
                        freetoken.append(nnaa)
                        print(" [%s] %s%s%s"%(num,H,nnaa,N))
                        print("-"*50)
        pil = input("\n [?] Salin Tokennya Lalu  Klik [ ENTER ] ")
        if pil in[""," "]:
                os.system('python rmd.py')
                
if __name__=='__main__':
	vino()
