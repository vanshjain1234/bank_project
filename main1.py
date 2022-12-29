

accounts = {'0':['hello123','Vansh','1','123',1000000] , '1':['hello123','Anuj','1','123',0]}
# main code

print('Welcome to the prestigious Star Bank!')

print('Select the action: \n 1. Login to access bank accont : Enter "1" \n 2. Create/Open a new bank account : Enter "2"')

action = input('\nEnter the option selected: ')

if action == '1':
   
   account_number = input('Enter the account number: ')
   
   password = input('Enter the password: ')
   
   if accounts[account_number][0] == password:
      print('Login Successful')

      print('Hey ' + accounts[account_number][1] + '!\nWhat would you like to do today...')

      print('Select the action: \n 1. Account Details : Enter "1" \n 2. Money Transaction : Enter "2"  \n 3. Help / Contact Us : Enter "3"')
      option = input('Select the option: ')
         if option == '1':
            pass
         elif option == '2':
            print('Select the action:\n1. add money: Enter "1"\n2. tranfer money: Enter "2"')
            option1 = input('Enter your option')

            if option1 == '1':
               amount = input('Enter the amount you want to add: ')
               accounts[account_number][4]
             
   
elif action == '2':
   print('For a new account, kindly provide us some details of yours...')
   name = input('Enter your name: ')
   age = input('Enter the age: ')
   PAN = input('Enter your pan card number: ')
   password = input('Enter your password: ')
   account_number = len(accounts)
   accounts[str(account_number)] = [password,name,age,PAN,0]
   
   print('Your account has been successfully created...')

print(accounts)

