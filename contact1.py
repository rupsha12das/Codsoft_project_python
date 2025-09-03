contacts={}
def is_valid_email(Email):
      
      if "@" not in Email:
        return False 
      
      parts=Email.split("@")  
      if len(parts)!=2:
        return False
      username,domain=parts
      if not username or not domain:
         return False
     
      if "." not in domain:
         return False
      if domain.startswith(".") or domain.endswith("."):
         return False
      return True
def add():
    name=input("Enter the name: ")
    phone=input("Enter the phone number: ")
    Email=input("Enter the Email id: ")
    Address=input("Enter the Address: ")
    if  name.isalpha() and phone.isdigit() and len(phone)==10 and is_valid_email( Email) :
     contacts[name]={"phone":phone,"Email":Email,"Address":Address}
     print(f"Contacts for {name } added sucessfully")
     
    else:
     print("Invalid! Name should be in alphabates and Phone number must be exactly 10 digits and email should be in valid format")
def view():
    if not contacts:
        print("No contacts found")
    else:
        for name,info in contacts.items():
            print(f"Name:{name}")        
            print(f"Phone:{info['phone']}") 
            print(f"Email:{info['Email']}") 
            print(f"Address:{info['Address']}") 
def search():
    search1=input("Enter name or phone no. to search : ")
    found=False
    for name,info in contacts.items():
       if search1.lower()==name.lower() or search1==info['phone']:
           
            print(f"Name:{name}")
            print(f"Phone:{info['phone']}")
            print(f"Email:{info['Email']}")
            print(f"Address:{info['Address']}")
            found=True
            break
       if not found:
            print("No contacts found")        
def update():
     for name,info in contacts.items():
            print(f"Name:{name}")        
            print(f"Phone:{info['phone']}") 
            print(f"Email:{info['Email']}") 
            print(f"Address:{info['Address']}") 
     update1=input("Enter the name to search for update: ")
     if update1 not in contacts:
        print("Contacts not found")
        return
     info=contacts[update1]
     print(f"Cureent Info->\n Phone:{info['phone']}\n Email:{info['Email']}\n Address:{info['Address']}\n")
     while True:
        print("What do you want to update")
        print("1.Name")
        print("2.Phone")
        print("3.Email")
        print("4.Address")
        print("5.Done")
        choice=input("Enter your choice(1-5): ")
        if choice=="1":
            new=input("Enter your name: ")
            if new.isalpha():
                contacts[new]=contacts.pop(update1)
                update1=new
            print("Named updated successfully")
        elif choice=="2":
              new=input("Enter your phone number: ")  
              if new.isdigit() and len(new)==10:
               contacts[update1]["phone"]=new
               print("Phone number updated successfully")
              else:
                  print("Phone number must be exactly 10 digits")  
              
        elif choice=="3":
              new=input("Enter your Email: ")  
              if is_valid_email(new):
               contacts[update1]["Email"]=new
               print(" Eamil updated successfully") 
              else:
                  print("Invalid format") 
        elif choice=="4":
              new=input("Enter your Address: ")  
              contacts[update1]["Address"]=new
              print("Adderss updated successfully") 

        elif choice=="5":
            print("Update process finished")
            break
        else:
            print("Invalid choice! Please enter 1-5")    
def delete():
    delete1=input("Enter the name for delete: ")
    if not contacts:
        print(f"{delete1} not Exists")
    else:
        del contacts[delete1]
        print(f"{delete1} Deleted Successfully")    

while True:
     print("----Contact Book-------")
     print("1.Add Contact")
     print("2.View Contact")
     print("3.Search Contact")
     print("4.Update Contact")
     print("5.Delete Contact")
     choice=input("Enter the option: ")
     if choice=="1":
         add()
     elif choice=="2":
         view() 
     elif choice=="3":
         search()  
     elif choice=="4":
         update()    
     elif choice=="5":
         delete()   
     else:
         print("Invalid choice! please choose from 1/2/3/4/5")     
    

