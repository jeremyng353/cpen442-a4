import subprocess
import os

# Runs the exe, returns True if access is not denied
def run_exe(password):
    p = subprocess.Popen(os.getcwd() + '\Group5.program1.exe', stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    return p.communicate(input=password.encode())[0][-10:-3] != b'denined'
    
# TODO: come up with brute force?
