#Inventory Management System 
#Project by Utkarsh Saxena and Dushyant Purohit 


#Dictionaries
unit_price={}
description={}
stock={}

#Open file with stock
details = open("stock.txt","r")

#First line of the file is the number of items
no_items  = int((details.readline()).rstrip("\n"))

#Add items to dictionaries
for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    x2=float(x2)
    unit_price.update({x1: x2})

for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    description.update({x1: x2})

for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    x2=int(x2)
    stock.update({x1: x2})

details.close()

#List to store the items purchased
cart=[]

c="y" #Runs the while loop as long as user wants


#Instructions
print()
print("Welcome to Inventory Management Software ")
print()
print("A-Add an item")
print("R-Remove an item")
print("E-Edit specifics of an item")
print("L-List all items")
print("I-Inquire about a item")
print("P-Add to cart to sell item")
print("C-Checkout")
print("S-Show all items purchased")
print("Q-Quit")
print("remove-Remove an item from the cart")
print("help-See all commands again")
print()


total_cost=0 
flag=0 #To check if they have checked out


while(c!= "q" or c!= "Q"):
    c= input("What would you like to do? ")
    
    if(c=="q" or c=="Q"):
        break
        
    elif(c=="A" or c=="a"):#Add a item
        i_no = int(input("Enter item number: "))
        i_pr = float(input("Enter item price: "))
        i_desc = input("Enter item description: ")
        i_stock = int(input("Enter item stock: "))
        
        m=0
        for i in range(0,len(unit_price)):
            if(i_no in unit_price):
                i_no+=1
                m=1
        if(m==1):
            print()
            print("That item number already exists :(, changing value to ",i_no)
                
        unit_price.update({i_no: i_pr})
        description.update({i_no: i_desc})
        if(i_stock > -1):
            stock.update({i_no: i_stock})
        else:
            i_stock = 0
            stock.update({i_no: i_stock})
            print("The stock of an item cannot be negative, the stock has been set to 0.")
        print()
        print("item number: ",i_no," Description: ",description.get(i_no)," Price: ",unit_price.get(i_no)," Stock: ",stock.get(i_no))
        print("item was added successfully!")
        print()
        
    elif(c=="E" or c=="e"):#Edit an item
        print()
        i_no=int(input("Enter item Number: "))
        if(i_no in unit_price):
            print()
            print("item number: ",i_no," Description: ",description.get(i_no)," Price: ",unit_price.get(i_no)," Stock: ",stock.get(i_no))
            if(stock.get(i_no)<3 and stock.get(i_no)!=0):
                print("Only ",stock.get(i_no),"left!!")
            print()
        else:
            print("No item found!")
            print()
        
        if(i_no in unit_price):
            i_pr = float(input("Enter item price: "))
            i_desc = input("Enter item description: ")
            i_stock = int(input("Enter item stock: "))
                
            unit_price.update({i_no: i_pr})
            description.update({i_no: i_desc})
            stock.update({i_no: i_stock})
            
        else:
            print("That item does not exist, to add an item use a")
        print()
    
            
    elif(c=="R" or c=="r"):#Remove an item
        print()
        i_no = int(input("Enter item number: "))
        if(i_no in unit_price):
            are_you_sure = input("Are you sure you want to remove that item(y/n)? ")
            if(are_you_sure=="y" or are_you_sure=="Y"):
                unit_price.pop(i_no)
                description.pop(i_no)
                stock.pop(i_no)
                print("Item successfully removed!")
            print()
        else:
            print("Sorry, we don't have such an item!")
            print()
        
    elif(c=="L" or c=="l"):#List all the items
        print()
        print("items and their prices: ",unit_price)
        print("Descriptions: ",description)
        print("Stock left of Item: ",stock)
        print()

    elif(c=="I" or c=="i"):#Inquire about a item
        print()
        i_no=int(input("Enter item Number: "))
        if(i_no in unit_price):
            print()
            print("item number: ",i_no," Description: ",description.get(i_no)," Price: ",unit_price.get(i_no)," Stock: ",stock.get(i_no))
            if(stock.get(i_no)<3 and stock.get(i_no)!=0):
                print("Only ",stock.get(i_no),"left!!")
            print()
        else:
            print("No item found!")
            print()
        
    elif(c=="P" or c=="p"):#Add to cart to sell item 
        print()
        i_no = int(input("Enter item number: "))
        i_quant = int(input("Enter item quantity: "))
        i_desc = description.get(i_no)
        if(i_no in unit_price):
            if(flag==1):
                flag=0
            stock_current = stock.get(i_no)
            if(stock_current>0):
                stock_current = stock.get(i_no)
                stock[i_no] = stock_current-i_quant
                if(stock[i_no]<0):
                    print("Only ",stock_current,"quantity left, selling ",stock_current," ",i_desc)
                    stock[i_no]=0
                    item_price = unit_price.get(i_no)
                    total_cost = total_cost+item_price*stock_current
                    print(description.get(i_no),"added to cart: ","₹",item_price ,"Each")
                    cart.append([i_no,i_desc,"quantity "+str(stock_current)])#Stores item in cart
                else:
                    item_price = unit_price.get(i_no)
                    total_cost = total_cost+item_price*i_quant
                    print(description.get(i_no),"added to cart: ","₹",item_price ,"Each")
                    cart.append([i_no,i_desc,"quantity "+str(i_quant)])#Stores item in cart
                
            else:
                print("Sorry! We don't have that item in stock!")
        else:
                print("Sorry! We don't have such an item!")
        print()
        
    elif(c=="C" or c=="c"):#Check out
        print()
        print("You sold the following items: ",cart)
        print("Total: ","₹",round(total_cost,2))
        tax= round(0.18*total_cost,2)
        print("Tax is 18%: ","₹",tax)
        total = round(total_cost+tax,2)
        print("After Tax: ","₹",total)
        total_cost=0
        flag=1
        print()
        print("You can still sell items after check out, your cart has been reset. To quit press q")
        print()
        cart.clear()
        
    elif(c=="help"):#Display all commands
        print()
        print("Help Centre")
        print("A-Add an item")
        print("R-Remove an item")
        print("E-Edit specifics of an item")
        print("L-List all items")
        print("I-Inquire about a item")
        print("P-Add to cart to sell item")
        print("C-Checkout")
        print("S-Show all items purchased")
        print("remove-Remove an item from the cart")
        print("help-See all commands again")
        print("If you have any other questions or concerns please contact the manager.")
        print()
        
    elif(c=="remove" or c=="Remove"):#To remove an item from the cart
        print()
        are_you_sure = input("Are you sure you want to remove an item from the cart(y/n)? ")
        if(are_you_sure=="y"):
            i_no = int(input("Enter item number to remove from cart: "))
            if(i_no in cart):
                stock_current = stock.get(i_no)
                stock[i_no] = stock_current+1
                item_price = unit_price.get(i_no)
                total_cost = total_cost-item_price
                j=0
                for i in range(0,len(cart)):#To find the index of the item in the list cart
                    if(i==i_no):
                        j=i

                cart.pop(j)
                print(description.get(i_no),"removed from cart: ")
                print()
            else:
                print()
                print("That item is not in your cart!")
                print()
                
    elif(c=="s" or c=="S"):#prints list cart
        print()
        print(cart)
        print()
        
    else:
        print()
        print("ERROR! Contact manager for help!")
        print()


#Outputs total if the user quits without checking out
if(total_cost>0 and flag==0):
    print()
    print("You bought: ",cart)
    print("Total: ","₹",round(total_cost,2))
    tax= round(0.18*total_cost,2)
    print("Tax is 18%: ","₹",tax)
    total = round(total_cost+tax,2)
    print("After Tax: ","₹",total)
    
print()
print("Thank you for using IMS")

#Writing  the updated inventory to the file
details = open("stock.txt","w")
no_items=len(unit_price)
details.write(str(no_items)+"\n")
for i in range(0,no_items):
    details.write(str(i+1)+"#"+str(unit_price[i+1])+"\n")
    
for i in range(0,no_items):
    details.write(str(i+1)+"#"+description[i+1]+"\n")
    
for i in range(0,no_items):
    details.write(str(i+1)+"#"+str(stock[i+1])+"\n")
    
details.close()
