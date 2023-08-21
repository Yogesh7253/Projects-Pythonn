from datetime import datetime
import sys
import time
import json
from User import user

print()
print("Date :",datetime.now(),
      "\n@Aurthor :","Yogesh Bhardwaj")
    
# Use Email :- yogeshbhardwaj1001@gmail.com
# Pass :-  Yogesh@@09876 for Login

demo1 = user()
email = input("Enter Your Mail Id :")
passw = input("Enter Your Password :")

with open("User_details.json","r") as f:
    temp = json.load(f)
if temp["Email Address"] != email:
    print("Your Are not Our Exiting Coustome Login Again")
else:
    demo1.login(email,passw)
    while True:

        print("--------------------------------------------------------------------------->>>>>>Welcome to Bhojan App<<<<<------------------------------------------------------------\n")
        time.sleep(2)
        l = []
        rs = 0
        order_history = {}

        print("+="*60)
        print("Press E for Exit the App 👉👉")
        print("Press P Place New Order 👉👉")
        print("Press H Order History 👉👉")
        print("Press U Update Profile 👉👉")
        print("+="*60)

        user_input = input("Press Button :")
        if user_input ==  "P" or user_input =="p":
            with open("Admin.json","r") as f:
                temp = json.load(f)
            print("1. ",temp["621"]["Quentity"] ," ",temp["621"]["food_name"],"..........................",temp["621"]["Price"],"Rupee")
            print("2. ",temp["072"]["Quentity"] ," ",temp["072"]["food_name"],"..........................",temp["072"]["Price"],"Rupee")
            print("3. ",temp["089"]["Quentity"] ," ",temp["089"]["food_name"],"........................",temp["089"]["Price"],"Rupee")
            print("4. ",temp["834"]["Quentity"] ," ",temp["834"]["food_name"],".........................",temp["834"]["Price"],"Rupee")
            print("5. ",temp["462"]["Quentity"] ," ",temp["462"]["food_name"],"..........................",temp["462"]["Price"],"Rupee")
            print("6. ",temp["182"]["Quentity"] ," ",temp["182"]["food_name"],"..........................",temp["182"]["Price"],"Rupee")
            print("7. ",temp["043"]["Quentity"] ," ",temp["043"]["food_name"],"..........................",temp["043"]["Price"],"Rupee")
       
            print()
            print("------------------------->>>>>Press 999 For Place Your Order <<<<------------------------")
            ch = 1
            while ch!=0:
                ch = int(input(" Press Button For Order----> "))
                if ch==1 :
                    rs+=240
                    l.append(temp["621"]["food_name"])

                elif ch==2:
                    rs+=320
                    l.append(temp["072"]["food_name"])
                    
                elif ch==3:
                    rs+=14
                    l.append(temp["834"]["food_name"])       
                
                elif ch==4:
                    rs+=12
                    l.append(temp["462"]["food_name"])
                
                elif ch==5:
                    rs+=120
                    l.append(temp["462"]["food_name"])
                
                elif ch==6:
                    rs+=25
                    l.append(temp["182"]["food_name"])
            
                elif ch==7:
                    rs+=30
                    l.append(temp["043"]["food_name"])
                
                elif ch==999:
                    print()
                    order_history={"Order History":l,"Total Bill":rs}
                    with open("history.json","w") as f:
                        json.dump(order_history,f,indent=4)
                    time.sleep(2)
                    print("Total Bill : - ",rs)
                    print(               " 🎆🎊🎊     Your Order Got Placed   🎆🎊🎊"              )
                    print("You'll Get Your Order Soon")
                    print()
                    print("              Thanks For Using Bhojan App      ")
                    break

        elif user_input=="h" or user_input=="H":
            with open("history.json","r")  as f:
                temp =json.load(f)
                print(temp)            

        elif user_input=="U" or user_input=="u":   
            demo1.update_profile()

        elif user_input =="E" or user_input=="e":
            sys.exit()