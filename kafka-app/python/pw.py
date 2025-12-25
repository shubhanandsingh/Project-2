#! python3
#pw.py -- I will use this may be
password = {'email':'12sdhlsqhfh33ff', 'username':'shubhanandsingh', 'password':'653153'}
import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
account = sys.argv[1]
if account in password:
    pyperclip.copy(password[account])
    print('password for' + account + 'copied to clipboard')
else:
    print('there is no account named' + account)