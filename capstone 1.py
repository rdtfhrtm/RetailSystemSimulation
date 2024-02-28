
import time
import sys

#keyid, name, address, city, phone, money deposit,dictionary of item cart
user = {
    "ADMIN": ["admin", "asd"],
    "CUST001": ["Andy Warhol", "312 E 2 Street", "Hummelstown", "233-847-7561", 400, {}],
    "CUST002": ["John Wick", "181 N Pottstown Pike", "Exton", "932-814-0012", 900, {}],
    "CUST003": ["Peggy Gou", "57 Kensington Street", "Philadelphia", "523-756-3314", 10, {}],
    "CUST004": ["Justin Bieber", "90 Street 3 Avenue", "New York City", "432-343-5673", 10000, {}],
    "CUST005": ["Justin Timberlake", "18 Bleecker Street", "New York City", "717-905-2934", 3000, {}],
    "CUST006": ["Michael Jordan", "23 North Street", "Chicago", "312-555-1234", 500, {}],
    "CUST007": ["LeBron James", "6 South Avenue", "Los Angeles", "213-555-5678", 700, {}],
    "CUST008": ["Kobe Bryant", "8 West Street", "Los Angeles", "213-555-8765", 200, {}],
    "CUST009": ["Serena Williams", "10 E Jo Street", "Miami", "305-555-4321", 1000, {}],
    "CUST010": ["Tom Brady", "12 East 2 Street", "Tampa Bay", "813-555-9876", 1500, {}],
    "CUST011": ["Michael Phelps", "14 South Avenue", "Baltimore", "410-555-2468", 800, {}],
    "CUST012": ["Lionel Messi", "16 West Wash Street", "Barcelona", "123-456-7890", 3000, {}],
    "CUST013": ["Cristiano Ronaldo", "18 North Street", "Turin", "456-789-0123", 2000, {}],
    "CUST014": ["Neymar Jr", "20 E Ronald Drive", "Paris", "789-012-3456", 4000, {}],
    "CUST015": ["Virat Kohli", "22 E Mary Street Pike", "Delhi", "012-345-6789", 600, {}],
    "CUST016": ["Roger Federer", "24 North White Street", "Zurich", "345-678-9012", 900, {}],
    "CUST017": ["Rafael Nadal", "26 West Street Springs", "Mallorca", "678-901-2345", 1200, {}],
    "CUST018": ["Lewis Hamilton", "28 Wendi Street", "Monaco", "901-234-5678", 1800, {}],
    "CUST019": ["Sebastian Vettel", "30 Xumse 22 Street", "Heppenheim", "234-567-8901", 2200, {}],
    "CUST020": ["Max Verstappen", "32 Zumba Avenue", "Montfort", "567-890-1234", 2500, {}]
}

#keyid, name, price, stock, discount rate, category
item = {
    "ITEM001": ["Red Gaming Chair", 400, 300, 0, "Computer"],
    "ITEM002": ["Skech Sneakers", 120, 33, 30, "Wearable"],
    "ITEM003": ["Chicken Costume", 320, 55, 50, "Wearable"],
    "ITEM004": ["Steelseries Keyboard", 60, 30, 40, "Computer"],
    "ITEM005": ["Flower Vase", 6, 25, 20, "Ornament"],
    "ITEM006": ["Jordan Sneakers", 200, 10, 10, "Wearable"],
    "ITEM007": ["Coffee Machine", 500, 100, 0, "Kitchen"],
    "ITEM008": ["Steak Knives", 3, 3000, 5, "Kitchen"],
    "ITEM009": ["Fat Chicken Pillow", 34, 900, 15, "Home"],
    "ITEM010": ["Red Lemon Bags", 7, 3000, 0, "Food"],
    "ITEM011": ["Bed Matress", 1500, 20, 30, "Furniture"],
    "ITEM012": ["Wooden Table", 30, 40, 25, "Furniture"],
    "ITEM013": ["Bed Lamp", 4, 50, 20, "Electronics"],
    "ITEM014": ["White Phone", 20, 600, 15, "Electronics"],
    "ITEM015": ["Brown Sofa", 50, 760, 30, "Furniture"],
    "ITEM016": ["Yeezy Sneakers", 500, 50, 0, "Wearable"],
    "ITEM017": ["Bed Nightstand", 100, 400, 0, "Furniture"],
    "ITEM018": ["Flu Syrup", 4, 1322, 0, "Medicine"],
    "ITEM019": ["Roland Keyboard", 700, 13, 5, "Music"],
    "ITEM020": ["Black Mirror", 30, 40, 0, "Home"],
    "ITEM021": ["Flat Television", 3000, 100, 30, "Electronics"],
    "ITEM022": ["Red Oven", 406, 30, 16, "Kitchen"],
    "ITEM023": ["Wooden Bed", 560, 20, 0, "Home"],
    "ITEM024": ["Lemon Juice", 6, 10, 0, "Food"],
    "ITEM025": ["Chicken Nuggets", 8, 9000, 0, "Food"],
    "ITEM026": ["Tube Television", 1000, 400, 10, "Electronics"],
    "ITEM027": ["Basketball", 15, 70, 0, "Sports"],
    "ITEM028": ["Electric Guitar", 4206, 90, 30, "Music"],
    "ITEM029": ["Coughing Syrup", 6, 2000, 0, "Medicine"],
    "ITEM030": ["Lego Set", 55, 1000, 0, "Toys"],
    "ITEM031": ["Drum Kit", 1000, 30, 25, "Music"]
}

transaction_history = ['CUST003', 'CUST003', 'CUST002','CUST001']

transaction_history_amount = {"CUST002" : 10000, "CUST003": 900, "CUST001" : 400}

processed_transaction = [['PT001','CUST001', {"Spoon":1,"Steak Knives":5},
                          "312 E 2 Street", "Hummelstown", "233-847-7561"],
                         ['PT002','CUST002', {"Flower vase":2},
                          "181 N Pottstown Pike", "Exton", "932-814-0012"]
                        ]


def moving_print(text, speed=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

def sleep(x = 0.75):
    time.sleep(x)

def cleartrm():
    print('\033c', end='')

def exitmen():
        cleartrm() 
        exs = "\n\nHave a Good One!"
        moving_print(exs, 0.03)
        sleep(1)

def menuHeader(x=0.01):
    mh = '''\t-= Welcome to FAST Super Store =-\n\n'''
    moving_print(mh, speed= x)

def getUserKey():
    while True:
        cleartrm()
        print(f"{'-'*11}\n--WELCOME--\n{'-'*11}\n")
        welc = "Greetings, FAST Super Store User!"
        moving_print(welc, speed=0.01)
        a = input("\n\nEnter your user code ('exit' to quit program): ").upper()
        if a == "EXIT":
            cleartrm()
            print('\n\n\n')
            exitf = "- = G O O D   B Y E ! = -"
            moving_print(exitf, speed=0.05)
            sleep(1)
            cleartrm()
            exit()        
        elif a not in user.keys():
            print("User invalid!\n")
            sleep()
        else:
            return a

def welcomingAdmin(userKey):
    cleartrm()
    menuHeader()
    print(f"Welcome, {user[userKey][0].title()}!")

def welcomingGreetings(userKey):
    name = user[userKey][0].title()
    balance = user[userKey][4]
    cleartrm()
    menuHeader()
    print(f"Welcome, ", end = '')
    namewelc = f"{name}"
    moving_print(namewelc, speed=0.03)
    print('\t\tYour Balance: $ ',end = '')
    balwelc = str(balance)
    moving_print(balwelc, speed=0.1)
    print()

def menuAdmin():
    print('''
    1.  View all user      
    2.  Add user
    3.  Edit user
    4.  Delete user      
    5.  View all items      
    6.  Add item
    7.  Edit item
    8.  Delete item
    9.  Search user details   
    10. View processed transactions    
    11. Exit admin menu  
''')
    
def menuCustomer():
    print('''
    1. View all items 
    2. Search for items            
    3. View items on sale
    4. View items by category
    5. View items by price range     
    6. View Cart      
    7. Checkout cart      
    8. Top up balance
    9. Exit customer menu  
''')

def listUser(dict):
    cleartrm()
    print(f"\n-== Showing all users  ==-")
    print(
        f"\n{'CCODE'.ljust(8)}|"
        f"{'NAME'.ljust(25)}|"
        f"{'ADDRESS'.ljust(27)}|"
        f"{'CITY'.ljust(15)}|"
        f"{'PHONE'.ljust(12)}|BALANCE"
    )
    for i in dict:
        if i == "ADMIN":
            continue
        else:
            print(
                f"{i.ljust(8)}|"
                f"{dict[i][0].ljust(25)}|"
                f"{dict[i][1].ljust(27)}|"
                f"{dict[i][2].ljust(15)}|"
                f"{dict[i][3].ljust(12)}|"
                f"{dict[i][4]}"
            )

def listItem(dict):
    cleartrm()
    print(f"\n-== Showing all items  ==-")
    print(
        f"\n{'ICODE'.ljust(8)}|"
        f"{'NAME'.ljust(27)}|"
        f"{'PRICE'.ljust(8)}|"
        f"{'STOCK'.ljust(8)}|"
        f"{'DISCOUNT RATE'.ljust(15)}|CATEGORY"
    )
    for i in dict:
        print(
            f"{i.ljust(8)}|"
            f"{str(dict[i][0]).ljust(27)}|"
            f"{str(dict[i][1]).ljust(8)}|"
            f"{str(dict[i][2]).ljust(8)}|"
            f"{str(dict[i][3]).ljust(15)}|"
            f"{str(dict[i][4])}"
        )

def fillUser(s):
    while True:
        a = input(f"\nEnter new user's name {s}: ").lower()
        if a == "cancel":
            return a,'0','0','0'
        elif a != "":
            break
        else:
            print("Input cannot be blanked! \n")
    while True:
        b = input("Enter new user's address : ")
        if b != "":
            break
        else:
            print("Input cannot be blanked! \n")
    while True:
        c = input("Enter new user's city of residence : ")
        if c != "":
            break
        else:
            print("Input cannot be blanked! \n")
    while True:
        d = input("Enter new user's phone : ")
        if d == "":
            print("Input cannot be blanked! \n")
        elif d.isnumeric() == False or len(d) != 10:
            print("Enter valid number!\n")    
        else:
            break 
    return a.strip().title(),b.strip().title(),c.strip().title(),d.strip()

def fillItem(s):
    while True:
        itemnames = [item[i][0] for i in item]

        a = input(f"\nEnter new item's name {s}: ").title().strip()
        if a.lower() == "cancel":
            return a,0,0,0,'0'
        elif a in itemnames:
            print("Item already exists! \n")
        elif a != "":
            break
        else:
            print("Input cannot be blanked! \n")
    while True:
        b = input("Enter new item's price : ")
        if b.isdigit() == True and int(b) >= 0:
            b = int(b)
            break
        else:
            print("Input cannot be blanked / non-numeric / less than zero! \n")
    while True:
        c = input("Enter new item's stock : ")
        if c.isdigit() == True and int(c) >= 0:
            break
        else:
            print("Input cannot be blanked / non-numeric / less than zero! \n")
    while True:
        d = input("Enter new item's discount rate : ")
        if d.isdigit() == True and 0 <= int(d) <= 80:
            break
        else:
            print("Input cannot be blanked / non-numeric / less than zero / more than 80! \n")
    while True:
        e = input("Enter new item's category : ").title().strip()
        if e == "":
            print("Input cannot be blanked! \n")
        else:
            break 
    return a,b,c,d,e
   
def getCode(dict, action, obj):
        x = input(f"\nEnter {obj}'s code to be {action} ('cancel' to cancel): ").upper()
        if x == "CANCEL":
            return x
        elif x in list(dict.keys()):
            return x
        else:
            print(f"Invalid {obj} code!")
            sleep()
            return 0

def showTempDict(tempdict):
    print(f"\n{'ICODE'.ljust(8)}|{'NAME'.ljust(27)}|{'PRICE'.ljust(8)}|{'STOCK'.ljust(8)}|{'DISCOUNT RATE'.ljust(15)}|CATEGORY")
    for i in tempdict:
        print(
            f"{i.ljust(8)}|"
            f"{str(tempdict[i][0]).ljust(27)}|"
            f"{str(tempdict[i][1]).ljust(8)}|"
            f"{str(tempdict[i][2]).ljust(8)}|"
            f"{str(tempdict[i][3]).ljust(15)}|"
            f"{str(tempdict[i][4])}"
        )

def getAdmPass():
    while True:
        cleartrm()
        a = input("\n\nEnter Password ('cancel' to cancel): ")
        if a.lower() == "cancel":
            return 0
        elif a == user["ADMIN"][1]:
            return a
        else:
            print("Password incorrect! \n")
            sleep()

def format_phonenum(d):
    return d[:3] + '-' + d[3:6] + '-' + d[6:]

def getlastkeyint(dict):
        last_key = list(dict.keys())[-1]
        last_int = int(last_key[4:])
        return last_int

def addtocart(dict1,dict2, itemkey, userkey):
    stock = dict1[itemkey][2]
    while True:
        try:
            qty = int(input("Enter quantity : "))
            if qty > stock:
                print("Quantity is more than the item stock!\n")
            elif qty > 0:
                break
            else:
                print("Cannot be zero!\n")
        except:
            print("Invalid input!\n")

    name = dict1[itemkey][0]
    price = dict1[itemkey][1]
    disc = dict1[itemkey][3]
    if itemkey in dict2[userkey][5]:
        dict2[userkey][5][itemkey][1] += qty
    else:
        dict2[userkey][5][itemkey] = [name, qty, price, disc]
    dict1[itemkey][2] -= qty

def showcart(dict):
            print(f"\n-== Your Cart ==-")
            print(f"\n{'ICODE'.ljust(8)}|{'NAME'.ljust(27)}|{'QUANTITY'.ljust(15)}|{'PRICE'.ljust(15)}|{'DISCOUNT RATE'.ljust(15)}")
            for i in dict:
                print(
                    f"{i.ljust(8)}|"
                    f"{dict[i][0].ljust(27)}|"
                    f"{str(dict[i][1]).ljust(15)}|"
                    f"{str(dict[i][2]).ljust(15)}|"
                    f"{str(dict[i][3]).ljust(15)}"
                )
    
def showcartcheckout(dict):
            grandtotal = 0
            totalitem = 0
            print(f"\n-== Your Cart ==-")
            print(f"\n{'NAME'.ljust(27)}|{'QUANTITY'.ljust(15)}|{'PRICE'.ljust(15)}|{'DISCOUNT RATE'.ljust(15)}|{'SUB TOTAL'.ljust(15)}")
            for i in dict:      
                    qty = dict[i][1]
                    price = dict[i][2]
                    disc = dict[i][3]
                    subtotal = (price - (price*(disc/100))) * qty
                    subtotal = round(subtotal,2)
                    totalitem += qty
                    grandtotal += subtotal
                    print(
                        f"{dict[i][0].ljust(27)}|"
                        f"{str(qty).ljust(15)}|"
                        f"{str(price).ljust(15)}|"
                        f"{str(disc).ljust(15)}|"
                        f"{str(round(subtotal,2)).ljust(15)}"
                    )
            return round(grandtotal,2), totalitem

def cartclearing_historyappending(userKey, dict, dict2, dict3, gt):
    dict.append(userKey)

    if userKey in dict2:
        dict2[userKey] += gt
    else:
        dict2[userKey] = gt

    dict3[userKey][5].clear()    

def balance_subtracting(balance, grandtotal):
    return balance - grandtotal

def itemaddednotif():
    input("\nItem added to cart!\nPress enter to continue...")

def topupbal(dict, key):
        topup = int(input("\nEnter amount you wish to add : "))
        dict[key][4] += topup

def showuserdetails(dict, st, ctc, trt, code):
    cleartrm()
    print(f"\n-== Showing details of customer: {code} ==-")
    print(f"\n{'CCODE'.ljust(8)}|{'NAME'.ljust(25)}|{'ADDRESS'.ljust(27)}|{'CITY'.ljust(15)}|{'PHONE'.ljust(12)}|BALANCE")
    print(f"{code.ljust(8)}|"
          f"{dict[code][0].ljust(25)}|"
          f"{dict[code][1].ljust(27)}|"
          f"{dict[code][2].ljust(15)}|"
          f"{dict[code][3].ljust(12)}|"
          f"{dict[code][4]}")
    print(f"\nTotal transaction amount   : {st}")
    print(f"Distinct items in cart     : {ctc}")
    print(f"Transaction history count  : {trt}")
    input("\nPress enter to continue...")      

def ptlastint(list):
    listlastint = [int(i[0][2:]) for i in list][-1]
    return listlastint

def showpt(list):
    print(f"-== Showing all processed transactions  ==-\n")
    for i in list:
        print(i[0])
        print("--------")
        print(f"Customer Code : {i[1]}")
        print("\n--Item list--")
        for j in i[2]:
            print(f"{j.ljust(15)} : {i[2][j]} unit(s)")
        print("\n--Address and Contact of Delivery--")
        print(f"{i[3]}, {i[4]}\n{i[5]}")
        print()

def get_price_range():
    while True:
        try:
            cleartrm()
            priceRange = input("\nEnter price range separated by comma : ")
            listRange = priceRange.split(',')
            
            if listRange[0].isdigit() == False or listRange[1].isdigit() == False:
                print("\ninput must be numeric!")
                sleep()
            elif priceRange.count(',') != 1:
                print("\ninput 2 numbers only!")
                sleep()
            else:
                return listRange
        except:
            print("\nInvalid input!")
            sleep()

def partialupdate(col,dict,key,pos):
    while True:
        parinp = input(f"\nEnter new {col} : ").title()
        if parinp != "":
            break
        else:
            print("Input cannot be blanked!")

    cleartrm()
    print(f"\nNew {col} : {parinp}")
    conf1 = input("\nDo you wish to proceed with the update? (y/n) : ").lower()
    if conf1 == 'y':
        dict[key][pos] = parinp
        input("\nUser updated!\nPress enter to continue...")

#main menu ===================================
flag = 1
while flag == 1:
    cleartrm()
    userKey = getUserKey()
    flag2 = 1
    while flag2 == 1:
        if userKey == "ADMIN":    
            ap = getAdmPass()
            if ap == 0:
                break 
            else:
                flag3 = 1
                while flag3 == 1:
                    while True:
                        try:
                            welcomingAdmin(userKey)
                            menuAdmin()
                            admInput = int(input("Enter menu number : "))
                            if 1 <= admInput <= 11:
                                
                                if admInput == 1:
                                    #VIEW ALL USER
                                    cleartrm()
                                    listUser(user)
                                    input("\nPress enter to continue...")
                                elif admInput == 2:
                                        #ADD USER
                                        cleartrm()
                                        last_int = getlastkeyint(user)
                                        a,b,c,d = fillUser("('cancel' to cancel)")
                                        if a == "cancel":
                                            break
                                        else:
                                            d = format_phonenum(d)
                                            dup_indices = [i[:4] for i in user.values() if i[0] != "admin"]

                                            if [a,b,c,d] in dup_indices:
                                                input("\nUser already exists!\nPress enter to continue...")        
                                            else:
                                                newkey = "CUST"+str(last_int+1).zfill(3)
                                                cleartrm()
                                                print(f"\n\nNew User: {newkey}")
                                                print("--------------------")
                                                print(f"New Name    : {a}")
                                                print(f"New Address : {b}")
                                                print(f"New City    : {c}")
                                                print(f"New Phone   : {d}")

                                                conf = input(f"\nDo you wish to create data for {newkey}? (y/n): ")
                                                if conf == 'y':
                                                    user[newkey] = [a,b,c,d,0,{}]
                                                    input("\nNew user has been added!\nPress enter to continue...")

                                elif admInput == 3:
                                    #EDIT USER
                                    while True:
                                        listUser(user)
                                        x = getCode(user, "updated", "user")
                                        if x != 0:
                                            break
                                    if x == 'CANCEL':
                                        break
                                    else:
                                        while True:
                                            cleartrm()
                                            print(f"\n\nSelect Update Type for {x}")
                                            print("--------------------")
                                            print("1. Partial Update")
                                            print("2. Full Update")
                                                   
                                            inp = input("\nSelect number of choice : ")

                                            if inp == '1':
                                                while True:
                                                    cleartrm()
                                                    print("\n\nSelect Column")
                                                    print("--------------------")
                                                    print("1. Name")
                                                    print("2. Address")
                                                    print("3. City")
                                                    print("4. Phone Number")
                                                    inp2 = input("\nSelect number of choice : ")

                                                    if inp2 == '1':
                                                        partialupdate("Name",user,x,0)        
                                                        break

                                                    elif inp2 == '2':
                                                        partialupdate("Address",user,x,1)
                                                        break

                                                    elif inp2 == '3':
                                                        partialupdate("City",user,x,2)
                                                        break
                                                    elif inp2 == '4':
                                                        while True:
                                                            parinp = input("\nEnter new user's phone : ")
                                                            if parinp == "":
                                                                print("Input cannot be blanked! \n")
                                                            elif parinp.isnumeric() == False or len(parinp) != 10:
                                                                print("Enter valid number!\n")    
                                                            else:
                                                                break 

                                                        parinp = format_phonenum(parinp) 
                                                        cleartrm()       
                                                        print(f"\nNew phone : {parinp}")
                                                        conf1 = input("\nDo you wish to proceed with the update? (y/n) : ")
                                                        if conf1 == 'y':
                                                            user[x][3] = parinp
                                                            input("\nUser updated!\nPress enter to continue...")
                                                            break
                                                        else:
                                                            break
                                                    else:
                                                        print("\nInvalid choice!")
                                                        sleep()
                                                break
      
                                            elif inp == '2':
                                                cleartrm()
                                                a,b,c,d = fillUser('')
                                                if a == "cancel":
                                                    break                                 
                                                d = format_phonenum(d)
                                                cleartrm()
                                                print(f"\n\nNew Data")
                                                print("---------------")
                                                print(f"New Name    : {a}")
                                                print(f"New Address : {b}")
                                                print(f"New City    : {c}")
                                                print(f"New Phone   : {d}")

                                                conf = input(f"\nDo you wish to update the data for {x}? (y/n): ")
                                                if conf == 'y':
                                                    for i,j in enumerate([a,b,c,d]):
                                                        user[x][i] = j.title()
                                                    input("\nUser updated!\nPress enter to continue...")
                                                    break
                                                else:
                                                    break
                                            else:
                                                print("\nInvalid choice!")
                                                sleep()

                                elif admInput == 4:
                                    #DELETE USER
                                    while True:
                                        listUser(user)
                                        x = getCode(user, "deleted", "user")
                                        if x != 0:
                                            break                          
                                    if x == 'CANCEL':
                                        break
                                    else:
                                        if len(user[x][5]) > 0:
                                            input("\nUser cannot be deleted! User still has items in cart!\nPress enter to continue...")
                                        else:
                                            cleartrm()
                                            print(f"\n\n{x}")
                                            print("---------------")
                                            print(f"Name    : {user[x][0]}")
                                            print(f"Address : {user[x][1]}")
                                            print(f"City    : {user[x][2]}")
                                            print(f"Phone   : {user[x][3]}")

                                            conf = input(f"\nDo you wish to delete {x} data? (y/n): ")
                                            if conf == 'y':
                                                user.pop(x)
                                                if x in transaction_history_amount:
                                                    transaction_history_amount.pop(x)
                                                input("\nUser deleted!\nPress enter to continue...")
                                            else:
                                                input("\n\nPress enter to continue...")

                                elif admInput == 5:
                                    #VIEW ALL ITEMS
                                    cleartrm()
                                    listItem(item)
                                    input("\nPress enter to continue...")

                                elif admInput == 6:
                                    #ADD ITEM
                                    cleartrm()
                                    last_int = getlastkeyint(item)
                                    a,b,c,d,e = fillItem("('cancel' to cancel)")
                                    if a == "Cancel":
                                        break
                                    newkey = "ITEM"+str(last_int+1).zfill(3)
                                    cleartrm()
                                    print(f"\n\n{newkey}")
                                    print(f"Name          : {a}")
                                    print(f"Price         : {b}")
                                    print(f"Stock         : {c}")
                                    print(f"Discount Rate : {d}")
                                    print(f"Category      : {e}")
                                    conf = input(f"\nDo you wish to add this item ? (y/n): ")
                                    if conf == 'y':
                                        item[newkey] = [a.title(),b,c,d,e.title()]
                                        input("\nNew item has been added!\nPress enter to continue...")

                                elif admInput == 7:
                                    #EDIT ITEM
                                    while True:
                                        listItem(item)
                                        x = getCode(item, "updated", "item")
                                        if x != 0:
                                            break                                       
                                    if x == 'CANCEL':
                                        break
                                    else:
                                        cleartrm()
                                        a,b,c,d,e = fillItem("")
                                        if a == "cancel":
                                            break                                        
                                        a = a.title()
                                        e = e.title()

                                        cleartrm()
                                        print(f"\n\n{x}")
                                        print(f"Name          : {a}")
                                        print(f"Price         : {b}")
                                        print(f"Stock         : {c}")
                                        print(f"Discount Rate : {d}")
                                        print(f"Category      : {e}")
                                        conf = input(f"\nDo you wish to update the item ? (y/n): ")
                                        if conf == 'y':
                                            for i,j in enumerate([a,b,c,d,e]):
                                                item[x][i] = j
                                            input("\nItem updated!\nPress enter to continue...")

                                elif admInput == 8:
                                    #DELETE ITEM
                                    while True:
                                        listItem(item)
                                        x = getCode(item, "deleted", "item")
                                        if x != 0:
                                            break       
              
                                    if x == 'CANCEL':
                                        break
                                    else:
                                        dictdel = []
                                        for i in user:
                                            if i == "ADMIN":
                                                continue
                                            elif x in user[i][5]:
                                                dictdel.append(x)     
                                        if len(dictdel) > 0:
                                            input("\nItem cannot be deleted! Item still in customer's cart!\nPress enter to continue...")   
                                        else:
                                            conf = input(f"\nDo you wish to delete this item ? (y/n):")
                                            if conf == 'y':
                                                item.pop(x)
                                                input("\nItem deleted!\nPress enter to continue...")

                                elif admInput == 9:
                                    #SEARCH USER DETAILS
                                    cleartrm()
                                    while True:
                                        listUser(user)
                                        x = getCode(user, "searched for details", "user")
                                        if x != 0:
                                            break                                        

                                    if x == 'CANCEL':
                                        break
                                    else:
                                        totalTransaction = transaction_history.count(x)
                                        cartitemcount = len(user[x][5])
                                        sumtransaction = 0
                                        if x in transaction_history_amount:
                                            sumtransaction = transaction_history_amount[x]

                                        showuserdetails(user, sumtransaction, cartitemcount, totalTransaction, x)

                                elif admInput == 10:
                                    #VIEW PROCESSED TRANSACTIONS
                                    while True:
                                        cleartrm()
                                        print()
                                        showpt(processed_transaction)                

                                        if len(processed_transaction) > 0:
                                            ptid = [i[0] for i in processed_transaction]
                                            ptinp = input("\nEnter transaction ID you want to complete ('cancel' to cancel): ").upper()
                                        
                                            if ptinp in ptid:
                                                processed_transaction = [i for i in processed_transaction if i[0] != ptinp]
                                                input("\nTransaction has been completed!\nPress enter to continue...")
                                                break
                                            elif ptinp == 'CANCEL':
                                                break
                                            else:
                                                print("\nTransaction not found!\n")
                                                sleep()
                                        else:
                                            input("\nNo ongoing transaction!\nPress enter to continue...")
                                            break

                                elif admInput == 11:
                                    #EXIT ADMIN MENU
                                    exitmen()
                                    flag3 = 0
                                    flag2 = 0
                                    break                                 
                            else:
                                print("Menu range invalid!\n")
                                sleep()
                        except:
                            print("Input Invalid!\n")
                            sleep()

        elif userKey in user.keys():
            while True:
                try:
                    welcomingGreetings(userKey)
                    menuCustomer()
                    cusInput = int(input("Enter menu number : "))
                    if 1 <= cusInput <= 9:
                        #VIEW ALL ITEM
                        if cusInput == 1:
                            tempdict = item
                            if len(tempdict) > 0:
                                while True:
                                    cleartrm()
                                    print(f"\n-== Showing all items ==-")
                                    showTempDict(tempdict)
                                    addcart =  getCode(tempdict, "added to cart", "item")
                                    if addcart != 0:
                                        break      
                                if addcart == 'CANCEL':
                                            break
                                else:
                                    addtocart(item,user,addcart,userKey)

                                itemaddednotif()   
                            else:
                                input("\nPress enter to continue...")

                        elif cusInput == 2:
                                #SEARCH FOR ITEMS
                                while True:
                                    cleartrm()
                                    searchinp = input("\nWhat do you want to buy? ('cancel' to cancel) : ").strip().lower()
                                    if searchinp == "":
                                        print("\nInput cannot be blank!")
                                        sleep()
                                    elif searchinp == 'cancel':
                                        break
                                    else:
                                        tempdict = {i: item.get(i) for i in item if searchinp in item[i][0].lower()}

                                        cleartrm()
                                        if len(tempdict) > 0:
                                            while True:
                                                cleartrm()
                                                print(f"\n-== Showing items result for {searchinp} ==-")
                                                showTempDict(tempdict)
                                                addcart =  getCode(tempdict, "added to cart", "item")
                                                if addcart != 0:
                                                    break    
                                            if addcart == 'CANCEL':
                                                        break
                                            else:
                                                addtocart(item,user,addcart,userKey)
                                            itemaddednotif() 
                                            break  
                                        else:
                                            input("\nPress enter to continue...")
                                            break

                        elif cusInput == 3:
                                #VIEW ITEMS ON SALE
                                tempdict = {i: item.get(i) for i in item if item[i][3] > 0}
                                tempdict = dict(sorted(tempdict.items(), key = lambda i:i[1][3], reverse= True))
                                cleartrm()
                                
                                if len(tempdict) > 0:
                                    while True:
                                        cleartrm()
                                        print(f"\n-== Showing items on sale from highest to lowest discount rate ==-")
                                        showTempDict(tempdict)
                                        addcart =  getCode(tempdict, "added to cart", "item")
                                        if addcart != 0:
                                            break    
                                    if addcart == 'CANCEL':
                                                break
                                    else:
                                        addtocart(item,user,addcart,userKey)

                                    itemaddednotif()   
                                else:
                                    input("\nPress enter to continue...")                           
                                
                        elif cusInput == 4:
                            #VIEW ITEMS BY CATEGORY
                            category = []
                            for i in item:
                                if item[i][4] not in category:
                                    category.append(item[i][4])
                            category.sort()
                            cleartrm()
                            while True:
                                cleartrm()      
                                print("\nAvailable Category : \n")
                                for i in category:
                                    print("- "+i)
                                catinput = input("\n\nEnter category you wish to see : ").strip().title()
                                if catinput in category:
                                    break
                                else:
                                    print("Category Invalid! \n")
                                    sleep()

                            tempdict = {i: item.get(i) for i in item if item[i][4] == catinput}
                            cleartrm()
                        
                            if len(tempdict) > 0:
                                while True:
                                        cleartrm()
                                        print(f"\n-== Showing items in {catinput} category ==-") 
                                        showTempDict(tempdict)
                                        addcart =  getCode(tempdict, "added to cart", "item")
                                        if addcart != 0:
                                            break    
                                if addcart == 'CANCEL':
                                            break
                                else:
                                    addtocart(item,user,addcart,userKey)

                                itemaddednotif()   
                            else:
                                input("\nPress enter to continue...")

                        elif cusInput == 5:
                            #VIEW ITEMS BY PRICE RANGE
                            cleartrm()
                            listRange = get_price_range()
                            listRange = [int(i) for i in listRange]
                            listRange.sort()
                            cleartrm()
                            tempdict = {i: item.get(i) for i in item if listRange[0]<= item[i][1] <= listRange[1]}
                            tempdict = dict(sorted(tempdict.items(), key = lambda i:i[1][1]))
                            
                            if len(tempdict) > 0:
                                while True:
                                        cleartrm()
                                        print(f"\n-== Showing items ranging between ${listRange [0]} and ${listRange [1]} ==-") 
                                        showTempDict(tempdict)
                                        addcart =  getCode(tempdict, "added to cart", "item")
                                        if addcart != 0:
                                            break                                
                                if addcart == 'CANCEL':
                                            break
                                else:
                                    addtocart(item,user,addcart,userKey)
                                    itemaddednotif()
                            else:
                                input("\nPress enter to continue...")
                                    
                        elif cusInput == 6:
                            #VIEW CART
                            cleartrm()
                            tempdict = user[userKey][5]
                            showcart(tempdict)

                            if len(tempdict) > 0:
                                print("\n\n- 'Clear' to clear your cart\n\n- Enter item code to remove individually\n\n- 'Back' to go back")
                                cc = input("\n\nInput : ").upper()
                                if cc == 'CLEAR':
                                    for i in tempdict:
                                        item[i][2] += tempdict[i][1]

                                    user[userKey][5].clear()
                                    input("\nCart has been cleared!\nPress enter to continue...")
                                
                                elif cc in tempdict:
                                    item[cc][2] += tempdict[cc][1]
                                    user[userKey][5].pop(cc)
                                    input("\nItem removed!\nPress enter to continue...")
                            else:
                                input("\nYour cart is empty!\nPress enter to continue...")

                        elif cusInput == 7:
                            #CHECK OUT CART
                            cleartrm()
                            tempdict = user[userKey][5]
                            grandtotal, totalqty = showcartcheckout(tempdict)

                            if len(tempdict) > 0:
                                address = user[userKey][1]
                                city = user[userKey][2]
                                phonenum = user[userKey][3]
                                print(f"\n\nTotal Quantity : {totalqty}")
                                print(f"Grand Total : {grandtotal}\n\n")
                                print(f"Deliver to \t\t: {address}, {city}")
                                print(f"Customer Contact Number : {phonenum}")
                                ccart = input("\n\nDo you want to check out items in your cart?\n('yes' to proceeed, 'back' to go back): ").lower()
                                
                                if ccart == 'yes':
                                    balance = user[userKey][4]

                                    if balance < grandtotal:
                                        print(f"\nInsufficient balance to checkout items!")
                                        print(f"Please add ${grandtotal - balance} to your balance!")
                                        input("\nPress enter to continue...")
                                    elif balance >= grandtotal:
                                        ptli = ptlastint(processed_transaction)
                                        newpt = "PT"+str(ptli+1).zfill(3)
                                        dd = user[userKey][5]
                                        aa = {dd[i][0] : dd[i][1] for i in dd}

                                        ptlist = [newpt, userKey, aa, address, city, phonenum]
                                        processed_transaction.append(ptlist)
                                        
                                        cartclearing_historyappending(userKey, transaction_history, transaction_history_amount, user, grandtotal)
                                        new_balance = balance_subtracting(balance, grandtotal)
                                        user[userKey][4] = round(new_balance,2)
                                        input("\n\nItems have been checked out!\nPress enter to continue...")

                            else:
                                input("\n\nYou don't have anything to check out!\nPress enter to continue...")

                        elif cusInput == 8:
                            #TOP UP BALANCE
                            while True:
                                try:
                                    cleartrm()
                                    print(f"\n-== Balance Top Up ==-") 
                                    balance = user[userKey][4]
                                    print(f"\n\nYour Balance : {balance}")
                                    conf = input("\n\nDo you want to top up your balance?\n('yes' to proceed, 'cancel' to cancel) : ").lower()
                                    if conf == 'yes':
                                        print()
                                        topupbal(user, userKey)
                                        input("\nTop Up Successful! \nPress enter to continue...")
                                    break
                                except:
                                    print("Invalid Input!")
                                    sleep()
                            
                        elif cusInput == 9:
                            #EXIT CUST MENU
                            exitmen()
                            flag2 = 0
                            break
                    else:
                        print("Menu range invalid!\n")
                        sleep()
                except:
                    print("Input Invalid!\n")
                    sleep()
                






















