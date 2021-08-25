from io import RawIOBase
import requests
import sys
import os
from colorama import init
init()
from colorama import Fore

if (__name__ == "__main__"):
    # Coded By Armin Asefi From https://geek-hub.ir
    if (len(sys.argv) == 3):
        webUrl = sys.argv[1]
        wordPath = sys.argv[2]
        if (os.path.exists(wordPath)):
            FILE = open(wordPath,"r")
            wordlist = FILE.readlines()
            for i in range(len(wordlist)):
                wordlist[i] = wordlist[i].replace("\n","")
            for i in wordlist:
                url = webUrl + "/" + i
                req = requests.get(url)
                if (int(req.status_code / 100) == 2 and req.is_redirect == False):
                    print(Fore.LIGHTGREEN_EX + "[" + str(req.status_code) + "] " + Fore.RESET + url)
                elif (int(req.status_code / 100) == 3 or req.is_redirect):
                    print(Fore.LIGHTYELLOW_EX + "[" + str(req.status_code) + "] " + Fore.RESET + url)
                elif (int(req.status_code / 100) == 4 or int(req.status_code / 100) == 5):
                    print(Fore.LIGHTRED_EX + "[" + str(req.status_code) + "] " + Fore.RESET + url)
                else:
                    print(Fore.LIGHTCYAN_EX + "[" + str(req.status_code) + "] " + Fore.RESET + url)
        else:
            print(Fore.LIGHTRED_EX + "wordlist is not exist..." + Fore.RESET)
    else:
        print(Fore.LIGHTRED_EX + "arg error ..." + Fore.RESET)
    print("Coded By Armin Asefi From https://geek-hub.ir")