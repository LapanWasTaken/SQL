#Author : LapanWasTaken
#Note   : Bila Cinta Di Dusta :D
import multiprocessing
from googlesearch import search
import requests, time, os
from colorama import Fore

from requests.models import HTTPError

Headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

def scan(query,count):
    try:
        if count == 1: result = search(query, num_results=count)

        elif count == 0: print(Fore.RED+"\n [!] Apa Yang Awak Letak Tu"); exit()

        elif count > 1: count -= 1; result = search(query, num_results=count)
        
        else: print(Fore.RED+"\n [!] Bubye !"); exit()

        no = 0
        for i in result:
            no += 1
            print(Fore.LIGHTBLUE_EX+f"\n [{no}] Finding --> {i}")
            url = i
            i = i+"'"
            
            try:
                r = requests.get(i,timeout=8)
                if "sql" in r.text or "SQL" in r.text or "Sql" in r.text:
                    print(Fore.GREEN+f"    [*] SQLi Found At [ {url} ]")
                else:
                    print(Fore.RED+"    [!] SQLi Not Found :(")
            except:
                print(Fore.RED+"    [!] Time Out !")

            time.sleep(0.5)
        return

    except KeyboardInterrupt:
        print(Fore.RED+"\n [!] OK BYE !")
        return exit()
    except HTTPError:
        print(Fore.RED+"\n [!] Too Many Requests, Cuba Lagi Awak :)")
    except Exception as e:
        print(e)
        return exit()


if __name__ == "__main__":
    os.system("clear")
    print(Fore.BLUE+"""
                           ,--.
                          {    }
                          K,   }
                         /  `Y`
                    _   /   /
                   {_'-K.__/
                     `/-.__L._
                     /  ' /`\_}
                    /  ' /     
            ____   /  ' /
     ,-'~~~~    ~~/  ' /_
   ,'             ``~~~%%',
  (                     %  Y
 {                      %% I
{      -                 %  `.
|       ',                %  )  ======================###===============
|        |   ,..__      __. Y   Coded By LapanWasTaken | t.me/Cendawannn
|    .,_./  Y ' / ^Y   J   )|   ======================###=============== 
\           |' /   |   |   ||
 \          L_/    . _ (_,.'(
  \,   ,      ^^""' / |      )
    \_  \          /,L]     /
      '-_`-,       ` `   ./`
         `-(_            )
             ^^\..___,.--`
             
    """)
    try:
            query = str(input(Fore.GREEN+"[*]Enter Query :" + Fore.RED + ""))
            count = int(input(Fore.GREEN+"[*]Enter Count of Result :" + Fore.RED + ""))
    except KeyboardInterrupt:
        print(Fore.GREEN+"\n [!] Bye Sayang")
        exit()
    except:
        print(Fore.GREEN+"\n [!] Error La Awak T_T")
        exit()
        
    p1 = multiprocessing.Process(target=scan, args=(query,count))
    p1.start()
    p1.join()
