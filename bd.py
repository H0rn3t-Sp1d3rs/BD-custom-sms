import requests,os,sys
from colorama import Fore, init, Style
init(autoreset=True)
os.system("cls" if os.name == "nt" else "clear")
print(f'\n\n{Fore.GREEN}\t\tAPI BY TEAM BLACK BERRY\n\t\tCODE BY : @h0rn3t_sp1d3r\n\t\tTelegram : https://t.me/badscommunity0\n\n')
while True:
    number = input(f"{Fore.YELLOW} Enter 11 digits (BD Number):{Fore.WHITE} ")
    if number.isdigit() and len(number) <= 11:
        break
    else:
        print(f"{Fore.RED}Invalid input. Please enter up to 11 digits only.")
        exit()
message = input(f"{Fore.YELLOW} Enter your message:{Fore.RED} ")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0"}
data = {"number": number,"message": message}
response = requests.post("https://tbblab.shop/tbbcs/index.php", headers=headers, data=data)
if 'মেসেজ পাঠানো সফল হয়েছে!' in response.text or 'Message sent successfully' in response.text:
    print(f"{Fore.GREEN}\n Message sent successfully.")
else:
    print(f"{Fore.RED}\n Message sending failed.")
