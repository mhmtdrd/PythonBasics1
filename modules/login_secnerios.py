#from modules/login_steps import enter_username,enter_passord
from modules.login_steps import * #read the file and have the reference to function

#from <source package> import < function , class name or simply * >
import time
#import modules.login_steps
#colling the functions/execution
enter_username('john')
enter_password()
click_login()
time.sleep(15) # hold the execution for 15 seconds
logout()





