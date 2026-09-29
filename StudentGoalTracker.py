import json
from datetime import datetime
FILE="DATA.json"
try:
    with open(FILE,"r") as f:
        goal=json.load(f)
except:
    goal=[]
def Save():
    # just writing everything back to json
    with open(FILE,"w") as f:
        json.dump(goal,f,indent=4)
def Add():
    print("\n===== Add Your Goals ====")
    goalText=input("Goal: ")
    subj=input("Subject: ")

    # loop until date is valid
    while True:
        duedate=input("Enter Due Date'dd-mm-yyyy':")
        try:
            dueD=datetime.strptime(duedate,"%d-%m-%Y")
            today=datetime.today().date()
            if dueD.date()<today:
                print("Due date can't be in past")
            else:
                break
        except ValueError:
            print("Please enter like this--[dd-mm-yyyy]")
    # loop until priority is valid
    while True:
        print("\nChoose priority of the task:")
        print("1. High")
        print("2. Medium")
        print("3. Low")
        pri=input()
        if pri=="1":
            priority="High"
            break
        elif pri=="2":
            priority="Medium"
            break
        elif pri=="3":
            priority="Low"
            break
        else:
            print("Enter 1, 2 or 3 to choose priority")
    item={
        "goal": goalText,
        "subject": subj,
        "deadline": duedate,
        "priority": priority,
        "progress": 0,
    }
    goal.append(item)
    Save()
    print("\nGoal added successfully!!")
def View():
    if len(goal)==0:
        print("\nNo goals available right now.")
        return
    # just using a standard loop instead of enumerate to keep it old school
    for i in range(len(goal)):
        curr_goal = goal[i]
        print("\n------------------")
        print("Goal #" + str(i + 1))
        print("Goal      :", curr_goal["goal"])
        print("Subject   :", curr_goal["subject"])
        print("Deadline  :", curr_goal["deadline"])
        print("Priority  :", curr_goal["priority"])
        print("Progress  :", str(curr_goal["progress"])+"%")
        # quick inline check for status
        if curr_goal["progress"]==100:
            status="Completed"
        else:
            status="In Progress"
        print("Status    :", status)
    print("------------------")
def UpdateProgress():
    View()
    if len(goal)==0:
        return
    try:
        num=int(input("\nEnter goal number to update: "))
    except ValueError:
        print("Bruh, enter a valid number.")
        return
    if num<1 or num>len(goal):
        print("There is no goal with this number")
        return
    while True:
        try:
            prog = int(input("Enter progress between 0 and 100: "))
        except ValueError:
            print("Numbers only please...")
            continue
        if prog<0 or prog>100:
            print("between 0 and 100")
            continue
        break
    goal[num - 1]["progress"] = prog
    Save()
    print("\nProgress updated successfully!")
def ProgressRepo():
    if not goal:
        print("\nNo goals available to report on.")
        return
    totalProg=0
    completed_count=0
    for g in goal:
        totalProg+=g["progress"]
        if g["progress"]==100:
            completed_count+=1
    avg=totalProg/len(goal)
    print("\n========== PROGRESS REPORT ========== ")
    print("Total Goals      :", len(goal))
    print("Completed Goals  :", completed_count)
    print("Overall Progress :", round(avg, 2), "%")
    print("===================================== ")
# main program loop
while True:
    print("\n\n===== STUDENT GOAL TRACKER ===== ")
    print("1. Add Goal")
    print("2. View Goals")
    print("3. Update Progress")
    print("4. Progress Report")
    print("5. Exit")
    choice=input("\nEnter your choice:- ")
    if choice=="1":
        Add()
    elif choice=="2":
        View()
    elif choice=="3":
        UpdateProgress()
    elif choice=="4":
        ProgressRepo()
    elif choice=="5":
        Save()
        print("\nSaving goals... Bye bye!")
        break
    else:
        print("\nInvalid choice")