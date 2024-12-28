import requests
from bs4 import BeautifulSoup
from steamid import SteamID
import random
import string

def GenerateRandomSteamID():
    account_type = random.randint(0, 1) 
    account_id = random.randint(1000, 5000) 
    steam_id = f"STEAM_0:{account_type}:{account_id}"
    return steam_id


def IsValidID(ID):
    return SteamID.isValid(ID)
    
    
def Check(ID, strid, fuckyou):
    if IsValidID(fuckyou) == False:
        return
    try:
        
        url = f"https://steamcommunity.com/profiles/{strid}"
        text = "This user has not yet set up their Steam Community profile."
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        website_text = soup.get_text()
        if text in website_text:
            print(f"[!] Low Dig Account! {url}")
    except requests.exceptions.RequestException as e:
        pass # shad dap.
    except KeyboardInterrupt: 
        exit()        
        

def main():
    print("Searching..")
    while True: 
        # test = SteamID.steam3(SteamID('STEAM_0:0:925340191'))
        nigger = SteamID(GenerateRandomSteamID())
        steamid3 = SteamID.steam3(SteamID(GenerateRandomSteamID()))
        idstring = SteamID.steam3(SteamID(GenerateRandomSteamID()))
        Check(steamid3, idstring, nigger)
        
        
        
main()
