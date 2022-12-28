
class Account:
   def __init__(self,name,account_no,password):
      self.name = name
      self.acc_no = acc_no


accounts = {'00000':['hello123','Vansh Jain']}
# main code

print('Welcome to the prestigious Star Bank!')

print('Select the action: \n 1. Login to access bank accont : Enter "1" \n 2. Create/Open a new bank account : Enter "2"')

action = input('\nEnter the option selected: ')

if action == '1':
   
   account_number = input('Enter the account number: ')
   
   password = input('Enter the password: ')
   
   if accounts[account_number][0] == password:
      print('Login Succesful')

      print('Hey ' + accounts[account_number][1] + '!\nWhat would you like to do today...')
      print('Select the action: \n 1. Account Details : Enter "1" \n 2. Transfer Money : Enter "2"  \n 3. Help / Contact Us : Enter "3"')

    
   
elif action == '2':
   print('For a new account, kindly provide us some details of yours...')
   name = 
   print('A bank representative will visit you shortly')
