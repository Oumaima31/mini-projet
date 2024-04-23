tasks=[]

   # add new task:
def addTask():
    task=input("Please enter a task :")
    tasks.append(task)
    print(f"task '{task}' added to the list.")

    # read the tasks of the list:
def listTask():
    if not tasks:
        print("there are no tasks currently.")
    else:
        print("current tasks :")
        for index, task in enumerate(tasks ,start=1):
           print(f"Task #'{index}'. '{task}' ")
            
    # delete a task from the list:
def deleteTask():
    listTask()
    try:
       taskToDelete=int(input("Enter the # to delete : ").strip())
       if taskToDelete>=0 and taskToDelete<len(tasks):
           tasks.pop(taskToDelete)
           print(f"task {taskToDelete} has been removed.")
       else:
           print(f"task #{taskToDelete} was not found.") 
    except:
        print("Invalid input.")    
    



if __name__=="__main__":
    # create a loop to run the app
    print("Welcome to the 'To-Do-List' app :)")
    while True:
        print("\n")
        print("Please select one of the following options:")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice=input("Enter your choice :")

        if(choice=="1"):
            addTask()
        elif(choice=="2"):
            deleteTask()
        elif(choice=="3"):
            listTask()
        elif(choice=="4"):
            break
        else:
            print("Invalid input,Please try again.")        

    print("Goodbye")               
