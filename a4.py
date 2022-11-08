import subprocess
import os

# Runs the exe, returns True if access is not denied
def run_exe(password):
    p = subprocess.Popen(os.getcwd() + '\Group5.program1.exe', stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    text = p.communicate(input=password.encode())[0]
    print(text)
    return text[-10:-3] != b'denined'
    
# TODO: come up with brute force?
s = f'sZ@x4$8teCM_zKWG(M()Sy@K%*Wf=C_P^P$lueyqk+OAvdbcWq42E@A(@zG0p3uZG+f8UNl%nV9V9Ko@&WFZWsleo)q)UNiEZ$(y-aEil$O8c4kAlT&QvTco0aTZqqtXNC)(P$#ZaxN82BbI0_8aUOjg!5M+V4&(T^sX8p9v6az-fsJH=l%sFsc-t#i9z%eKFSn'

for i in range(len(s)-17):
    if run_exe(s[i:i+17]):
        print('found it!')
        print(s[i:i+17])
        break