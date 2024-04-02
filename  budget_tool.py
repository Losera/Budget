import xlsxwriter

def gross_monthly_income():
    income = float(input("Enter this months income:" ))
    expenses = {}
    while True:
        category = input("Enter expense category or done to finish")
        if category.lower() == "done":
            break
        amount = float(input(f"Enter amount for {category}: "))
        expenses[category] = amount
        
    return income, expenses
    

def calculate_budget(income,expenses):
    gross_expenses = sum(expenses.values())
    balance = income - gross_expenses
    return gross_expenses, balance, income

def display_budget(income, gross_expenses,balance):
    budget_summary = {
        "Income": income,
        "Gross Expenses": gross_expenses,
        "Balance": balance
    }

    print("\nBudget Summary")
    for name, value in budget_summary.items():
        print(f"Total {name}: {value}")

    return budget_summary


income, expenses = gross_monthly_income()
gross_expenses, balance, income = calculate_budget(income, expenses)
budget_summary = display_budget(income, gross_expenses, balance)


workbook = xlsxwriter.Workbook('budget_tool.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

for name,value in budget_summary.items():
    worksheet.write(row,col,name)
    worksheet.write(row,col+1,value)
    row += 1

for category,amount in expenses.items():
    worksheet.write(row,col,category)
    worksheet.write(row,col+1,amount)
    row += 1

workbook.close()