tasks=[]
while True:
  print("\nTask Manager")
  print("1. Add task")
  print("2. Show task")
  print("3. Exit")
  choise=input("Choose an option (1-3):")
  if choise =="1":
    task=input("Enter a new task:")
    tasks.append(task)
    print("Task added")
  elif choise =="2":
    if not tasks:
      print("No tasks yet")
    else:
      print ("\nYour tasks:")
      for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
  elif choise =="3":
    print("byyee")
    break
  else:
    print("Invalid choise. Try aagain")
    
      
  
