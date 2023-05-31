#set of available pins
pins = {1234, 5678, 9876}
#list of available accounts
accounts=[
    (1111, "Aly", 1000),(2222, "Ahmed", 2000),(3333, "Khaled", 3000)
]
pin = int(input("Enter your PIN: "))
#check if the PIN is valid
if pin in pins:
    # the user should enter the account number
    account_number = int(input("Enter your account number: "))
else:
     print("invalid pin")
    
#find the account with the given account number
for acc in accounts:
    if acc[0] == account_number:
        account = acc
        break
#check if the account exists or not 
if account is None:
    print("invalid account number")
#check on the operation
print("1.Check balance")
print("2.Withdraw money")
operation=int(input("enter your choice: "))
    
#check the user's choice and perform the appropriate action
if operation==1:
    print("your balance is:", account[2])
elif operation==2:
    amount=int(input("enter the amount to withdraw: "))
    if amount>account[2]:
        print("no enought money")
    else:
        print("successful")
else:
    print("invalid choice")
    

