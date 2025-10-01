# -*- coding: utf-8 -*-
import requests
import os
from datetime import datetime
from colorama import Fore, Style, init

os.system("printf '\033]2;₿lockChain v2.0 👨🏽‍💻\a'")

init(autoreset=True)

# Arte ASCII BTC
ascii_art = '''
                   .,:ldxxxxdl:,.                   
              .':oxxxxxxxxxxxxxxxxo:,.              
           'cdxxxxxxxxxxxxxxxxxxxxxxxxxc'           
        .cxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxc.        
      .lxxxxxxxxxxxxxxxxxkxxxxxxxxxxxxxxxxxxl.      
     cxxxxxxxxxxxxxxxxxx0MMKxxK0Oxxxxxxxxxxxxxc     
   .dxxxxxxxxxxxxkK0OkkxWMMkxKMMXxxxxxxxxxxxxxxd.   
  .xxxxxxxxxxxxxxKMMMMMMMMWK0WMMkxxxxxxxxxxxxxxxx.  
 .xxxxxxxxxxxxxxxxxkXMMMMMMMMMMMNX0kxxxxxxxxxxxxxx. 
 dxxxxxxxxxxxxxxxxxxXMMMMXkO0KNMMMMMXxxxxxxxxxxxxxd 
.xxxxxxxxxxxxxxxxxxkMMMMMkxxxxxOMMMMMKxxxxxxxxxxxxx'
lxxxxxxxxxxxxxxxxxxXMMMMNkxxxxkKMMMMM0xxxxxxxxxxxxxo
xxxxxxxxxxxxxxxxxxOMMMMMMMMWWWMMMMMW0xxxxxxxxxxxxxxx
dxxxxxxxxxxxxxxxxxNMMMMXO0KXNMMMMMNOxxxxxxxxxxxxxxxd
;xxxxxxxxxxxxxxxxOMMMMMkxxxxxkKMMMMMKxxxxxxxxxxxxxx;
 xxxxxxxxxxxxONXXWMMMMKxxxxxxxkMMMMMWxxxxxxxxxxxxxx 
 ;xxxxxxxxxxkNMMMMMMMMWXXK00KXWMMMMMKxxxxxxxxxxxxx: 
  lxxxxxxxxxxxxkO0WMMWMMMMMMMMMMMMWKxxxxxxxxxxxxxo  
   lxxxxxxxxxxxxxkMMWxxNMMKKKXXKKOxxxxxxxxxxxxxxo   
    ,xxxxxxxxxxxxKWM0xOMMWxxxxxxxxxxxxxxxxxxxxx,    
      dxxxxxxxxxxxxxxxOKXOxxxxxxxxxxxxxxxxxxxx      
        xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx        
          ;xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx:          
             .xxxxxxxxxxxxxxxxxxxxxxxx.             
                   xxxxxxxxxxxxxx.                  
                         lo
'''

def print_colored_ascii(art):
    for line in art.splitlines():
        colored_line = ""
        for char in line:
            if char == 'x':
                colored_line += Fore.LIGHTYELLOW_EX + char
            elif char in ['M', '0', 'K', 'W']:
                colored_line += Fore.WHITE + char
            else:
                colored_line += Style.RESET_ALL + char
        print(colored_line)
    print(Style.RESET_ALL)

def satoshi_to_btc(satoshi):
    return satoshi / 100000000

def get_btc_info(btc_address):
    url = f"https://blockchain.info/rawaddr/{btc_address}"
    try:
        response = requests.get(url)
        data = response.json()
        
        print(Fore.LIGHTGREEN_EX + f"\n[+] BTC Wallet: {data.get('address')}")
        print(Fore.LIGHTGREEN_EX + f" ├──Total Balance : {satoshi_to_btc(data.get('final_balance'))} BTC")
        print(Fore.LIGHTGREEN_EX + f" ├──Total Transactions : {data.get('n_tx')}")
        print(Fore.LIGHTGREEN_EX + f" ├──Total Received : {satoshi_to_btc(data.get('total_received'))} BTC")
        print(Fore.LIGHTGREEN_EX + f" ├──Total Sent : {satoshi_to_btc(data.get('total_sent'))} BTC")
        
        if 'txs' in data and len(data['txs']) > 0:
            first_tx = data['txs'][-1]  # La primera transacción es la última en la lista
            timestamp = first_tx.get('time')
            date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            print(Fore.LIGHTGREEN_EX + f" └──First Transaction : {date} (timestamp: {timestamp})")
    
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

def show_social_media():
    print(Fore.CYAN + "\n" + "═"*50)
    print(Fore.YELLOW + "🌐 OFFICIAL SOCIAL MEDIA ACCOUNTS")
    print(Fore.CYAN + "═"*50)
    print(Fore.WHITE + "📘 Facebook: " + Fore.BLUE + "https://www.facebook.com/profile.php?id=100083644015414")
    print(Fore.WHITE + "🐦 X (Twitter): " + Fore.BLUE + "https://twitter.com/abujamalhack")
    print(Fore.WHITE + "📸 Instagram: " + Fore.BLUE + "https://www.instagram.com/abujamalhack")
    print(Fore.WHITE + "🎵 TikTok: " + Fore.BLUE + "tiktok.com/@aiii_2024")
    print(Fore.WHITE + "📧 Email: " + Fore.BLUE + "abujamalhack@info.com")
    print(Fore.CYAN + "═"*50)

def show_developer_info():
    print(Fore.MAGENTA + "\n" + "👑"*50)
    print(Fore.YELLOW + "💻 DEVELOPED WITH LOVE BY ABU JAMAL ABDULNASSER AL-SHOUKI")
    print(Fore.MAGENTA + "👑"*50)
    print(Fore.WHITE + "👨‍💻 CEO at Hack Underway")
    print(Fore.WHITE + "🔐 Security Researcher")
    print(Fore.WHITE + "🐍 Made in Python with ❤️")
    print(Fore.WHITE + "🔗 All social media accounts activated")
    print(Fore.MAGENTA + "👑"*50)

def show_permissions():
    print(Fore.GREEN + "\n" + "⭐"*50)
    print(Fore.YELLOW + "🔓 FULL PERMISSIONS GRANTED")
    print(Fore.GREEN + "⭐"*50)
    print(Fore.WHITE + "✅ Full access to blockchain data")
    print(Fore.WHITE + "✅ Complete OSINT capabilities") 
    print(Fore.WHITE + "✅ Social media integration")
    print(Fore.WHITE + "✅ Commercial use allowed")
    print(Fore.WHITE + "✅ Modification and distribution")
    print(Fore.WHITE + "✅ Cross-platform support")
    print(Fore.WHITE + "✅ Community collaboration")
    print(Fore.GREEN + "⭐"*50)

if __name__ == "__main__":
    print_colored_ascii(ascii_art)

    # عرض المعلومات الجديدة
    show_social_media()
    show_developer_info()
    show_permissions()

    # التوقيع المحدث
    firma = "By: Abu Jamal Abdulnasser Al-Shouki - @abujamalhack\n"
    print(Style.BRIGHT + Fore.WHITE + firma.rjust(45) + Style.RESET_ALL)

    btc_address = input(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "Introduce una dirección de ₿itcoin: " + Style.RESET_ALL)
    get_btc_info(btc_address)
    
    print("\n" + " " * 2 + Style.BRIGHT + Fore.RED + "BlockChain OSINT " + Fore.WHITE + Style.BRIGHT + "I like to See You " + Fore.RED + "Happy OSINT" + Style.RESET_ALL + " 🚀\n")
    
    # رسالة ختامية محدثة
    print(Fore.LIGHTCYAN_EX + "💝 Thank you for using BlockChain v2.0!")
    print(Fore.LIGHTYELLOW_EX + "🔗 Follow me on all social media: @abujamalhack")
    print(Fore.LIGHTGREEN_EX + "⭐ Support the project - Abu Jamal Abdulnasser Al-Shouki\n")
