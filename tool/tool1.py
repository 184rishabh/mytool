                                               
try:
                 import time
                 import os
                 import sys
                 import requests
                 import re
                 import json
                 import urllib
                 import colorama
                 import instaloader
                 from time import sleep
                 from datetime import datetime
                 import phonenumbers as pnumb
                 from phonenumbers import parse
                 from phonenumbers import geocoder
                 from phonenumbers import carrier
                 from phonenumbers import timezone
                 from instaloader import instaloader
except ModuleNotFoundError as e:
                 missing_module = str(e).split("'")[1]
                 print (f"Please Install Module First: {missing_module}")
                 sys.exit()
### 14 modules

### colors
RED = ""
GREEN = ""
BLUE = ""
YELLOW = ""
WHITE = ""
NORMAL = ""

OKGREEN = ''
WARNING = ''
YE = ''
BOLD = ''
ENDC = ''

CRED2 = ""
CBLUE2 = ""
ENDC = ""

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
### animation
def animation(s):
  for c in s + "\n":
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(0.0025)
     
### banner
def banner():
            animation (f"""
         [??] Choose an option:
         [1] Phone Number Information
         [2] Track IP
         [3] Instagram User Information
         [A] About""")
def start():
      os.system("clear")
      banner()
      chose=input("           Choose: ")
      if chose == "1": ## MENU 1
        sleep(1)
        number = input(f"Enter Number ({GREEN}Without +) :{CRED2}➤ ")
        parsing = parse(number)
        loc = geocoder.description_for_number(parsing,"id")
        isp = carrier.name_for_number(parsing,"id")
        tz = timezone.time_zones_for_number(parsing)
        ### track number v1
        print ()
        sleep(0.1)
        print(f"International Format          :",pnumb.normalize_digits_only(parsing))
        sleep(0.1)
        print(f"National Format               :",pnumb.national_significant_number(parsing))
        sleep(0.1)
        print(f"Valid Number                  :",pnumb.is_valid_number(parsing))
        sleep(0.1)
        print(f"Can Be Internatioally Dialled :",pnumb.can_be_internationally_dialled(parsing))
        sleep(0.1)
        print(f"Location                      :",loc)
        sleep(0.1)
        print(f"Region Code For Number        :",pnumb.region_code_for_number(parsing))
        sleep(0.1)
        print(f"Number Type                   :",pnumb.number_type(parsing))
        sleep(0.1)
        print(f"Is Carrier Specific           :",pnumb.is_carrier_specific(parsing))
        sleep(0.1)
        print(f"ISP                           :",isp)
        sleep(0.1)
        print(f"Time Zone                     :",tz)
        sleep(0.1)
        print('\nWhatsApp Number               : wa.me/' + number + ' \n')
        sleep(0.1)
        print(f"Is Number Geographical        :",pnumb.is_number_geographical(parsing))
        print("")
        sleep(1)
                    
      elif chose == "2": ## MENU 2
                        try:
                            def IP_Track():
                                           sleep(1)
                                           ip = input(f"\n Enter IP target :{CRED2}➤ ") #INPUT IP ADDRESS
                                           print()
                                           print(f' ============= SHOW INFORMATION IP ADDRESS =============')
                                           req_api = requests.get(f"http://ipwho.is/{ip}") #API IPWHOIS.IS
                                           ip_data = json.loads(req_api.text)
                                           time.sleep(0.5)
                                           print(f"\n IP target       :", ip)
                                           sleep(0.1)
                                           print(f" Type IP         :", ip_data["type"])
                                           sleep(0.1)
                                           print(f" Country         :", ip_data["country"])
                                           sleep(0.1)
                                           print(f" Country Code    :", ip_data["country_code"])
                                           sleep(0.1)
                                           print(f" City            :", ip_data["city"])
                                           sleep(0.1)
                                           print(f" Continent       :", ip_data["continent"])
                                           sleep(0.1)
                                           print(f" Continent Code  :", ip_data["continent_code"])
                                           sleep(0.1)
                                           print(f" Region          :", ip_data["region"])
                                           sleep(0.1)
                                           print(f" Region Code     :", ip_data["region_code"])
                                           sleep(0.1)
                                           print(f" Latitude        :", ip_data["latitude"])
                                           sleep(0.1)
                                           print(f" Longitude       :", ip_data["longitude"])
                                           sleep(0.1)
                                           lat = int(ip_data['latitude'])
                                           lon = int(ip_data['longitude'])
                                           sleep(0.1)
                                           print(f" Maps            :",f"https://www.google.com/maps/@{lat},{lon},8z")
                                           sleep(0.1)
                                           print(f" EU              :", ip_data["is_eu"])
                                           sleep(0.1)
                                           print(f" Postal          :", ip_data["postal"])
                                           sleep(0.1)
                                           print(f" Calling Code    :", ip_data["calling_code"])
                                           sleep(0.1)
                                           print(f" Capital         :", ip_data["capital"])
                                           sleep(0.1)
                                           print(f" Borders         :", ip_data["borders"])
                                           sleep(0.1)
                                           print(f" Country Flag    :", ip_data["flag"]["emoji"])
                                           sleep(0.1)
                                           print(f" ASN             :", ip_data["connection"]["asn"])
                                           sleep(0.1)
                                           print(f" ORG             :", ip_data["connection"]["org"])
                                           sleep(0.1)
                                           print(f" ISP             :", ip_data["connection"]["isp"])
                                           sleep(0.1)
                                           print(f" Domain          :", ip_data["connection"]["domain"])
                                           sleep(0.1)
                                           print(f" ID              :", ip_data["timezone"]["id"])
                                           sleep(0.1)
                                           print(f" ABBR            :", ip_data["timezone"]["abbr"])
                                           sleep(0.1)
                                           print(f" DST             :", ip_data["timezone"]["is_dst"])
                                           sleep(0.1)
                                           print(f" Offset          :", ip_data["timezone"]["offset"])
                                           sleep(0.1)
                                           print(f" UTC             :", ip_data["timezone"]["utc"])
                                           print ()
                                           sleep(0.1)
                            if __name__ == '__main__':
                                IP_Track()
                        except KeyboardInterrupt:
                            print(f" [{YE}!] {YE}PROGRAM STOPPED...")
      elif chose == "3":
          def instagram():
            import instaloader, sys
            from instaloader import instaloader
            x = instaloader.Instaloader()

            try:
                      print ()
                      sleep(1)
                      uname = input(f"\033[36mEnter a username :{CRED2}➤ \033[36m") #INPUT USER
                      if uname == "":
                                      print("\033[33mUnknown command!")
                                      sys.exit()

                      f = instaloader.Profile.from_username(x.context,uname)
                      print("Username :", f.username)
                      print("ID :", f.userid)
                      print("Full Name :", f.full_name)
                      print("Biography :", f.biography)
                      print("Business Category Name :", f.business_category_name)
                      print("External URL :", f.external_url)
                      print("Following :", f.followees)
                      print("Followers :", f.followers)
                      print("Highlight Reels :", f.has_highlight_reels)
                      print("Public Story :", f._has_public_story)
                      print("Business Account :", f.is_business_account)
                      print("Private Account :", f.is_private)
                      print("Verified :", f.is_verified)
                      print("Posts :", f.mediacount)
                      print("Profile Picture URL :", f.profile_pic_url)
                      print ()

            except KeyboardInterrupt:
                      print("\033[33mI understand!")

            except EOFError:
                      print("\033[33mWhy?")
          instagram()
                 
      elif chose == "A" or "a": ## MENU 4
                                     sleep(1)
                                     print(f"""
This is a tool for searching phone number information""")

start()
