from time import strftime,gmtime,ctime
import mysql.connector

#connection to database
conn = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password = "sakthivel",
    database = "ATM"
)
cur=conn.cursor()

#create table atmusers(bank_id int primary key auto_increment,acc_user varchar(40) not null,
#acc_no int not null,atm_pin int not null, balance_amt int); 
#insert into atmusers(acc_user,acc_no,atm_pin,balance_amt) 
#values("sakthivel",123456,1234,40000);

print("\t\t(((((((((((( $ Welcome to Sakthivel ATM Machine & )))))))))))) ")

class atm:
    try:
        #Method to withdraw money
        list = []
        def withdraw(self):
            try:
                s = "SELECT * FROM atmusers"
                cur.execute(s)
                result = cur.fetchall()
                for draw in result:
                    self.amount = int(input("Enter your amount: "))
                    if self.amount < 0:
                        print("Oooops! :( Sorry Negative amount cannot withdraw.")
                    elif self.amount == 0:
                        print("Oooops! :( Sorry Zero amount cannot withdraw.")
                    elif self.amount <= draw[4]:
                        self.balance = draw[4] - self.amount
                        s = "UPDATE atmusers SET balance_amt=%s WHERE acc_no=%s"
                        b = (self.balance, card_number)
                        cur.execute(s, b)
                        conn.commit()
                        t = strftime("%d %b %Y %H:%M", gmtime())
                        atm.list.append([self.amount, t, "Withdrawed"])
                        print(f"Successfully debited {format(self.amount, ',.2f')} Rs. from your current account :)")
                        print(f"Current balance is {format(self.balance, ',.2f')} Rs.\n")
                    else:
                        print("Insufficient balance!!!...:(")
                    break
            except:
                print("Please enter valid amount!!!:(")

        def Deposit_amount(self):
            #method to Deposit money
            try:
                s="SELECT * FROM atmusers"
                cur.execute(s)
                result=cur.fetchall()
                for dep in result:
                    self.amount = int(input("Enter your amount: "))
                    self.balance = dep[4] + self.amount
                    s="UPDATE atmusers SET balance_amt=%s WHERE acc_no=%s"
                    b=(self.balance,card_number)
                    cur.execute(s,b)
                    conn.commit()
                    print(f"Successfully credited {format(self.amount, ',.2f')} Rs. to your account.:)")
                    print(f"Current balance is {format(self.balance, ',.2f')} Rs.\n")
                    t = strftime("%d %b %Y %H:%M", gmtime())
                    atm.list.append([self.amount, t, "Deposited"])
                    break
            except:
                print("Please enter valid amount!:(")
    except:
        print("Getting Errors so Refresh again Try! :(")

try:
    choise = int(input(" Select 1: Register 2: Login "))
    if choise==1:
        #registration for new user
        card_num=int(input("Enter your 6-digit account number: "))
        s = "SELECT * FROM atmusers"
        cur.execute(s)
        result = cur.fetchall()
        for rec in result:
            if card_num ==rec[1]:
                print("Enter valid card number!Card number already exists :(")
                break
            else:
                user_name = input("Enter your first and last name: ")
                pin = int(input("Set pin for your account: "))
                conf_pin = int(input("Confirm pin: "))
                balance = int(input("Enter balance in your account: "))
                if pin == conf_pin:
                    s = "INSERT INTO atmusers (acc_user,acc_no,atm_pin,balance_amt) VALUES(%s,%s,%s,%s)"
                    b = (user_name, card_num, pin, balance)
                    cur.execute(s,b)
                    conn.commit()
                    print("Sucessfully registered. :)")
                else:
                    print("Please enter valid pin!:(")
                break
    elif choise==2:
        #log in
        card_num=int(input("Enter your account number: "))
        s="SELECT * FROM atmusers"
        cur.execute(s)
        result=cur.fetchall()
        for prs in result:
            if card_num==prs[2] :
                card_number=prs[2]
                password=prs[3]
                name=prs[1]
                pin=int(input("Enter pin:"))
                while pin == prs[3]:
                    try:
                        print(f"\n Welcome {name}..")
                        print("1.Deposit Money\n2.Withdraw Money\n3.Balance Enquiry\n4.Mini Statement\n5.Pin Change\n6.Quit")
                        option = int(input("\nSelect Choice 1,2,3,4,5 or 6: "))
                        print()
                        obj = atm()
                        if option == 1:
                            obj.Deposit_amount()
                        elif option == 2:
                            obj.withdraw()
                        elif option == 3:
                            s = "SELECT * FROM atmusers WHERE acc_no=%s AND atm_pin=%s"
                            b=(card_number,password)
                            cur.execute(s,b)
                            result = cur.fetchall()
                            for prs in result:
                                print(f"Available Balance: Rs.{prs[4]}\n")
                        elif option == 4:
                            print("\t\tMini Statement")
                            print(f'''{strftime("%d %b %Y %H:%M", gmtime())}''')
                            print(f"CARD NO.{card_number}")
                            for i in range(len(atm.list)):
                                print(f'''{atm.list[i][1]} \t {atm.list[i][0]}Rs. {atm.list[i][2]}\n''')
                        elif option == 5:
                            try:
                                current_pin = int(input("Enter Current Pin :"))
                                for prs in result:
                                    while current_pin == prs[3]:
                                        try:
                                            new_pin = int(input("Enter New Pin: "))
                                            confirm_pin = int(input("Confirm New Pin: "))
                                            if new_pin == confirm_pin:
                                                s="UPDATE atmusers SET atm_pin=%s WHERE acc_no=%s"
                                                b=(new_pin,card_number)
                                                cur.execute(s,b)
                                                conn.commit()
                                                print("Your pin has been changed successfully!\n")
                                                try:
                                                    f = open("pass.txt", "w")
                                                    f.write(f"Your Current Pin is {pin}")
                                                    f.close()
                                                except:
                                                    print("")
                                                try:
                                                    pin_num = int(input("Enter new pin: "))
                                                except:
                                                    print("Invalid pin :(")
                                                break
                                            else:
                                                print("Pin did not match :( try again!")
                                        except:
                                            print("Please Enter valid pin :(")
                                    else:
                                        print("Invalid current pin:(")

                            except:
                                print("Please Enter valid pin!!!...:(")
                        elif option == 6:
                            pass
                            print("\t\n$$$ (: Thanks for Using Sakthivel ATM Machine :) $$$!!!")
                            break
                        else:
                            print("Please select valid option!!!...:(")
                    except:
                        print("Please select valid option!!!...:(")
                else:
                    print("Invalid pin, Try again!:(")
except:
    print("please users Enter valid input:(")