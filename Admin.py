import sys
import json
import random
from datetime import datetime

print()
print("Time is :-",datetime.now(),
      "\n@aurthor is :-","Yogesh Bhardwaj")


class Admin:
    def __init__(self):
        self.food_id = "".join(random.sample("013246789",3))
        self.food_items = {}
       
    
    def add_food_items(self):
        food_name = input("Enter Your Food Name :")
        food_quentity = input("Enter Your Food Quentity :")
        price = int(input("Enter Your Price Here :"))
        Discount = int(input("Enter Your Discount Price here :")) 
        stock = int(input("Enter How Much Stock Left :"))
        self.food= {"food_name":food_name,"Quentity":food_quentity,"Price":price,"Discount":Discount,"Stock":stock}
        self.food_id = "".join(random.sample("013246789",3))
        self.food_items[self.food_id] = self.food
        
        with open("Admin.json","w") as f:
            json.dump(self.food_items,f,indent=4)
        print()
        print("Your Items Got Added Successfully")
        return ""
    
    #  For Watch Food Items Which You have added
    def watch_Add_items(self):
        with open("Admin.json","r") as f:
            tem = json.load(f)
        for i in tem.items():
            print(i)
        return ""
    
    # For Watch the Food ID
    def watch_food_id(self):
        l = []
        with open("Admin.json","r") as f:
            tem = json.load(f)
        for i in tem.keys():
            l.append(i)
        return l
    
    # For Removing Added_food Items

    def remove_food_items(self):
        ID = input("Enter Food Id Which You Want to Delete :")
        with open("Admin.json",'r') as f:
            self.temp = json.load(f)
        
        if ID not in self.temp:
            return "Enter a Valid ID"
        else:
            del self.temp[ID]

            with open("Admin.json","w") as f:
                json.dump(self.temp,f,indent=4)
                print("Items Got Removed")
            return ""

    # For Update Items    
    def Update_items(self):
        ID = input("Enter Food Id Which You Want to Update :")
        with open("Admin.json",'r') as f:
            self.temp = json.load(f)
        
        if ID not in self.temp:
            return "Please Enter a Valid ID"
        else:
            print(self.temp[ID])
            while True:
                print("+="*55)
                print("Press 0 For exit")
                print("Prees 1 for Update Food Name")
                print("Prees 2 for Update Quentity")
                print("Prees 3 for Update Price")
                print("Prees 4 for Update Discount")
                print("Prees 1 for Update Stock")
                update_input = int(input("Enter Your Number Here :"))

                if update_input ==1:
                    food_name = input("Enter Your New Food Name :")
                    self.temp[ID]["food_name"] = food_name
                    with open("Admin.json","w") as f:
                        json.dump(self.temp,f,indent=4)
                    print(self.temp[ID])
                
                if update_input ==2:
                    New_qty = input("Enter Your New Quentity Name :")
                    self.temp[ID]["Quentity"] = New_qty
                    with open("Admin.json","w") as f:
                        json.dump(self.temp,f,indent=4)
                    print(self.temp[ID])
                
                if update_input ==3:
                    new_Price = input("Enter Your New Quentity Name :")
                    self.temp[ID]["Prices"] = new_Price
                    with open("Admin.json","w") as f:
                       json.dump(self.temp,f,indent=4)
                    print(self.temp[ID])

                if update_input ==4:
                    new_Discount = input("Enter Your New Quentity Name :")
                    self.temp[ID]["Discount"] = new_Discount
                    with open("Admin.json","w") as f:
                       json.dump(self.temp,f,indent=4)
                    print(self.temp[ID])

                
                if update_input ==5:
                    Stock = input("Enter Your New Quentity Name :")
                    self.temp[ID]["Stock"] = Stock
                    with open("Admin.json","w") as f:
                       json.dump(self.temp,f,indent=4)
                    print(self.temp[ID])

                if update_input ==0:
                    print("Your Updated Items Food is :")
                    print(self.temp[ID])
                    break




    # For Updateing the items







user1 = Admin()
print(user1.watch_Add_items())
print(user1.watch_food_id())
print(user1.Update_items())
