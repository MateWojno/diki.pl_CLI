#=======+=======+                   #=======+=======+
#       @author:    matewojno
#       @date:      11.11.2026
#       @purpouse:  translate using diki.pl in cli
#       @vesion:    1.0.2
#=======+=======+                      #=======+=======+

#=======+=======+   TODO LIST           #=======+=======+
#   @ToDo:      
#       1.  Save queryString and queryResults to db (json, csv, sqlite3)
#       2.  Make the output more appealing
#       3.  Use args* in main to run the app in cmd: diki <phrase>
#       4.  Refactor the code if possible
#       5.  Search in db first if there is no answer then do requests.get()
#       6.  Make output more appealing 
#=======+=======+   TODO LIST           #=======+=======+


#=======+=======+   DEPENDENCIES        #=======+=======+

#   To export my history of searches 
import json     
import csv      

#   To use system commands
import os           

#   To send HTTP/1.1 requests easily
import requests

#   To use REGEX - regular expressions
import re           #it is not used at the moment

#   To scrape web easily, html parser
from bs4 import BeautifulSoup

#=======+=======+   DEPENDENCIES        #=======+=======+

#=======+=======+   OUTPUT COLORS        #=======+=======+

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' 
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'

# return to standard color
RESET = '\033[0m' 

OUTPUT_COLORS = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]
#   @ToDo:  make function(textArg) to:
    #generateRandomColor, 
    #print text(textArg),
    #return to standard color
    
#=======+=======+   OUTPUT COLORS        #=======+=======+


queryString = ""
    
headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
            " like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
    }
    
mainUrl = "https://www.diki.pl/slownik-angielskiego?q="

def runQuery():
    queryString = input("Give me your world to check in dictionary: ")
    mainQuery = mainUrl + queryString

    try:
        response = requests.get(mainQuery, headers=headers, timeout=10)
        if response.status_code != 200:
            printf(f"[-] Error {response.status_code} try again!")
            return 
    except Exception as e:
        print(f"[-] Network error {mainQuery}: {e}")
        return 
        
    soup = BeautifulSoup(response.text, "html.parser")


    targetSpans = soup.select('ol.foreignToNativeMeanings li[id^="meaning"] span.hw')
    
    if not targetSpans:
        print("[-] No translations found or page structure has changed.")
        return 
    
    #   @Todo wrap in in list or something as queryResults
    print(RED + "\n--- RESULTS ---\n" + RESET)
    for index, span in enumerate(targetSpans, 1):
        print(f"{index}. \t{span.get_text(strip=True)}")
    print(RED + "\n--- END OF RESULTS ---\n" + RESET)
    
if __name__ == "__main__":
    os.system("cls")
    runQuery()
    
