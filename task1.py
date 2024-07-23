def add(Non_veg_starter):
    starter = input("enter starter : ")
    Non_veg_starter.append(starter)
    print("added...")
    return  Non_veg_starter
 
def display(Non_veg_starter):
    print("===============Menu===================")
    for i in Non_veg_starter:
        print(i)
    print("======================================")
 
def update(Non_veg_starter):
    select = input(" enter starter name")
    if select in Non_veg_starter:
        ind = Non_veg_starter.index(select)
        updated=input("eneter updated name : ")
        Non_veg_starter[ind]=updated
        print("updated...")
        return Non_veg_starter
    print("entered is not in menu")
    return Non_veg_starter
   
def remove(Non_veg_starter):
    select = input(" enter starter name")
    if select in Non_veg_starter:
        Non_veg_starter.remove(select)
        print("removed...")
        return Non_veg_starter
    print("entered is not in menu")
    return Non_veg_starter
def main():
     Non_veg_starter = ['Chicken 65','chilly chicken','Butter Chicken']
     while True:
        print("1.Display Menu Card")
        print("2.Add Menu Card")
        print("3.Update Menu Card")
        print("4.Remove Menu Card")
        print("5.Exit")
        choice = int(input("enter choice"))
        if choice==1:
            display(Non_veg_starter)
        elif choice==2:
            Non_veg_starter = add(Non_veg_starter)
        elif choice==3:
            Non_veg_starter= update(Non_veg_starter)      
        elif choice==4:
            remove(Non_veg_starter)    
        elif choice==5:
            break
       
 
if __name__ == "__main__":
    main()