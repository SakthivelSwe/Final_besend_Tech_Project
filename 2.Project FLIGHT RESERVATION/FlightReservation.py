import pandas as p
import mysql.connector
import warnings

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sakthivel",
    database = "flight"
)
#print(con)
def menus():
    print()
    print("*"*85)
    print("FLIGHT RESERVATION".center(70))
    print("*"*85)
    print("1. Add New Passenger Details")
    print("2. Add Food Items Details")
    print("3. Show Food Menus")
    print("4. Search by Food item name")
    print("5. Delete food item details if no more available")
    print("6. Add new Charges for more weights")
    print("7. Show all types of Seats and their Ticket Price")
    print("8. Show Type of Seats Passengers has chosen and its Ticket Price")
    print("9. If Extra luggage then its Bill")
    print("10. If Food items ordered the its Bill")
    print("11. Exit")
    print("*"*87)
menus()
    
#Add Passengers Function
def add_pass():
    warnings.filterwarnings('ignore')
    add_pass = con.cursor()
    list = []
    name = input("Enter Your Name: ")
    list.append(name)
    address = input("Enter Your Address: ")
    list.append(address)
    phone = input("Enter your phone number: ")
    list.append(phone)
    res_date = input("Enter your Reservation date: ")
    list.append(res_date)
    sou = input("Enter your source: ")
    list.append(sou)
    des = input("Enter your Destination: ")
    list.append(des)
    passing = (list)
    query = "insert into passengers(p_name,p_address,p_mobile,res_date,source,destination) values(%s,%s,%s,%s,%s,%s)"
    add_pass.execute(query,passing)
    con.commit()
    print("Passenger Your Record is inserted")
    


def add_clstype():
    cls = con.cursor()
    show = p.read_sql("select * from clstype",con)
    print(show)
    list = []
    sno = input("Enter the Serial No: ")
    list.append(sno)
    type = input("Enter the Class type: ")
    list.append(type)
    rate = input("Enter the rate of per Ticket: ")
    list.append(rate)
    passing = (list)
    query = "insert into clstype(sno,classtype,rate) values(%s,%s,%s)"
    cls.execute(query,passing)
    con.commit()
    print("Classtype Record inserted.")

def add_food():
    warnings.filterwarnings('ignore')
    f = con.cursor()
    show = p.read_sql("select * from food",con)
    print(show)
    list = []
    sno = input("Enter the Serial No: ")
    list.append(sno)
    items = input("Enter the name of food items: ")
    list.append(items)
    rate = input("Enter the food of per item price: ")
    list.append(rate)
    passing = (list)
    query = "insert into food(sno,itemname,rate) values(%s,%s,%s)"
    f.execute(query,passing)
    con.commit()
    print("Food iteam Record inserted.")
    

def displayfoodmenus():
    warnings.filterwarnings('ignore')
    print("AVAILABLE OF ALL FOOD ITEMS")
    show = p.read_sql("select * from food",con)
    print(show)
    

def search_food_items():
    displayfoodmenus()
    warnings.filterwarnings('ignore')
    print("Search Rate of Food item by enter food item serial No.")
    a = float(input("Enter food item Serial no: "))
    query = "select * from food where sno=%s"%(a,)
    show = p.read_sql(query,con)
    print(show)
    

def delete_food_item():
    warnings.filterwarnings('ignore')
    print("Any Changes in food menus")
    show = p.read_sql("select * from food",con)
    print(show)
    print()
    dele = con.cursor()
    del_item = input("Enter Delete item name: ")
    query=dele.execute("delete from food where itemname = %s")
    dele.execute(query,del_item)
    dele.commit()
    print("Record deleted")
    show = p.read_sql("select * from food",con)
    print(show)
    dele.commit()

def add_lug():
    warnings.filterwarnings('ignore')
    lugg= con.cursor()
    show = p.read_sql("select * from luggages",con)
    print(show)
    sno = input("Enter the Serial No: ")
    list.append(sno)
    weight = input("Enter the weight of luggage: ")
    list.append(weight)
    rate = input("Enter the rate of luggage: ")
    list.append(rate)
    passing = (list)
    query = "insert into luggages(sno,weight,rate) values(%s,%s,%s)"
    lugg.execute(query,passing)
    con.commit()
    print("Luggage Record inserted.")

def ticket_res():
    warnings.filterwarnings('ignore')
    print("(SAKTHIVEL FLIGHT HAVA THE FOLLOW SEAT TYPE FOR YOU)")
    print("1. FIRST CLASS RS.6000 PER PERSON")
    print("2. BUSINESS CLASS RS.12000 PER PERSON")
    print("3. ECONOMY CLASS RS. 5000 PER PERSON")
    t = int(input("Enter your choice of Ticket type:::"))
    n = int(input("How many Tickets you want: "))
    if t==1:
        print("You have chose FIRST CLASS TICKET")
        cal = 6000*n
    elif t==2:
        print("You have chose BUSINESS CLASS TICKET")
        cal = 12000*n
    elif t == 3:
        print("You have chose ECONOMY CLASS TICKET")
        cal = 5000*n
    else:
        print("please choose currect class")
    print(f"Your Total Ticket Price is {cal}\n")

def lugg_bill():
    warnings.filterwarnings('ignore')
    ex = int(input("Enter serial no. of weight of extra luggages: "))
    if ex==1:
        print("You hava 30 kg Extra")
        extra = 3000
    elif ex==2:
        print("you hava 35 kg Extra")
        extra = 4000
    elif ex==3:
        print("you hava 40 kg Extra")
        extra = 5000
    elif ex==4:
        print("you have 45 kg Extra")
        extra = 6000
    elif ex ==5:
        print("you hava 50 kg Extra")
        extra = 7000
    else:
        print("Please choose a correct serial no")
    print(f"your cost of Extra Luggages is {extra}")

def food_bill():
    displayfoodmenus()
    warnings.filterwarnings('ignore')

    order = int(input("Order your food item serial no: "))
    n = int(input("Enter the quantity:"))
    if order == 1:
        tot = 30 * n
    elif order == 2:
        tot = 40 * n
    elif order == 3:
        tot = 70 * n
    elif order == 4:
        tot = 45 * n
    elif order == 5:
        tot = 50 * n
    else:
        print("Invalid Option")
    print(f"Total food bill = Rs{tot}\n")

def showticketprice():
    warnings.filterwarnings('ignore')
    print("All records of type of seats available")
    show = p.read_sql("select * from clstype",con)
    print(show)
while True:
    option = ""
    option = int(input("\nEnter your choices: "))
    if option == 1:
        add_pass()
    elif option == 2:
        add_food()
    elif option == 3:
        displayfoodmenus()
    elif option == 4:
        search_food_items()
    elif option == 5:
        delete_food_item()
    elif option == 6:
        add_lug()
    elif option == 7:
        showticketprice()
    elif option == 8:
        ticket_res()
    elif option == 9:
        lugg_bill()
    elif option == 10:
        food_bill()
    elif option == 11:
        exit()
        

    else:
        print("Invalid option ")





