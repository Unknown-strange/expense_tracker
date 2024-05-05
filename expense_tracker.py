def main():

    items = input("List the items you bought: ")
    item_list = [item for item in items.split(",")]
        
    for item in item_list:
        print(item)
    Add_up = input("Do you want to add more to the list yes/no : ").lower()
        
    if Add_up == "yes":
        addition(item_list)
    else:
        amount(item_list)
            
            
def addition(item_list):
    while True:
        #item_list =  [item for item in item_list]
        new_input = input("new Items, (type exit to leave): ")
        
        print("")
        
        if new_input == "exit":
            break
        else:
            item_list.append(new_input.strip())
    delet_item(item_list)


def delet_item(amount_list):
    while True:
        amount_list = [list for list in amount_list]
        delet_input = input("Do you wan to delet an item, yes/no :")
        
        if delet_input == "yes":
        
            for list in amount_list:
                print(list) 
                
                print("")   
                
            del_input = input("What do you want to delet: ")
            for item in amount_list:
                if del_input in item:
                    amount_list.remove(item)
                    break
            else:
                print("item not found")
        elif delet_input == "no":
            break
        else:
            print('Enter "yes" or "no"')
    for list in amount_list:
        print(list)
    amount(amount_list)




def amount(item_list):
    try:
        amount_list = []
        for item in item_list:
            amount_input = float(input(f"what's the amount of {item} in Ghc: "))
            amount_list.append(f'{item}-{amount_input}')
        
        for list in amount_list:
            print(list)
                
    
    except ValueError:
        print('INPUT  THE VALID INTEGERS')          
    categorize_expense(amount_list)
    
    


def categorize_expense(amount_list):
    categories = {
        "Groceries" : ["food","groceries","drinks"],
        "Utilities" : ["electricity","water","gas"],
        "Transpotation" : ["fuel","public transport"],
        "Entertainment" : ["movies", "restaurants","concerts"],
        "Housing" : ["rent","mortgage"],
        "Others" : []
    }
    
    categorized_expenses = {categorize : [] for categorize in categories}
    
    for list in amount_list:
        categorized = False
        for categorize , keywords in categories.items():
            for keyword in keywords:
                if keyword in list.lower():
                    categorized_expenses[categorize].append(list)
                    categorized = True
                    break
            if categorized:
                break
        else:
            categorized_expenses["Others"].append(list)    

          
    for category, expenses_list in categorized_expenses.items():
        print(f'{category}:')
        for expense in expenses_list:
            print(f'- {expense}')
        
    summary(categorized_expenses)
    report(categorized_expenses)
        
            

def summary(categorized_expenses):
   for category, expense_list in categorized_expenses.items():
        total = 0
        for expense in expense_list:
            amount = float(expense.split("-")[1])
            total += amount
        print("Summary of account")
        print(f'Total {category} is Ghc{total}')
        
        
        
def report(categorized_expenses):
     groceries = categorized_expenses.get("Groceries",0)
     utilities = categorized_expenses.get("Utilities",0)
     transportation = categorized_expenses.get("Transportation",0)
     entertainment = categorized_expenses.get("Entertainment",0)
     housing = categorized_expenses.get("Housing",0)
     others = categorized_expenses.get("Others",0)
     if groceries > entertainment and groceries > housing and groceries > others:
         print("Good expense")
     else:
         print("Bad expense")
     
    

if __name__ == "__main__":
    main()