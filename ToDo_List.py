'''
shape of app
----------------------------------------------------------
ToDo List
------------
(enter) what do you want (add , view , remove , exit) ?
==> 
-----------
'''
# intro of App
print("\n\n----------------------------------------------------------")
print("ToDo List")


#list of tasks
tasks = []

while True :
    # your task
    # print("------------\n")
    task = input(" what do you want (add , view , remove , exit) ? \n ==> ").lower().strip()
    print("----------------------------------------\n")
    


    # types of tasks

    if task == "add" :
        additional_task = input("add new task : ")
        tasks.append(additional_task)
        print("addition done")

        print("----------------------------------------\n")

    elif task == "exit" :
        exit()  # break

    elif task == "view" :
        #print(tasks)
        if len(tasks) != 0 :
            print("My tasks : ")
            for t in tasks :
                print(t)  
        else :
            print("there are not any tasks")        
        print("----------------------------------------\n")     

    elif task == "remove" :
        if len(tasks) != 0 :
            del_task = input("enter task that you delete : ")
            if del_task in tasks :
                tasks.remove(del_task)
                print("removal done")
            else:
                print(f"task : {del_task} isn't exsit")    
        else :
            print("there are not any tasks")        
        print("----------------------------------------\n")  
   

    # elif task == "remove" :
    #     if len(tasks) != 0 :
    #         tasks.clear() 
    #         print("delete all tasks")
    #     else :
    #         print("there are not any tasks")        
    #     print("----------------------------------------\n")  

    else :
        print("you enter uncorrect task , retry again ") 
print("----------------------------------------")


    ## other shape ##
#     task = input("""
#  --------     ---------     --------      ----------
#   (1) Add     (2) view      (3) exit      (4) remove
#  --------     ---------     --------      ----------  

#       select one of these button (1,2,3,4)  : 
#       ==> """)
