import string
import getpass

#function to get password
def check_password_strength():
   password = getpass.getpass('Enter the password: ')
   strength = 0
   remarks = ''
   lower_count = upper_count = num_count = wspace_count = special_count = 0

#analysing the password
   for char in list(password):
       if char in string.ascii_lowercase:
           lower_count += 1
       elif char in string.ascii_uppercase:
           upper_count += 1
       elif char in string.digits:
           num_count += 1
       elif char == ' ':
           wspace_count += 1
       else:
           special_count += 1

#counting the 'strength' of the pw
   if lower_count >= 1:
       strength += 1
   if upper_count >= 1:
       strength += 1
   if num_count >= 1:
       strength += 1
   if wspace_count >= 1:
       strength += 1
   if special_count >= 1:
       strength += 1

#conclusion and suggestion for the pw
   if strength == 1:
       remarks = ('That\'s a very weak password.'
           ' Please change it as soon as possible.')
   elif strength == 2:
       remarks = ('That\'s a very hackable password.'
           ' You should consider using a tougher password.')
   elif strength == 3:
       remarks = 'Your password is okay, but it can be improved.'
   elif strength == 4:
       remarks = ('Your password is hard to guess.'
                ' But you could make it even more secure.')
   elif strength == 5:
       remarks = ('That\'s a strong password!!!'
           ' Hackers don\'t have a chance guessing that password!')

#details about the pw
   print('Your password has:-')
   print(f'{lower_count} lowercase letters')
   print(f'{upper_count} uppercase letters')
   print(f'{num_count} digits')
   print(f'{wspace_count} whitespaces')
   print(f'{special_count} special characters')
   print(f'Password Score: {strength / 5}')
   print(f'Remarks: {remarks}')

#prg repeating condition
def check_pwd(another_pw=False):
   valid = False
   if another_pw:
       choice = input('Do you want to check another password\'s strength (y/n) : ')
   else:
       choice = input('Do you want to check your password\'s strength (y/n) : ')

   while not valid:
       if choice.lower() == 'y':
           return True
       elif choice.lower() == 'n':
           print('Exiting...')
           return False
       else:
           print('Invalid input...please try again. \n')
           break

#main
if __name__ == '__main__':
   print('===== Welcome to Password Strength Checker =====')
   check_pw = check_pwd()
   while check_pw:
       check_password_strength()
       check_pw = check_pwd(True)