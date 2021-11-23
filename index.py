operation= input("   ")
if operation =='*131#':
   print("1. data plans\n" "2. Xtravalus(data+voice)\n" "3. social bundle\n" "4. balance check\n" "5. roaming/int'l\n" "6. borrow credit/recharge\n"  "7. Gift\n" "8. Video pack\n" "9. Hot deals")
else:
   print('invald')
GOODNESS= input("input.. ")
if GOODNESS =='1':
    print("1. Daily plans\n" "2. Weekly plans\n" "3. monthly plans\n" "4. 2-3Month Plans\n" "5. Mifi plans\n" "6. FREE Youtube\n" "7. Popular plans" "8. Hot Deals\n" "9. Manage Data\n" "0. Back")
    house = input("input... ")

    if house =="1":
        print("1. n200 for 1Gb")
    elif house =="2":
        print("1. n200 for 200mb\n" "N500 for 1Gb")
    elif house =="3":
        print("1. n1000 for 20gb\n" "N5000 for 1Tb")   
    elif GOODNESS =='2':
        print("1. XtraTalk\n" "2. XtraData\n" "3. Eligible Int'l Destination\n" "4. XtraData")
elif GOODNESS =='3':
   print("1. WhatsApp\n" "2. Facebook\n" "3. Instgram\n" "4. TikTok\n" "5. Ayoba\n" "6. All socal Bundles\n" "7. YouTube, Instagram,and TikTok" "8. opera Mini & News\n" "9. Socal Mega bundle\n" "99 .Next")
elif GOODNESS =='4': 
   print('99.next\n' '0.back')    
elif GOODNESS =='5':  
   print("1. Roaming Data Bundles\n" "2. Roaming Voice + Data Bundles\n" "3. Free incoming roaming call\n" "4. lnt'l Calling Bundle\n" "5. Roaming Balance Check\n" ) 
elif GOODNESS =='6':  
   print("1. Borrow Airtime\n" "2. Borrow Data\n" "0. Back" )  
elif GOODNESS =='7':  
   print("1. Roaming Data Bundle\n" "2. Roaming Voice + Data Bundles\n" "3. Free incoming roaming call\n" "4. lnt'l Calling Bundle\n" "5. Roaming Balance Check\n" )        
elif GOODNESS =='8':  
   print("1. Youtube Video pack\n" "2. startimes video pack\n" "3. 1GB(YouTube Only)+ 500MB (Data access)\n" "4. Showmax moblile") 
elif GOODNESS =='9':  
   print("1. TopDeal4ME\n" "2. Recharge4ME\n" "3. Data4ME\n" "4. Combo4ME\n" "5. VAS4ME")              
else:
   print('invalid') 