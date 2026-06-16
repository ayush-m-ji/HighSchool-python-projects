print ("Welcome to smart inventory system")

#dictionarie
leptop = {
    "price": 50000, "stock": 6,
}

mouse = {
    "price": 300, "stock": 28,
}

keyboard = {
    "price": 800, "stock": 8,
}

inventory = {
    "leptop": leptop,
    "mouse": mouse,
    "keyboard": keyboard
}

#itams buy funtion
def buy_itam():

    if itam == "leptop":
        if 0 <= qty <= leptop["stock"]:
            leptop["stock"] -= qty
            amount = leptop["price"]*qty
        else:
            print("no more stock")
    elif itam == "mouse":
        if 0 <= qty <= mouse["stock"]:
            mouse["stock"] -= qty
            amount = mouse["price"]*qty
        else:
            print("no more stock")
    elif itam == "keyboard":
        if 0 <= qty <= keyboard["stock"]:
            keyboard["stock"] -= qty
            amount = keyboard["price"]*qty
        else:
            print("no more stock")

    print(f"the amount is {amount}")

        
# loop, the control the full funtion of this code
while True:
    try:
        print ("press 1 for view inventory")
        print ("press 2 for buy item")
        print ("press 3 for update stock")
        print ("press 4 for check low stock warning ")
        print ("press 5 for exit")
        user_input = int (input ())

#condition for view inventory
        if user_input == 1:
            for x, y in inventory.items():             
                print (x, y)
            input("press enter to go menu")

#condition for buy itam
        
        if user_input == 2:
            i = 1
            print ("inventory")
            for itams in inventory:
                print (f"{i}  {itams}")
                i += 1
            itam = input ("Enter the itam name ")
            if itam in inventory:
                print (f"the details of {itam} is:")
                print (inventory[itam])
                qty = int(input ("Enter quntity "))
                buy_itam()

            else:
                print("sorry this itam are not found in inventory")
                
            input ("press enter to go menu")

#add/update stock
        if user_input == 3:
            itam = input("Enter the itam name ")
            price = int (input("update price "))
            qty = int (input("Update quntity "))
            inventory[itam].update({"price": price, "stock": qty})
            print (inventory[itam])
            input ("press enter to go menu")

#check low stock 
        if user_input == 4:     
            print ("secning")
            for x, y in inventory.items():
                for a, b in y.items():
                    if a == "stock":
                        if b < 10:
                        
                            print (f"we have only {b} stock of {x}")
                    else:
                        pass
            input ("press enter to go menu")

#exit to funtion     
        if user_input == 5:
            print ("thanks")
            break

            
    except:
        print("please follow instructions")