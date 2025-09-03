
import ast
tasks=[]
def add():
    task=input("Enter a new task: ")
    tasks.append(task) 
    print("Task added successfully")
def delete():
    if not tasks:
        print("Empty")
    else:    
        print("The tasks are: ")
        for i,task in enumerate(tasks,start=1):
          print(f"{i}.{task}")
        index=input("Enter a task to delete: ")        
        tasks.remove(index)  
        print(f"{index} deleted successfully")  
def update():
 global tasks
 if not tasks:
        print("Empty")
 else:
       print("The tasks are: ")
       for i,task in enumerate(tasks,start=1):
        print(f"{i}.{task}")
       input1=input("Enter the task to update: ") 
       value1=input("Enter the new value: ") 
       input2=str(tasks)
       input2=input2.replace(input1,value1) 
       list_again=ast.literal_eval(input2)
    
       tasks=list_again
       print("Tasks updated successfylly")

def view():
        print("The tasks are: ")
        for i,task in enumerate(tasks,start=1):
         print(f"{i}.{task}")         
while True:
    print("-------TO-DO-LIST-------")

    print("1.Add task")   
    print("2.Delete Task")
    print("3.Update Task")
    print("4.View Task")
    print("5 Quit")
    choice=input("Enter a choice 1/2/3/4:  ")
    if(choice=="1"):
        add()
    elif(choice=="2"):  
      delete()  
    elif(choice=="3"):
       update()
    elif(choice=="4"):
        view()   
    elif choice=="5":
        print("Bye")   
        break 
    else:
        print("Invalid choice")    