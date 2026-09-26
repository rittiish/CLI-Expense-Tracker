import json

# Try to load existing expenses from a file named "expenses.json"
try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []#this is a nested list

print("Expense Tracker Programme")
while True:
    
    print("-----Enter A Valid Choice------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. View Total")
    print("5. Exit")


    choice = input("Enter your choice: ")
    if choice=="1":
        serial_num=input("Enter serial number:")
        amount= input("Enter the amount:")
        category=input("Enter the category:")
        description=input("Enter the discription:")
        

        expense=[serial_num,amount,category,description]
        expenses.append(expense)
        with open("expenses.json", "w") as file:
            json.dump(expenses, file)

        print("Expense added successfully")



    elif choice =="2":
        print("===EXPENSE DETAILS===")
        if not expenses:
            print("no expense recored yet")
        for expense in expenses:
            print(expense)


    
    elif choice == "3":
        num = input("Enter the serial number: ")
        found = False
        for i in range(len(expenses)):
            if expenses[i][0] == num: # since ive use a nested list so the line checks the 0 item of every list of main list"expenses"
                expenses.pop(i)
                with open("expenses.json", "w") as file:
                            json.dump(expenses, file)
                print("Expense deleted successfully")
                found = True
                break
        if not found:# not here flips the found and check is it still false
            print("Expense not found.")



    elif choice == "4":
        total=0
        for i in range(len(expenses)):
            num=int(expenses[i][1])
            total+=num
        print (f"Total expense is:${total}")



    elif choice =="5":
        print("Thank you for Visiting Program")
        break



    
    else:
        print("Enter a valid choice")