import ctypes
import time
import sys
from datetime import datetime

def execute():
    print(f'{time.ctime()}, Start time')
    # just open a simple dialog box
    ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
    print(f"{time.ctime()}, End time (it ends before you've clicked at dialog box)")

# Define execution day as string
dt_str = datetime.now().date().strftime('%Y_%m_%d')
# Save a reference to the original standard output
original_stdout = sys.stdout 
# Create a log file in the same folder of this .py
# but it in a sub-folder just for your logs
# just to keep it clean =D
with open(f'logfiles\{dt_str}_test_py_sh_bat.txt', 'w') as logfile:
    # Change the standard output to the file we created.
    sys.stdout = logfile 
    # Call your main code 
    execute()
    # Change the standard output to original
    sys.stdout = original_stdout   