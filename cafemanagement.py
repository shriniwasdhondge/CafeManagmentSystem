print("welcome sir")
print()
menu={"items":"prices(rs)","cofee":"50","burger":"80","sandwich":"70","pizza":"110","samosa":"25"}
#In the menu you can add the menu as you want
for key, value in menu.items():
    print(f'{key}:{value}')

print()
c=0
d=0
ordertotal=0
print("what would you like to have sir...")
item1=input()

if item1 in menu:
    print("good choice sir...!")
    quantity1=int(input(f"how much is the quantity of {item1} do you want : "))
    c=int(menu[item1])

    
else:
    print("sorry we don't have that sir")

print("anything else that you want to have sir")

item2=input()
if item2 in menu:
    print("ok")
    quantity2=int(input(f"how much is the quantity of {item1} do you want : "))
    d=int(menu[item2])
    print()
    ordertotal=c*quantity1+d*quantity2
    print("your bill is:",ordertotal)
    
else:
    print("ok sir , your order will be on your order very soon")
    ordertotal=c*quantity1
    print("your bill is:",ordertotal)
    





    


