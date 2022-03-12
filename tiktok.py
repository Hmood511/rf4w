import os
lib = input("""
[1] setup
[2] continue

[+] Choose >> """)

if lib == "1":
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install colorama')
    os.system('cls' if os.name == 'nt' else 'clear')
    pass
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    pass

import json,requests,random
from colorama import *
from user_agent import generate_user_agent

g = Fore.GREEN
r = Fore.RED

try:
    os.system('color')
except:
    pass

banner = ("""
By TRIDX TEAM ™ Telegram: Issa_hh
  """)
print(banner)
print("=========================================")
option = input("""
[1] Cheack Users
[2] Generate Users

[+] Choose : """)
print("=========================================")
if option == "1":
    a = 0
    b = 0
    c = 0
    ssid = input('[+] SessionID : ')
    users = open('users.txt','r').read().splitlines()
    for user in users:
        url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id="+user+"&app_language=en"
        payload = ""
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "User-Agent": generate_user_agent(),
            "Connection": "Keep-Alive",
            "Host": "www.tiktok.com",
            "Accept-Encoding": "gzip, deflate",
            "Cache-Control": "max-age=0"
        }
        cookies = {'sessionid': ssid}
        res = requests.request ("GET", url, data=payload, headers=headers ,cookies=cookies).json()["status_msg"]
        if res == ""or"":
            a +=1
            print(g + f'[{a}] Good : {user}'+ Style.RESET_ALL)
            with open('good.txt','a') as new:
                new.write(f'{user}\n')

        elif 'This username isn’t available.' in res:
            b +=1
            print(r + f"[{b}] Bad : {user}" + Style.RESET_ALL)

        else:
            c +=1
            print(r + f"[{c}] Something wrong, try again" + Style.RESET_ALL)

elif option == '2':
    chars = 'abcdefghijklmnopqrstuvwxyz1234567890_.'
    user_len = int(input("[+] length : "))
    user_count = int(input("[+] How many users : "))
    for x in range(0, user_count):
        users = ""
        for x in range(0, user_len):
            users_char = random.choice(chars)
            users = users + users_char
        with open('users.txt','a') as ECHO:
            ECHO.write(f"{users}\n")
            ECHO.close()

else:
    print("[!] Please choose only 1 or 2")
    exit()
