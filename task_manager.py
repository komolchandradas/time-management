import datetime 
import uuid


class Alltask:
    alltask=[]

    def add_task(self,val):
        self.alltask.append(val)

class Task(Alltask):
    def __init__(self,task) -> None:
        self.task = task
        self.created_time = datetime.datetime.now()
        self.updated_time = "NA"
        self.completed_time = "NA"
        self.task_done = False
        self.id = uuid.uuid4().hex
        super().add_task(self)

    @staticmethod
    def update_task(obj,val):
        obj.task = val
        obj.updated_time = datetime.datetime.now()
    
    @staticmethod
    def task_done(obj):
        obj.task_done = True
        obj.completed_time = datetime.datetime.now()
        


while True:
    print(f"1.Add New Task\n2.Show all Task\n3.Show Incomplete Tasks\n4.Show Complete Tasks\n5.Update Task\n6.Mark A Task Completed\n")
    choice = int(input("Enter Option: "))
    print()

    if choice == 1:
        tsk = input("Enter New Task: ")
        tsk.split()[0] = Task(tsk)
        print("Task Created Successfully")
        print()

    if choice == 2:
        print()
        for idx,val in enumerate(Alltask.alltask):
            # print(f'Task:{idx+1}')
            print(f"ID - {val.id}")
            print(f"Task - {val.task}")
            print(f"Created Time - {val.created_time}")     
            print(f"Updated Time - {val.updated_time}")
            print(f"Completed - {val.task_done}")
            print(f"Completed Time- {val.completed_time}")
            print()


    if choice == 3:
        count = 0
        for val in Alltask.alltask:
            if val.task_done == False:
                print(f"ID - {val.id}")
                print(f"Task - {val.task}")
                print(f"Created Time - {val.created_time}")     
                print(f"Updated Time - {val.updated_time}")
                print(f"Completed - {val.task_done}")
                print(f"Completed Time- {val.completed_time}")
                print()
                count += 1
        
        if count == 0:
            print("No Incomplete Task")
            print()

    if choice == 4:
        count = 0
        for val in Alltask.alltask:
            if val.task_done == True:
                print(f"ID - {val.id}")
                print(f"Task - {val.task}")
                print(f"Created Time - {val.created_time}")     
                print(f"Updated Time - {val.updated_time}")
                print(f"Completed - {val.task_done}")
                print(f"Completed Time- {val.completed_time}")
                print()
                count += 1
        
        if count == 0:
            print("No Completed Task")
            print()

    
    if choice == 5:
        count = 0
        for val in Alltask.alltask:
            if val.updated_time == "NA":
                count+=1

        if count==0:
            print("No Task to Update")
            print()

        else:
            print("Select which Task to update")
            for idx,val in enumerate(Alltask.alltask):
                if val.updated_time == "NA":
                    print(f'Task No - {idx+1}')
                    print(f"ID - {val.id}")
                    print(f"Task - {val.task}")
                    print(f"Created Time - {val.created_time}")     
                    print(f"Updated Time - {val.updated_time}")
                    print(f"Completed - {val.task_done}")
                    print(f"Completed Time- {val.completed_time}")
                    print()

            tsk_no = int(input("Enter Task No: "))
            tsk_name = input("Enter New Task: ")

            Task.update_task(Alltask.alltask[tsk_no-1],tsk_name)
            print("Task updated successfully")
            print()

        

    
    if choice == 6:
        count = 0
        for val in Alltask.alltask:
            if val.task_done == False:
                count+=1

        if count==0:
            print("No Task to Complete")
            print()
        else:
            print("Select which Task to complete")
            for idx,val in enumerate(Alltask.alltask):
                if val.task_done == False:
                    print(f'Task No - {idx+1}')
                    print(f"ID - {val.id}")
                    print(f"Task - {val.task}")
                    print(f"Created Time - {val.created_time}")     
                    print(f"Updated Time - {val.updated_time}")
                    print(f"Completed - {val.task_done}")
                    print(f"Completed Time- {val.completed_time}")
                    print()

            tsk_no = int(input("Enter Task No: "))
            Task.task_done(Alltask.alltask[tsk_no-1])

            print("Task Completed Successfully")
            print()
