print("\t(((((((((((((((->HOTAL MANAGEMENT<-))))))))))))))))")
print("\t>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
#list of veg items
veg_menu = ("idly","dhosa","pongal","pooriset","appam","oniondosa","oothappam","vegrice","medhuvada",
"uppuma")
#list of non-veg items
non_veg_menu = ("chickenbriyani","muttonbiriyani","eggrice","chicken65","muttoncurry",
"chickencurry","tandoorichicken","muttonkabab","chickenparotta")

dessert_menu = ("halwa","gulabjamun","rasmalai","ricekheer","kulfi","venillaicecream",
"chocolatecake")

category = input("Enter the category 'VEG' items  or 'NONVEG' or 'DESSERT' items: ").strip().upper()

if category in "VEG":
    #price
    idly = 5
    dhosa = 20
    pongal = 15
    pooriset =7
    appam = 40
    oniondosa = 60
    oothappam = 55
    vegrice = 45
    medhuvada = 20
    uppuma = 35

    order_dish = input("Order your dish:").lower().strip()
    if order_dish in veg_menu:
        print(f"your order {order_dish} Available in Menu list.")
        how_many = int(input(f"how many {order_dish} you want: "))
        if order_dish == "idly":
            total = idly * how_many
            print(f"Your Total bill is RS.{total}.")
        if order_dish == "dhosa":
            total = dhosa * how_many
            print(f"Your Total bill is RS.{total}.")
        if order_dish == "pongal":
            total = pongal * how_many
            print(f"Your Total bill is RS.{total}.")
        if order_dish == "pooriset":
            total = pooriset * how_many
            print(f"Your Total bill is RS.{total}.")
        if order_dish == "appam":
            total = appam * how_many
            print(f"Your Total bill is RS.{total}.")
        if order_dish == "oniondosa":
            total = oniondosa * how_many
            print(f"Your Total bill is RS.{total}.")
        if order_dish == "oothappam":
            total = oothappam * how_many
            print(f"Your Total bill is RS.{total}.")
        if order_dish == "vegrice":
            total = vegrice * how_many
            print(f"Your Total bill is RS.{total}.")
        if order_dish == "medhuvada":
            total = medhuvada * how_many
            print(f"Your Total bill is RS.{total}.")
        if order_dish == "uppuma":
            total = uppuma * how_many
            print(f"Your Total bill is RS.{total}.")
    else:
        print(f"Sorry Your order {order_dish} not Avalible this hotal menu")
        print(f"Show the Hotal veg menus:\n {veg_menu}")
elif category == "NONVEG":
    #price
    chicken_briyani = 120
    mutton_briyani = 180
    eggrice = 70
    chicken_65 = 90
    muttoncurry = 250
    chickencurry = 100
    tandoorichicken = 200
    muttonkabab = 130
    chickenparotta = 150
    order_dish = input("Order your dish:").lower().strip()
    if order_dish in non_veg_menu:
        print(f"your order {order_dish} Available in Menu list.")
        how_many = int(input(f"how many {order_dish} you want: "))
        if order_dish == "chickenbriyani":
            total = chicken_briyani * how_many
            print(f"Your Total bill is RS.{total}.")
        if order_dish == "muttonbriyani":
            total = mutton_briyani * how_many
            print(f"Your Total bill is RS.{total}.")
        if order_dish == "eggrice":
            total = eggrice * how_many
            print(f"Your Total bill is RS.{total}.")
        if order_dish == "chicken65":
            total = chicken_65 * how_many
            print(f"Your Total bill is RS.{total}.")
        if order_dish == "muttoncurry":
            total = muttoncurry * how_many
            print(f"Your Total bill is RS.{total}.")
        if order_dish == "chickencurry":
            total = chickencurry * how_many
            print(f"Your Total bill is RS.{total}.")
        if order_dish == "tandoorichicken":
            total = tandoorichicken * how_many
            print(f"Your Total bill is RS.{total}.")
        if order_dish == "muttonkabab":
            total = muttonkabab * how_many
            print(f"Your Total bill is RS.{total}.")
        if order_dish == "chickenparotta":
            total = chickenparotta * how_many
            print(f"Your Total bill is RS.{total}.")
    else:
        print(f"Sorry Your order {order_dish} not Avalible this hotal menu")
        print(f"Show the Hotal non veg menus:\n {non_veg_menu} ")


           
        
            

